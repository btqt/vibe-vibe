<script setup lang="ts">
import { ref, computed } from 'vue'

interface Package {
  name: string
  size: number
  shared: boolean
}

const packages = ref<Package[]>([
  { name: 'react', size: 15, shared: true },
  { name: 'react-dom', size: 25, shared: true },
  { name: 'next', size: 45, shared: false },
  { name: 'typescript', size: 35, shared: true },
  { name: 'eslint', size: 20, shared: true },
  { name: 'prettier', size: 8, shared: true },
  { name: 'axios', size: 12, shared: false },
  { name: 'lodash', size: 18, shared: false },
])

const projectCount = ref(3)
const selectedManager = ref<'npm' | 'pnpm'>('npm')

const npmTotalSize = computed(() => {
  return packages.value.reduce((sum, p) => sum + p.size, 0) * projectCount.value
})

const pnpmTotalSize = computed(() => {
  const sharedSize = packages.value.filter(p => p.shared).reduce((sum, p) => sum + p.size, 0)
  const uniqueSize = packages.value.filter(p => !p.shared).reduce((sum, p) => sum + p.size, 0)
  return sharedSize + uniqueSize * projectCount.value
})

const savings = computed(() => {
  const saved = npmTotalSize.value - pnpmTotalSize.value
  const percentage = Math.round((saved / npmTotalSize.value) * 100)
  return { size: saved, percentage }
})

const currentTotal = computed(() => {
  return selectedManager.value === 'npm' ? npmTotalSize.value : pnpmTotalSize.value
})

function formatSize(size: number): string {
  return `${size}MB`
}
</script>

<template>
  <div class="pm-compare">
    <div class="compare-window">
      <!-- 标题栏 -->
      <div class="compare-header">
        <div class="header-tabs">
          <button
            class="tab"
            :class="{ active: selectedManager === 'npm' }"
            @click="selectedManager = 'npm'"
          >
            <span class="tab-icon">📦</span>
            npm
          </button>
          <button
            class="tab"
            :class="{ active: selectedManager === 'pnpm' }"
            @click="selectedManager = 'pnpm'"
          >
            <span class="tab-icon">🚀</span>
            pnpm
          </button>
        </div>
      </div>

      <!-- 可视化区域 -->
      <div class="visualization">
        <div class="disk-space">
          <div class="disk-label">磁盘空间使用</div>
          <div class="disk-bar-container">
            <div
              class="disk-bar"
              :class="selectedManager"
              :style="{ width: `${(currentTotal / npmTotalSize) * 100}%` }"
            >
              <span class="disk-value">{{ formatSize(currentTotal) }}</span>
            </div>
          </div>
          <div class="disk-compare">
            <div class="compare-item" :class="{ dim: selectedManager !== 'npm' }">
              <span class="dot npm"></span>
              <span>npm: {{ formatSize(npmTotalSize) }}</span>
            </div>
            <div class="compare-item" :class="{ dim: selectedManager !== 'pnpm' }">
              <span class="dot pnpm"></span>
              <span>pnpm: {{ formatSize(pnpmTotalSize) }}</span>
            </div>
          </div>
        </div>

        <!-- 节省提示 -->
        <div v-if="selectedManager === 'pnpm'" class="savings-banner">
          <span class="savings-icon">🎉</span>
          <span class="savings-text">
            节省了 {{ formatSize(savings.size) }} ({{ savings.percentage }}%)
          </span>
        </div>

        <!-- 项目数量控制 -->
        <div class="project-control">
          <span class="control-label">项目数量</span>
          <div class="control-buttons">
            <button
              class="control-btn"
              :disabled="projectCount <= 1"
              @click="projectCount--"
            >
              −
            </button>
            <span class="control-value">{{ projectCount }}</span>
            <button
              class="control-btn"
              :disabled="projectCount >= 10"
              @click="projectCount++"
            >
              +
            </button>
          </div>
        </div>
      </div>

      <!-- 包列表 -->
      <div class="packages-section">
        <div class="section-title">
          <span>依赖包列表</span>
          <span class="section-subtitle">
            {{ selectedManager === 'pnpm' ? '绿色 = 全局共享' : '每个项目独立复制' }}
          </span>
        </div>
        <div class="packages-grid">
          <div
            v-for="pkg in packages"
            :key="pkg.name"
            class="package-item"
            :class="{ shared: selectedManager === 'pnpm' && pkg.shared }"
          >
            <div class="package-icon">
              {{ pkg.shared ? '📦' : '📋' }}
            </div>
            <div class="package-info">
              <div class="package-name">{{ pkg.name }}</div>
              <div class="package-size">{{ formatSize(pkg.size) }}</div>
            </div>
            <div v-if="selectedManager === 'pnpm' && pkg.shared" class="shared-badge">
              共享
            </div>
          </div>
        </div>
      </div>

      <!-- 原理说明 -->
      <div class="principle-section">
        <div class="principle-title">
          <span>💡</span>
          <span>{{ selectedManager === 'npm' ? 'npm 的工作方式' : 'pnpm 的优化原理' }}</span>
        </div>
        <div class="principle-content">
          <template v-if="selectedManager === 'npm'">
            <p>npm 通过<strong>复制文件</strong>的方式安装依赖。</p>
            <p>每个项目的 <code>node_modules</code> 都是独立的完整副本。</p>
            <p>3 个项目 = 3 份相同的代码，磁盘空间线性增长。</p>
          </template>
          <template v-else>
            <p>pnpm 使用<strong>硬链接 + 符号链接</strong>技术。</p>
            <p>相同的包只在磁盘存一份，通过链接指向共享存储。</p>
            <p>3 个项目 = 1 份共享代码 + 项目特有代码，大幅节省空间。</p>
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pm-compare {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  margin: 20px 0;
}

