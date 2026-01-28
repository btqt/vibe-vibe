<script setup lang="ts">
import { ref, computed } from 'vue'

interface InstallStep {
  name: string
  status: 'pending' | 'running' | 'done' | 'error'
  output: string[]
}

const isInstalling = ref(false)
const currentStepIndex = ref(0)
const progress = ref(0)
const showComplete = ref(false)

const steps: InstallStep[] = [
  { name: '解析依赖', status: 'pending', output: [] },
  { name: '下载包', status: 'pending', output: [] },
  { name: '链接依赖', status: 'pending', output: [] },
  { name: '构建项目', status: 'pending', output: [] }
]

const currentSteps = ref<InstallStep[]>(JSON.parse(JSON.stringify(steps)))

const sampleOutputs = [
  ['Resolving dependencies...', '  + react@18.2.0', '  + next@14.1.0', '  + typescript@5.3.0', 'Found 0 vulnerabilities'],
  ['Packages: +523', '++++++++++++++++++++++++++++++++++++++++++++++++++', 'Downloading registry.npmjs.org/react/18.2.0...', 'Downloading registry.npmjs.org/next/14.1.0...', 'Progress: resolved 523, reused 480, downloaded 43, added 523, done'],
  ['Linking dependencies...', '  + node_modules/.pnpm/react@18.2.0', '  + node_modules/.pnpm/next@14.1.0', '  + node_modules/react', '  + node_modules/next', 'Already up to date'],
  ['Building project...', '  > next build', '  - info Creating an optimized production build...', '  - info Compiled successfully', '  - info Linting and checking validity of types...']
]

async function startInstall() {
  if (isInstalling.value) return

  isInstalling.value = true
  currentStepIndex.value = 0
  progress.value = 0
  showComplete.value = false
  currentSteps.value = JSON.parse(JSON.stringify(steps))

  for (let i = 0; i < currentSteps.value.length; i++) {
    currentStepIndex.value = i
    currentSteps.value[i].status = 'running'

    // 模拟输出逐行显示
    for (const line of sampleOutputs[i]) {
      currentSteps.value[i].output.push(line)
      await new Promise(r => setTimeout(r, 150))
    }

    currentSteps.value[i].status = 'done'
    progress.value = ((i + 1) / currentSteps.value.length) * 100

    await new Promise(r => setTimeout(r, 300))
  }

  showComplete.value = true
  isInstalling.value = false
}

function reset() {
  isInstalling.value = false
  currentStepIndex.value = 0
  progress.value = 0
  showComplete.value = false
  currentSteps.value = JSON.parse(JSON.stringify(steps))
}

const statusIcon = computed(() => (status: string) => {
  switch (status) {
    case 'running': return '⏳'
    case 'done': return '✓'
    case 'error': return '✗'
    default: return '○'
  }
})
</script>

<template>
  <div class="pnpm-install">
    <div class="install-window">
      <!-- Header -->
      <div class="window-header">
        <div class="window-controls">
          <span class="control close"></span>
          <span class="control minimize"></span>
          <span class="control maximize"></span>
        </div>
        <div class="window-title">
          <svg class="pnpm-icon" viewBox="0 0 24 24" fill="none">
            <path d="M12 2L2 7l10 5 10-5-10-5z" fill="#f9ad00"/>
            <path d="M2 17l10 5 10-5" fill="#f9ad00"/>
            <path d="M2 12l10 5 10-5" fill="#f9ad00"/>
          </svg>
          pnpm install
        </div>
        <button
          class="action-btn"
          :class="{ active: showComplete }"
          @click="showComplete ? reset() : startInstall()"
          :disabled="isInstalling"
        >
          <span v-if="isInstalling" class="spinner"></span>
          <span v-else>{{ showComplete ? '↺ 重置' : '▶ 安装' }}</span>
        </button>
      </div>

      <!-- Progress Bar -->
      <div class="progress-section">
        <div class="progress-bar">
          <div class="progress-fill" :style="{ width: progress + '%' }"></div>
        </div>
        <div class="progress-text">{{ Math.round(progress) }}%</div>
      </div>

      <!-- Install Steps -->
      <div class="steps-container">
        <div
          v-for="(step, index) in currentSteps"
          :key="step.name"
          class="step-item"
          :class="{ active: index === currentStepIndex && isInstalling, done: step.status === 'done' }"
        >
          <div class="step-header">
            <span class="step-icon">{{ statusIcon(step.status) }}</span>
            <span class="step-name">{{ step.name }}</span>
            <span v-if="step.status === 'running'" class="step-pulse"></span>
          </div>
          <div v-if="step.output.length > 0" class="step-output">
            <div v-for="(line, i) in step.output" :key="i" class="output-line">
              {{ line }}
            </div>
          </div>
        </div>
      </div>

      <!-- Complete Message -->
      <div v-if="showComplete" class="complete-banner">
        <div class="complete-icon">🎉</div>
        <div class="complete-text">
          <strong>安装完成！</strong>
          <span>项目依赖已就绪，可以开始开发了</span>
        </div>
        <div class="complete-hint">
          运行 <code>pnpm dev</code> 启动开发服务器
        </div>
      </div>

      <!-- Info Cards -->
      <div class="info-section">
        <div class="info-card">
          <div class="info-icon">📦</div>
          <div class="info-title">解析依赖</div>
          <div class="info-desc">分析 package.json，确定需要安装的包版本</div>
        </div>
        <div class="info-card">
          <div class="info-icon">⬇️</div>
          <div class="info-title">下载包</div>
          <div class="info-desc">从 npm 仓库下载所需代码包</div>
        </div>
        <div class="info-card">
          <div class="info-icon">🔗</div>
          <div class="info-title">链接依赖</div>
          <div class="info-desc">pnpm 使用硬链接技术节省磁盘空间</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pnpm-install {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  margin: 20px 0;
}

