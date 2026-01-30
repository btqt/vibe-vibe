<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

// 状态管理
const count = ref(0)
const history = ref<{ value: number; timestamp: Date; action: string }[]>([])
const isAnimating = ref(false)
const showHistory = ref(false)
const inputValue = ref('')
const activeTab = ref<'counter' | 'timer' | 'converter'>('counter')

// Timer 状态
const timerValue = ref(0)
const isTimerRunning = ref(false)
let timerInterval: number | null = null

// Converter 状态
const convertInput = ref('')
const convertResult = ref('')

// 计算属性
const stats = computed(() => {
  if (history.value.length === 0) return null
  const values = history.value.map(h => h.value)
  return {
    max: Math.max(...values),
    min: Math.min(...values),
    avg: (values.reduce((a, b) => a + b, 0) / values.length).toFixed(1),
    total: history.value.length
  }
})

const recentHistory = computed(() => {
  return history.value.slice(-5).reverse()
})

// 方法
function addToHistory(action: string) {
  history.value.push({
    value: count.value,
    timestamp: new Date(),
    action
  })
}

function increment() {
  count.value++
  addToHistory('increment')
  triggerAnimation()
}

function decrement() {
  count.value--
  addToHistory('decrement')
  triggerAnimation()
}

function reset() {
  count.value = 0
  addToHistory('reset')
  triggerAnimation()
}

function setValue() {
  const val = parseInt(inputValue.value)
  if (!isNaN(val)) {
    count.value = val
    addToHistory(`set to ${val}`)
    inputValue.value = ''
    triggerAnimation()
  }
}

function triggerAnimation() {
  isAnimating.value = true
  setTimeout(() => isAnimating.value = false, 300)
}

function clearHistory() {
  history.value = []
}

// Timer 功能
function toggleTimer() {
  if (isTimerRunning.value) {
    pauseTimer()
  } else {
    startTimer()
  }
}

function startTimer() {
  isTimerRunning.value = true
  timerInterval = window.setInterval(() => {
    timerValue.value++
  }, 1000)
}

function pauseTimer() {
  isTimerRunning.value = false
  if (timerInterval) {
    clearInterval(timerInterval)
    timerInterval = null
  }
}

function resetTimer() {
  pauseTimer()
  timerValue.value = 0
}

function formatTime(seconds: number): string {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
}

// Converter 功能
function convertNumber() {
  const val = parseInt(convertInput.value)
  if (isNaN(val)) {
    convertResult.value = '请输入有效数字'
    return
  }
  convertResult.value = `二进制: ${val.toString(2)}\n八进制: ${val.toString(8)}\n十六进制: ${val.toString(16).toUpperCase()}`
}

// 键盘快捷键
function handleKeydown(e: KeyboardEvent) {
  if (activeTab.value !== 'counter') return

  switch(e.key) {
    case 'ArrowUp':
      e.preventDefault()
      increment()
      break
    case 'ArrowDown':
      e.preventDefault()
      decrement()
      break
    case 'r':
    case 'R':
      if (!e.ctrlKey && !e.metaKey) {
        reset()
      }
      break
    case 'h':
    case 'H':
      showHistory.value = !showHistory.value
      break
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
  if (timerInterval) clearInterval(timerInterval)
})
</script>

