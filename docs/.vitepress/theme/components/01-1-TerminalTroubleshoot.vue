<script setup lang="ts">
import { ref, onUnmounted } from 'vue'

interface Step {
  id: string
  title: string
  icon: string
  command?: string
  description: string
  check: () => boolean
}

const currentStep = ref(0)
const commandInput = ref('')
const showResult = ref(false)
const isCorrect = ref(false)
const typedCommand = ref('')
let typeInterval: number | null = null

const steps: Step[] = [
  {
    id: 'spell',
    title: '拼写检查',
    icon: '🔤',
    description: '检查命令是否拼写正确，没有多余的空格',
    check: () => commandInput.value.trim() === 'pnpm install'
  },
  {
    id: 'installed',
    title: '工具已安装',
    icon: '✅',
    command: 'node -v',
    description: '确认工具已安装并能正常执行',
    check: () => commandInput.value.trim() === 'node -v'
  },
  {
    id: 'directory',
    title: '正确目录',
    icon: '📁',
    command: 'pwd',
    description: '确认在项目目录下，有 package.json 文件',
    check: () => commandInput.value.trim() === 'pwd'
  },
  {
    id: 'reload',
    title: '重新加载',
    icon: '🔄',
    command: 'source ~/.zshrc',
    description: '安装工具后需要重启终端或重新加载配置',
    check: () => commandInput.value.trim().startsWith('source')
  }
]

function startStep(index: number) {
  currentStep.value = index
  commandInput.value = ''
  showResult.value = false
  typedCommand.value = ''

  if (steps[index].command) {
    let i = 0
    const cmd = steps[index].command!
    typeInterval = window.setInterval(() => {
      if (i <= cmd.length) {
        typedCommand.value = cmd.slice(0, i)
        i++
      } else {
        clearInterval(typeInterval!)
      }
    }, 50)
  }
}

function checkCommand() {
  isCorrect.value = steps[currentStep.value].check()
  showResult.value = true
}

function nextStep() {
  if (currentStep.value < steps.length - 1) {
    startStep(currentStep.value + 1)
  }
}

function reset() {
  currentStep.value = 0
  commandInput.value = ''
  showResult.value = false
  typedCommand.value = ''
  if (typeInterval) clearInterval(typeInterval)
}

onUnmounted(() => {
  if (typeInterval) clearInterval(typeInterval)
})
</script>