.install-window {
  background: #1e1e2e;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

/* Window Header */
.window-header {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: linear-gradient(180deg, #2d2d44 0%, #1e1e2e 100%);
  border-bottom: 1px solid #2d2d44;
}

.window-controls {
  display: flex;
  gap: 8px;
}

.control {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.control.close { background: #ff5f56; }
.control.minimize { background: #ffbd2e; }
.control.maximize { background: #27c93f; }

.window-title {
  flex: 1;
  text-align: center;
  color: #a0a0b0;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.pnpm-icon {
  width: 16px;
  height: 16px;
}

.action-btn {
  padding: 6px 14px;
  background: #f9ad00;
  color: #1e1e2e;
  border: none;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 4px;
}

.action-btn:hover:not(:disabled) {
  background: #ffb833;
}

.action-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.action-btn.active {
  background: #4a5568;
  color: #e2e8f0;
}

.spinner {
  width: 12px;
  height: 12px;
  border: 2px solid rgba(30, 30, 46, 0.3);
  border-top-color: #1e1e2e;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Progress Section */
.progress-section {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  background: #16162a;
  border-bottom: 1px solid #2d2d44;
}

.progress-bar {
  flex: 1;
  height: 6px;
  background: #2d2d44;
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #f9ad00, #ffb833);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 12px;
  color: #a0aec0;
  font-weight: 500;
  min-width: 36px;
  text-align: right;
}

/* Steps Container */
.steps-container {
  padding: 16px 20px;
  min-height: 200px;
}

.step-item {
  margin-bottom: 12px;
  padding: 12px 16px;
  background: #252542;
  border-radius: 8px;
  border: 1px solid #2d2d44;
  transition: all 0.3s;
}

.step-item.active {
  border-color: #f9ad00;
  background: rgba(249, 173, 0, 0.05);
}

.step-item.done {
  border-color: #48bb78;
  background: rgba(72, 187, 120, 0.05);
}

.step-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.step-icon {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}

.step-name {
  flex: 1;
  font-size: 14px;
  color: #e2e8f0;
  font-weight: 500;
}

.step-pulse {
  width: 8px;
  height: 8px;
  background: #f9ad00;
  border-radius: 50%;
  animation: pulse 1s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(1.2); }
}

.step-output {
  margin-top: 10px;
  padding: 10px 12px;
  background: #1e1e2e;
  border-radius: 6px;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 11px;
  line-height: 1.5;
}

.output-line {
  color: #a0aec0;
  white-space: pre-wrap;
  word-break: break-all;
}

.output-line:nth-child(odd) {
  color: #718096;
}

/* Complete Banner */
.complete-banner {
  margin: 0 20px 16px;
  padding: 16px 20px;
  background: linear-gradient(135deg, #276749 0%, #48bb78 100%);
  border-radius: 10px;
  text-align: center;
  animation: slideDown 0.3s ease;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.complete-icon {
  font-size: 32px;
  margin-bottom: 8px;
}

.complete-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 10px;
}

.complete-text strong {
  font-size: 16px;
  color: white;
}

.complete-text span {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.9);
}

.complete-hint {
  padding: 8px 12px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 6px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.8);
}

.complete-hint code {
  background: rgba(255, 255, 255, 0.2);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'SF Mono', Monaco, monospace;
}

/* Info Section */
.info-section {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  padding: 16px 20px;
  background: #16162a;
  border-top: 1px solid #2d2d44;
}

.info-card {
  padding: 14px;
  background: #252542;
  border-radius: 8px;
  text-align: center;
}

.info-icon {
  font-size: 20px;
  margin-bottom: 6px;
}

.info-title {
  font-size: 13px;
  font-weight: 600;
  color: #e2e8f0;
  margin-bottom: 4px;
}

.info-desc {
  font-size: 11px;
  color: #718096;
  line-height: 1.4;
}

@media (max-width: 640px) {
  .info-section {
    grid-template-columns: 1fr;
  }

  .step-output {
    font-size: 10px;
  }
}
</style>