<template>
  <div class="interactive-demo">
    <!-- Tab 切换 -->
    <div class="tab-bar">
      <button
        v-for="tab in ['counter', 'timer', 'converter']"
        :key="tab"
        class="tab-button"
        :class="{ active: activeTab === tab }"
        @click="activeTab = tab as any"
      >
        <span class="tab-icon">
          {{ tab === 'counter' ? '🔢' : tab === 'timer' ? '⏱️' : '🔄' }}
        </span>
        <span class="tab-label">{{ tab === 'counter' ? '计数器' : tab === 'timer' ? '计时器' : '进制转换' }}</span>
      </button>
    </div>

    <!-- Counter 面板 -->
    <div v-if="activeTab === 'counter'" class="panel">
      <div class="counter-display" :class="{ animating: isAnimating }">
        <span class="counter-value">{{ count }}</span>
        <span class="counter-label">当前数值</span>
      </div>

      <div class="counter-controls">
        <button class="control-btn decrement" @click="decrement">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="5" y1="12" x2="19" y2="12"/>
          </svg>
        </button>

        <button class="control-btn reset" @click="reset">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="23 4 23 10 17 10"/>
            <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>
          </svg>
        </button>

        <button class="control-btn increment" @click="increment">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="5" x2="12" y2="19"/>
            <line x1="5" y1="12" x2="19" y2="12"/>
          </svg>
        </button>
      </div>

      <div class="quick-set">
        <input
          v-model="inputValue"
          type="number"
          placeholder="输入数值"
          class="quick-input"
          @keyup.enter="setValue"
        />
        <button class="quick-btn" @click="setValue">设置</button>
      </div>

      <!-- 统计信息 -->
      <div v-if="stats" class="stats-grid">
        <div class="stat-item">
          <span class="stat-value">{{ stats.max }}</span>
          <span class="stat-label">最大值</span>
        </div>
        <div class="stat-item">
          <span class="stat-value">{{ stats.min }}</span>
          <span class="stat-label">最小值</span>
        </div>
        <div class="stat-item">
          <span class="stat-value">{{ stats.avg }}</span>
          <span class="stat-label">平均值</span>
        </div>
        <div class="stat-item">
          <span class="stat-value">{{ stats.total }}</span>
          <span class="stat-label">操作次数</span>
        </div>
      </div>

      <!-- 历史记录 -->
      <div class="history-section">
        <div class="history-header" @click="showHistory = !showHistory">
          <span>操作历史</span>
          <svg
            class="history-arrow"
            :class="{ expanded: showHistory }"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
          >
            <polyline points="6 9 12 15 18 9"/>
          </svg>
        </div>
        <div v-show="showHistory" class="history-list">
          <div
            v-for="(item, index) in recentHistory"
            :key="index"
            class="history-item"
          >
            <span class="history-action">{{ item.action }}</span>
            <span class="history-value" :class="{
              positive: item.value > 0,
              negative: item.value < 0
            }">{{ item.value }}</span>
            <span class="history-time">{{ item.timestamp.toLocaleTimeString() }}</span>
          </div>
          <button v-if="history.length > 0" class="clear-btn" @click="clearHistory">
            清空历史
          </button>
        </div>
      </div>

      <!-- 快捷键提示 -->
      <div class="shortcuts">
        <span class="shortcut"><kbd>↑</kbd> 增加</span>
        <span class="shortcut"><kbd>↓</kbd> 减少</span>
        <span class="shortcut"><kbd>R</kbd> 重置</span>
        <span class="shortcut"><kbd>H</kbd> 历史</span>
      </div>
    </div>

    <!-- Timer 面板 -->
    <div v-if="activeTab === 'timer'" class="panel">
      <div class="timer-display" :class="{ running: isTimerRunning }">
        <span class="timer-value">{{ formatTime(timerValue) }}</span>
      </div>
      <div class="timer-controls">
        <button class="timer-btn" :class="{ active: isTimerRunning }" @click="toggleTimer">
          {{ isTimerRunning ? '⏸️ 暂停' : '▶️ 开始' }}
        </button>
        <button class="timer-btn reset" @click="resetTimer">⏹️ 重置</button>
      </div>
    </div>

    <!-- Converter 面板 -->
    <div v-if="activeTab === 'converter'" class="panel">
      <div class="converter-input-group">
        <input
          v-model="convertInput"
          type="number"
          placeholder="输入十进制数字"
          class="converter-input"
          @keyup.enter="convertNumber"
        />
        <button class="converter-btn" @click="convertNumber">转换</button>
      </div>
      <pre v-if="convertResult" class="converter-result">{{ convertResult }}</pre>
    </div>
  </div>
</template>

<style scoped>
.interactive-demo {
  background: linear-gradient(180deg, #f5f5f7 0%, #e8e8ed 100%);
  border-radius: 20px;
  padding: 24px;
  box-shadow:
    0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif;
}

/* Tab Bar */
.tab-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  background: rgba(0, 0, 0, 0.04);
  padding: 4px;
  border-radius: 12px;
}

.tab-button {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 10px 16px;
  border: none;
  border-radius: 10px;
  background: transparent;
  color: #666;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-button:hover {
  background: rgba(0, 0, 0, 0.04);
}

.tab-button.active {
  background: white;
  color: #007aff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.tab-icon {
  font-size: 16px;
}