.compare-window {
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid #e2e8f0;
}

/* Header */
.compare-header {
  background: #f7fafc;
  border-bottom: 1px solid #e2e8f0;
  padding: 4px;
}

.header-tabs {
  display: flex;
  gap: 4px;
}

.tab {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 20px;
  border: none;
  background: transparent;
  color: #718096;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.2s;
}

.tab:hover {
  background: #edf2f7;
  color: #4a5568;
}

.tab.active {
  background: #ffffff;
  color: #2d3748;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.tab-icon {
  font-size: 16px;
}

/* Visualization */
.visualization {
  padding: 24px;
  background: linear-gradient(180deg, #f7fafc 0%, #ffffff 100%);
}

.disk-space {
  margin-bottom: 20px;
}

.disk-label {
  font-size: 12px;
  color: #718096;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.disk-bar-container {
  height: 40px;
  background: #e2e8f0;
  border-radius: 8px;
  overflow: hidden;
  position: relative;
}

.disk-bar {
  height: 100%;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 12px;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.disk-bar.npm {
  background: linear-gradient(90deg, #fc8181 0%, #f56565 100%);
}

.disk-bar.pnpm {
  background: linear-gradient(90deg, #68d391 0%, #48bb78 100%);
}

.disk-value {
  color: white;
  font-weight: 600;
  font-size: 14px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.disk-compare {
  display: flex;
  gap: 20px;
  margin-top: 12px;
}

.compare-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #4a5568;
  transition: opacity 0.2s;
}

.compare-item.dim {
  opacity: 0.5;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.dot.npm { background: #f56565; }
.dot.pnpm { background: #48bb78; }

/* Savings Banner */
.savings-banner {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 16px;
  background: linear-gradient(135deg, #c6f6d5 0%, #9ae6b4 100%);
  border-radius: 8px;
  margin-bottom: 20px;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.savings-icon {
  font-size: 20px;
}

.savings-text {
  color: #22543d;
  font-weight: 600;
  font-size: 14px;
}

/* Project Control */
.project-control {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px;
  background: #edf2f7;
  border-radius: 8px;
}

.control-label {
  font-size: 14px;
  color: #4a5568;
  font-weight: 500;
}

.control-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.control-btn {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  border: 1px solid #cbd5e0;
  background: #ffffff;
  color: #4a5568;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.control-btn:hover:not(:disabled) {
  background: #f7fafc;
  border-color: #a0aec0;
}

.control-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.control-value {
  font-size: 18px;
  font-weight: 600;
  color: #2d3748;
  min-width: 24px;
  text-align: center;
}

/* Packages Section */
.packages-section {
  padding: 20px 24px;
  border-top: 1px solid #e2e8f0;
}

.section-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.section-title span:first-child {
  font-size: 14px;
  font-weight: 600;
  color: #2d3748;
}

.section-subtitle {
  font-size: 12px;
  color: #718096;
}

.packages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 12px;
}

.package-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px;
  background: #f7fafc;
  border-radius: 8px;
  border: 2px solid transparent;
  transition: all 0.2s;
}

.package-item.shared {
  background: #f0fff4;
  border-color: #9ae6b4;
}

.package-icon {
  font-size: 20px;
}

.package-info {
  flex: 1;
}

.package-name {
  font-size: 13px;
  font-weight: 500;
  color: #2d3748;
  font-family: 'SF Mono', Monaco, monospace;
}

.package-size {
  font-size: 11px;
  color: #718096;
}

.shared-badge {
  padding: 2px 6px;
  background: #48bb78;
  color: white;
  font-size: 10px;
  font-weight: 600;
  border-radius: 4px;
}

/* Principle Section */
.principle-section {
  padding: 20px 24px;
  background: #f7fafc;
  border-top: 1px solid #e2e8f0;
}

.principle-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 12px;
}

.principle-content {
  font-size: 13px;
  line-height: 1.8;
  color: #4a5568;
}

.principle-content p {
  margin: 0 0 4px;
}

.principle-content strong {
  color: #2d3748;
}

.principle-content code {
  background: #e2e8f0;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12px;
  font-family: 'SF Mono', Monaco, monospace;
}
</style>