<template>
  <div class="terminal-troubleshoot">
    <div class="flow-diagram">
      <div
        v-for="(step, index) in steps"
        :key="step.id"
        class="step-node"
        :class="{
          active: currentStep === index,
          completed: currentStep > index,
          clickable: currentStep >= index
        }"
        @click="currentStep >= index && startStep(index)"
      >
        <div class="step-icon">{{ step.icon }}</div>
        <div class="step-title">{{ step.title }}</div>
        <div v-if="currentStep > index" class="step-check">✓</div>
      </div>
    </div>

    <div class="terminal-section">
      <div class="terminal-header">
        <div class="terminal-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <span class="terminal-title">排查终端</span>
      </div>

      <div class="terminal-body">
        <div class="step-info">
          <div class="current-step-title">
            {{ steps[currentStep].icon }} {{ steps[currentStep].title }}
          </div>
          <div class="step-description">{{ steps[currentStep].description }}</div>
        </div>

        <div class="command-area">
          <div class="prompt">
            <span class="prompt-symbol">$</span>
            <input
              v-model="commandInput"
              type="text"
              class="command-input"
              placeholder="输入命令..."
              @keyup.enter="checkCommand"
            />
          </div>

          <div v-if="typedCommand && !commandInput" class="hint">
            提示: {{ typedCommand }}
          </div>

          <div v-if="showResult" class="result" :class="{ correct: isCorrect, wrong: !isCorrect }">
            <div v-if="isCorrect">
              ✅ 正确！{{ currentStep < steps.length - 1 ? '继续下一步' : '排查完成' }}
            </div>
            <div v-else>
              ❌ 不正确，请检查拼写
            </div>
          </div>
        </div>

        <div class="actions">
          <button v-if="showResult && isCorrect && currentStep < steps.length - 1" class="btn-primary" @click="nextStep">
            下一步 →
          </button>
          <button v-if="showResult && !isCorrect" class="btn-secondary" @click="commandInput = ''; showResult = false">
            重试
          </button>
          <button class="btn-ghost" @click="reset">重新开始</button>
        </div>
      </div>
    </div>

    <div class="tips">
      <div class="tip-item">
        <span class="tip-icon">💡</span>
        <span>不确定错误原因？直接把报错信息发给 AI</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.terminal-troubleshoot {
  background: linear-gradient(180deg, #1e1e2e 0%, #2d2d44 100%);
  border-radius: 16px;
  padding: 20px;
  color: #f0f0f0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.flow-diagram {
  display: flex;
  justify-content: space-between;
  margin-bottom: 24px;
  position: relative;
}

.flow-diagram::before {
  content: '';
  position: absolute;
  top: 24px;
  left: 12%;
  right: 12%;
  height: 2px;
  background: linear-gradient(90deg, #34c759 0%, #34c759 var(--progress, 0%), #3a3a3c var(--progress, 0%));
  z-index: 0;
}

.step-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  z-index: 1;
  cursor: default;
  transition: all 0.3s ease;
}

.step-node.clickable {
  cursor: pointer;
}

.step-node.clickable:hover .step-icon {
  transform: scale(1.1);
}

.step-icon {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: #3a3a3c;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.step-node.active .step-icon {
  background: #007aff;
  border-color: #5ac8fa;
  box-shadow: 0 0 20px rgba(0, 122, 255, 0.4);
}

.step-node.completed .step-icon {
  background: #34c759;
}

.step-title {
  font-size: 12px;
  color: #8e8e93;
  text-align: center;
}

.step-node.active .step-title {
  color: #fff;
  font-weight: 600;
}

.step-check {
  position: absolute;
  bottom: -4px;
  right: -4px;
  width: 20px;
  height: 20px;
  background: #34c759;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
}

.terminal-section {
  background: #0d0d0f;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 16px;
}

.terminal-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: linear-gradient(180deg, #2d2d44 0%, #1e1e2e 100%);
  border-bottom: 1px solid #3a3a3c;
}

.terminal-dots {
  display: flex;
  gap: 6px;
}

.terminal-dots span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.terminal-dots span:nth-child(1) { background: #ff5f56; }
.terminal-dots span:nth-child(2) { background: #ffbd2e; }
.terminal-dots span:nth-child(3) { background: #27c93f; }

.terminal-title {
  font-size: 13px;
  color: #8e8e93;
}

.terminal-body {
  padding: 20px;
}

.step-info {
  margin-bottom: 20px;
}

.current-step-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
}

.step-description {
  font-size: 14px;
  color: #8e8e93;
}

.command-area {
  margin-bottom: 20px;
}

.prompt {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #1e1e2e;
  padding: 12px 16px;
  border-radius: 8px;
  border: 1px solid #3a3a3c;
}

.prompt-symbol {
  color: #34c759;
  font-weight: 600;
  font-family: 'SF Mono', Monaco, monospace;
}

.command-input {
  flex: 1;
  background: transparent;
  border: none;
  color: #f0f0f0;
  font-size: 14px;
  font-family: 'SF Mono', Monaco, monospace;
  outline: none;
}

.command-input::placeholder {
  color: #5a5a5c;
}

.hint {
  margin-top: 8px;
  font-size: 12px;
  color: #8e8e93;
  font-family: 'SF Mono', Monaco, monospace;
}

.result {
  margin-top: 16px;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 14px;
}

.result.correct {
  background: rgba(52, 199, 89, 0.1);
  border: 1px solid #34c759;
  color: #34c759;
}

.result.wrong {
  background: rgba(255, 59, 48, 0.1);
  border: 1px solid #ff3b30;
  color: #ff3b30;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.btn-primary, .btn-secondary, .btn-ghost {
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.btn-primary {
  background: #007aff;
  color: white;
}

.btn-primary:hover {
  background: #0051d5;
}

.btn-secondary {
  background: #3a3a3c;
  color: #f0f0f0;
}

.btn-secondary:hover {
  background: #48484a;
}

.btn-ghost {
  background: transparent;
  color: #8e8e93;
}

.btn-ghost:hover {
  color: #f0f0f0;
}

.tips {
  background: rgba(255, 204, 0, 0.1);
  border: 1px solid rgba(255, 204, 0, 0.3);
  border-radius: 10px;
  padding: 12px 16px;
}

.tip-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #ffd60a;
}

@media (max-width: 640px) {
  .flow-diagram {
    flex-wrap: wrap;
    gap: 16px;
  }

  .flow-diagram::before {
    display: none;
  }

  .step-node {
    flex: 1;
    min-width: 60px;
  }

  .step-title {
    font-size: 10px;
  }
}
</style>