/* Panel */
.panel {
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Counter Display */
.counter-display {
  text-align: center;
  padding: 40px 20px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  margin-bottom: 20px;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.counter-display.animating {
  transform: scale(1.02);
}

.counter-value {
  display: block;
  font-size: 72px;
  font-weight: 200;
  background: linear-gradient(135deg, #007aff 0%, #5856d6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1;
  letter-spacing: -2px;
}

.counter-label {
  display: block;
  font-size: 13px;
  color: #86868b;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 8px;
}

/* Controls */
.counter-controls {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-bottom: 20px;
}

.control-btn {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.control-btn svg {
  width: 24px;
  height: 24px;
}

.control-btn.increment {
  background: linear-gradient(135deg, #34c759 0%, #30b350 100%);
  color: white;
}

.control-btn.decrement {
  background: linear-gradient(135deg, #ff3b30 0%, #e6352b 100%);
  color: white;
}

.control-btn.reset {
  background: white;
  color: #666;
}

.control-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.control-btn:active {
  transform: scale(0.95);
}

/* Quick Set */
.quick-set {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
}

.quick-input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid #d1d1d6;
  border-radius: 10px;
  font-size: 16px;
  background: white;
  outline: none;
  transition: all 0.2s;
}

.quick-input:focus {
  border-color: #007aff;
  box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.1);
}

.quick-btn {
  padding: 12px 20px;
  background: #007aff;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.quick-btn:hover {
  background: #0056b3;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 20px;
}

.stat-item {
  background: white;
  padding: 16px 8px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.stat-value {
  display: block;
  font-size: 24px;
  font-weight: 600;
  color: #1d1d1f;
}

.stat-label {
  display: block;
  font-size: 11px;
  color: #86868b;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 4px;
}

/* History */
.history-section {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  margin-bottom: 16px;
}

.history-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  color: #1d1d1f;
  user-select: none;
}

.history-header:hover {
  background: rgba(0, 0, 0, 0.02);
}

.history-arrow {
  width: 16px;
  height: 16px;
  transition: transform 0.2s;
}

.history-arrow.expanded {
  transform: rotate(180deg);
}

.history-list {
  padding: 0 16px 16px;
}

.history-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #f0f0f0;
  font-size: 13px;
}

.history-item:last-child {
  border-bottom: none;
}

.history-action {
  color: #86868b;
  text-transform: capitalize;
}

.history-value {
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.history-value.positive {
  color: #34c759;
}

.history-value.negative {
  color: #ff3b30;
}

.history-time {
  color: #c7c7cc;
  font-size: 12px;
}

.clear-btn {
  width: 100%;
  padding: 10px;
  margin-top: 12px;
  background: #f2f2f7;
  border: none;
  border-radius: 8px;
  color: #ff3b30;
  font-size: 13px;
  cursor: pointer;
  transition: background 0.2s;
}

.clear-btn:hover {
  background: #e5e5ea;
}

/* Shortcuts */
.shortcuts {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

.shortcut {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #86868b;
}

kbd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 24px;
  padding: 4px 8px;
  background: white;
  border: 1px solid #d1d1d6;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 600;
  color: #1d1d1f;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
}

/* Timer Panel */
.timer-display {
  text-align: center;
  padding: 60px 20px;
  background: white;
  border-radius: 16px;
  margin-bottom: 20px;
}

.timer-display.running .timer-value {
  color: #34c759;
}

.timer-value {
  font-size: 64px;
  font-weight: 200;
  font-variant-numeric: tabular-nums;
  color: #1d1d1f;
  letter-spacing: 4px;
}

.timer-controls {
  display: flex;
  justify-content: center;
  gap: 16px;
}

.timer-btn {
  padding: 14px 32px;
  border-radius: 12px;
  border: none;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.timer-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

.timer-btn.active {
  background: #34c759;
  color: white;
}

/* Converter Panel */
.converter-input-group {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
}

.converter-input {
  flex: 1;
  padding: 16px;
  border: 1px solid #d1d1d6;
  border-radius: 12px;
  font-size: 18px;
  background: white;
  outline: none;
}

.converter-input:focus {
  border-color: #007aff;
}

.converter-btn {
  padding: 16px 28px;
  background: #007aff;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
}

.converter-result {
  background: #1d1d1f;
  color: #30d158;
  padding: 20px;
  border-radius: 12px;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 14px;
  line-height: 1.8;
  white-space: pre-wrap;
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .interactive-demo {
    background: linear-gradient(180deg, #1c1c1e 0%, #2c2c2e 100%);
  }

  .tab-button {
    color: #999;
  }

  .tab-button.active {
    background: #3a3a3c;
    color: #0a84ff;
  }

  .counter-display,
  .stat-item,
  .history-section,
  .timer-display {
    background: #2c2c2e;
  }

  .counter-value {
    background: linear-gradient(135deg, #0a84ff 0%, #5e5ce6 100%);
    -webkit-background-clip: text;
  }

  .counter-label,
  .stat-label,
  .shortcut,
  .history-action,
  .history-time {
    color: #8e8e93;
  }

  .stat-value,
  .timer-value,
  .history-header {
    color: #f5f5f7;
  }

  .quick-input,
  .converter-input {
    background: #3a3a3c;
    border-color: #48484a;
    color: #f5f5f7;
  }

  kbd {
    background: #3a3a3c;
    border-color: #48484a;
    color: #f5f5f7;
  }

  .history-item {
    border-color: #3a3a3c;
  }

  .clear-btn {
    background: #3a3a3c;
    color: #ff453a;
  }

  .timer-btn {
    background: #2c2c2e;
    color: #f5f5f7;
  }
}
</style>
