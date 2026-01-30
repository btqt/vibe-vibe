<script setup lang="ts">
import { ref, computed, onUnmounted } from 'vue'

type AnimationPhase = 'idle' | 'typing' | 'request' | 'processing' | 'response' | 'rendering' | 'complete'

const animationPhase = ref<AnimationPhase>('idle')
const selectedSide = ref<'none' | 'browser' | 'server'>('none')
const isPlaying = ref(false)
const typedUrl = ref('')
const targetUrl = 'example.com'
const packetPosition = ref(0)
const showResponse = ref(false)

let animationTimer: number | null = null
let packetInterval: number | null = null

const browserCapabilities = [
  { icon: '🎨', title: '渲染页面', desc: 'HTML/CSS/JS 解析与渲染' },
  { icon: '🖱️', title: '用户交互', desc: '点击、输入、滚动等事件处理' },
  { icon: '💾', title: '本地存储', desc: 'LocalStorage, IndexedDB, Cookies' },
  { icon: '📡', title: '发送请求', desc: 'HTTP/HTTPS 请求到服务器' },
  { icon: '🔒', title: '安全限制', desc: 'CORS, CSP, 同源策略' },
  { icon: '🌐', title: '缓存资源', desc: '浏览器缓存、Service Worker' }
]

const serverCapabilities = [
  { icon: '⚙️', title: '处理请求', desc: '路由解析、参数验证' },
  { icon: '💽', title: '数据操作', desc: '数据库查询、文件读写' },
  { icon: '🔐', title: '身份验证', desc: 'Session、JWT、OAuth' },
  { icon: '📊', title: '业务逻辑', desc: '计算、数据处理、API 响应' },
  { icon: '🚀', title: '生成页面', desc: 'SSR、模板渲染、JSON 数据' },
  { icon: '🛡️', title: '安全防护', desc: 'SQL注入防护、XSS过滤' }
]

const comparisonData = [
  { aspect: '运行位置', browser: '用户设备（手机/电脑）', server: '远程数据中心' },
  { aspect: '代码可见性', browser: '源代码可见（HTML/JS/CSS）', server: '仅返回结果' },
  { aspect: '数据持久化', browser: '有限（本地存储）', server: '完整（数据库/文件系统）' },
  { aspect: '计算能力', browser: '受设备性能限制', server: '可扩展的强大算力' },
  { aspect: '网络访问', browser: '受限（CORS策略）', server: '自由（可访问任意服务）' },
  { aspect: '安全密钥', browser: '❌ 不能存储', server: '✅ 安全存储' }
]

const isAnimating = computed(() => animationPhase.value !== 'idle' && animationPhase.value !== 'complete')
const currentPhaseText = computed(() => {
  const texts: Record<AnimationPhase, string> = {
    idle: '点击播放开始演示',
    typing: '👤 用户在地址栏输入 URL...',
    request: '📤 浏览器发送 HTTP 请求...',
    processing: '⚙️ 服务器处理请求...',
    response: '📥 服务器返回响应数据...',
    rendering: '🎨 浏览器渲染页面...',
    complete: '✅ 页面加载完成！'
  }
  return texts[animationPhase.value]
})

function startAnimation() {
  if (isAnimating.value) return
  resetAnimation()
  isPlaying.value = true
  animationPhase.value = 'typing'

  let charIndex = 0
  typedUrl.value = ''

  const typeInterval = window.setInterval(() => {
    if (charIndex < targetUrl.length) {
      typedUrl.value += targetUrl[charIndex]
      charIndex++
    } else {
      clearInterval(typeInterval)
      setTimeout(() => {
        animationPhase.value = 'request'
        animatePacket('request')
      }, 500)
    }
  }, 150)
}

function animatePacket(direction: 'request' | 'response') {
  packetPosition.value = 0
  let progress = 0

  packetInterval = window.setInterval(() => {
    progress += 2
    packetPosition.value = progress

    if (progress >= 100) {
      if (packetInterval) clearInterval(packetInterval)

      if (direction === 'request') {
        animationPhase.value = 'processing'
        animationTimer = window.setTimeout(() => {
          animationPhase.value = 'response'
          animatePacket('response')
        }, 1500)
      } else {
        animationPhase.value = 'rendering'
        showResponse.value = true
        animationTimer = window.setTimeout(() => {
          animationPhase.value = 'complete'
          isPlaying.value = false
        }, 1000)
      }
    }
  }, 20)
}

function resetAnimation() {
  if (animationTimer) clearTimeout(animationTimer)
  if (packetInterval) clearInterval(packetInterval)
  animationPhase.value = 'idle'
  typedUrl.value = ''
  packetPosition.value = 0
  showResponse.value = false
  isPlaying.value = false
}

function selectSide(side: 'browser' | 'server') {
  selectedSide.value = selectedSide.value === side ? 'none' : side
}

function getPacketStyle() {
  const isRequest = animationPhase.value === 'request'
  const startX = isRequest ? 20 : 80
  const endX = isRequest ? 80 : 20
  const currentX = startX + (endX - startX) * (packetPosition.value / 100)

  return {
    left: `${currentX}%`,
    opacity: animationPhase.value === 'request' || animationPhase.value === 'response' ? 1 : 0
  }
}

onUnmounted(() => {
  resetAnimation()
})
</script>

<template>
  <div class="browser-server-flow">
    <div class="flow-header">
      <div class="phase-indicator" :class="animationPhase">
        <span class="phase-text">{{ currentPhaseText }}</span>
      </div>
      <button
        class="play-button"
        :class="{ playing: isAnimating }"
        @click="startAnimation"
        :disabled="isAnimating"
      >
        <svg v-if="!isAnimating" viewBox="0 0 24 24" fill="currentColor">
          <path d="M8 5v14l11-7z"/>
        </svg>
        <svg v-else viewBox="0 0 24 24" fill="currentColor">
          <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
        </svg>
        <span>{{ isAnimating ? '演示中...' : '播放演示' }}</span>
      </button>
    </div>

    <div class="flow-visualization">
      <div
        class="side-container browser-side"
        :class="{ selected: selectedSide === 'browser', active: animationPhase === 'typing' || animationPhase === 'rendering' }"
        @click="selectSide('browser')"
      >
        <div class="device-header">
          <div class="device-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="2" y="3" width="20" height="14" rx="2"/>
              <line x1="8" y1="21" x2="16" y2="21"/>
              <line x1="12" y1="17" x2="12" y2="21"/>
            </svg>
          </div>
          <span class="device-label">客户端 (浏览器)</span>
          <span class="click-hint">点击查看能力</span>
        </div>

        <div class="browser-window">
          <div class="browser-toolbar">
            <div class="browser-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
            <div class="address-bar" :class="{ active: animationPhase === 'typing' }">
              <span class="protocol">https://</span>
              <span class="url-text">{{ typedUrl }}</span>
              <span v-if="animationPhase === 'typing'" class="cursor">|</span>
            </div>
          </div>
          <div class="browser-content" :class="{ loaded: showResponse }">
            <div v-if="!showResponse" class="empty-state">
              <span class="empty-icon">🌐</span>
              <span>等待加载...</span>
            </div>
            <div v-else class="loaded-content">
              <div class="content-header"></div>
              <div class="content-lines">
                <div class="line"></div>
                <div class="line short"></div>
                <div class="line"></div>
              </div>
              <div class="content-image"></div>
            </div>
          </div>
        </div>
      </div>

      <div class="connection-area">
        <div class="connection-line">
          <div
            class="packet"
            :style="getPacketStyle()"
            :class="{ request: animationPhase === 'request', response: animationPhase === 'response' }"
          >
            <span class="packet-icon">
              {{ animationPhase === 'request' ? '📤' : '📥' }}
            </span>
          </div>
        </div>
        <div class="protocol-labels">
          <span class="protocol">HTTP/HTTPS</span>
        </div>
      </div>

      <div
        class="side-container server-side"
        :class="{ selected: selectedSide === 'server', active: animationPhase === 'processing' }"
        @click="selectSide('server')"
      >
        <div class="device-header">
          <div class="device-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="2" y="2" width="20" height="8" rx="2"/>
              <rect x="2" y="14" width="20" height="8" rx="2"/>
              <line x1="6" y1="6" x2="6.01" y2="6"/>
              <line x1="6" y1="18" x2="6.01" y2="18"/>
            </svg>
          </div>
          <span class="device-label">服务端 (服务器)</span>
          <span class="click-hint">点击查看能力</span>
        </div>

        <div class="server-rack">
          <div class="server-unit" :class="{ processing: animationPhase === 'processing' }">
            <div class="server-lights">
              <span class="light green"></span>
              <span class="light yellow"></span>
              <span class="light" :class="{ red: animationPhase === 'processing' }"></span>
            </div>
            <div class="server-info">
              <span class="server-name">Web Server</span>
              <span v-if="animationPhase === 'processing'" class="processing-text">处理中...</span>
            </div>
          </div>
          <div class="server-unit secondary">
            <div class="server-lights">
              <span class="light green"></span>
              <span class="light"></span>
              <span class="light"></span>
            </div>
            <div class="server-info">
              <span class="server-name">Database</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="selectedSide !== 'none'" class="capability-panel" :class="selectedSide">
      <div class="panel-header">
        <span class="panel-title">
          {{ selectedSide === 'browser' ? '🖥️ 浏览器能力' : '⚙️ 服务器能力' }}
        </span>
        <button class="close-btn" @click="selectedSide = 'none'">✕</button>
      </div>
      <div class="capability-grid">
        <div
          v-for="(cap, index) in selectedSide === 'browser' ? browserCapabilities : serverCapabilities"
          :key="index"
          class="capability-item"
          :style="{ animationDelay: `${index * 50}ms` }"
        >
          <span class="cap-icon">{{ cap.icon }}</span>
          <div class="cap-info">
            <span class="cap-title">{{ cap.title }}</span>
            <span class="cap-desc">{{ cap.desc }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="comparison-section">
      <h4 class="section-title">📊 客户端 vs 服务端对比</h4>
      <div class="comparison-table-wrapper">
        <table class="comparison-table">
          <thead>
            <tr>
              <th class="aspect-col">对比维度</th>
              <th class="browser-col">浏览器 (Client)</th>
              <th class="server-col">服务器 (Server)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(row, index) in comparisonData" :key="index">
              <td class="aspect-cell">{{ row.aspect }}</td>
              <td class="browser-cell">{{ row.browser }}</td>
              <td class="server-cell">{{ row.server }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<style scoped>
.browser-server-flow {
  background: linear-gradient(180deg, #f5f5f7 0%, #e8e8ed 100%);
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.8);
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif;
}

.flow-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 12px;
}

.phase-indicator {
  flex: 1;
  min-width: 200px;
  padding: 12px 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  transition: all 0.3s ease;
}

.phase-indicator.typing { border-left: 4px solid #007aff; }
.phase-indicator.request { border-left: 4px solid #ff9500; }
.phase-indicator.processing { border-left: 4px solid #5856d6; }
.phase-indicator.response { border-left: 4px solid #34c759; }
.phase-indicator.rendering { border-left: 4px solid #af52de; }
.phase-indicator.complete { border-left: 4px solid #34c759; background: #f0fff4; }

.phase-text {
  font-size: 14px;
  font-weight: 500;
  color: #1d1d1f;
}

.play-button {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  background: linear-gradient(135deg, #007aff 0%, #5856d6 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 122, 255, 0.3);
}

.play-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 122, 255, 0.4);
}

.play-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.play-button svg {
  width: 20px;
  height: 20px;
}

.flow-visualization {
  display: flex;
  align-items: stretch;
  gap: 16px;
  margin-bottom: 24px;
  min-height: 320px;
}

.side-container {
  flex: 1;
  min-width: 200px;
  background: white;
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.side-container:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.side-container.selected {
  border-color: #007aff;
  box-shadow: 0 0 0 4px rgba(0, 122, 255, 0.1);
}

.browser-side.active {
  border-color: #007aff;
  animation: pulse-blue 2s infinite;
}

.server-side.active {
  border-color: #5856d6;
  animation: pulse-purple 2s infinite;
}

@keyframes pulse-blue {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0, 122, 255, 0.4); }
  50% { box-shadow: 0 0 0 8px rgba(0, 122, 255, 0); }
}

@keyframes pulse-purple {
  0%, 100% { box-shadow: 0 0 0 0 rgba(88, 86, 214, 0.4); }
  50% { box-shadow: 0 0 0 8px rgba(88, 86, 214, 0); }
}

.device-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
}

.device-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #f5f5f7 0%, #e8e8ed 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #007aff;
}

.device-icon svg {
  width: 24px;
  height: 24px;
}

.server-side .device-icon {
  color: #5856d6;
}

.device-label {
  font-size: 15px;
  font-weight: 600;
  color: #1d1d1f;
}

.click-hint {
  margin-left: auto;
  font-size: 11px;
  color: #86868b;
  background: #f5f5f7;
  padding: 4px 8px;
  border-radius: 6px;
}

.browser-window {
  border: 1px solid #d1d1d6;
  border-radius: 10px;
  overflow: hidden;
  background: #f5f5f7;
}

.browser-toolbar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  background: #e8e8ed;
  border-bottom: 1px solid #d1d1d6;
}

.browser-dots {
  display: flex;
  gap: 6px;
}

.browser-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #c7c7cc;
}

.browser-dots span:nth-child(1) { background: #ff5f56; }
.browser-dots span:nth-child(2) { background: #ffbd2e; }
.browser-dots span:nth-child(3) { background: #27c93f; }

.address-bar {
  flex: 1;
  padding: 6px 12px;
  background: white;
  border-radius: 6px;
  font-size: 12px;
  font-family: 'SF Mono', Monaco, monospace;
  color: #1d1d1f;
  display: flex;
  align-items: center;
}

.address-bar.active {
  box-shadow: 0 0 0 2px #007aff;
}

.protocol {
  color: #34c759;
}

.url-text {
  color: #1d1d1f;
}

.cursor {
  color: #007aff;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

.browser-content {
  height: 140px;
  padding: 16px;
  background: white;
}

.empty-state {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #86868b;
  font-size: 13px;
  gap: 8px;
}

.empty-icon {
  font-size: 32px;
}

.loaded-content {
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.content-header {
  height: 20px;
  background: linear-gradient(90deg, #007aff 0%, #5856d6 100%);
  border-radius: 4px;
  margin-bottom: 12px;
}

.content-lines {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 12px;
}

.line {
  height: 8px;
  background: #e8e8ed;
  border-radius: 4px;
}

.line.short {
  width: 60%;
}

.content-image {
  height: 50px;
  background: linear-gradient(135deg, #f5f5f7 0%, #e8e8ed 100%);
  border-radius: 6px;
}

.connection-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-width: 80px;
  position: relative;
}

.connection-line {
  width: 2px;
  height: 200px;
  background: linear-gradient(180deg, #d1d1d6 0%, #c7c7cc 100%);
  position: relative;
}

.packet {
  position: absolute;
  width: 40px;
  height: 40px;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  transform: translateX(-50%);
  transition: opacity 0.2s;
  top: 50%;
  margin-top: -20px;
}

.packet-icon {
  font-size: 18px;
}

.protocol-labels {
  margin-top: 12px;
  font-size: 11px;
  color: #86868b;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.server-rack {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.server-unit {
  background: #1d1d1f;
  border-radius: 8px;
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 12px;
}

.server-unit.secondary {
  opacity: 0.6;
}

.server-lights {
  display: flex;
  gap: 6px;
}

.light {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #3a3a3c;
}

.light.green { background: #34c759; box-shadow: 0 0 4px #34c759; }
.light.yellow { background: #ff9500; box-shadow: 0 0 4px #ff9500; }
.light.red { background: #ff3b30; box-shadow: 0 0 4px #ff3b30; animation: blink 0.5s infinite; }

.server-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.server-name {
  color: white;
  font-size: 13px;
  font-weight: 600;
}

.processing-text {
  color: #ff9500;
  font-size: 11px;
  animation: pulse 1s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.capability-panel {
  background: white;
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.panel-title {
  font-size: 16px;
  font-weight: 600;
  color: #1d1d1f;
}

.close-btn {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: none;
  background: #f5f5f7;
  color: #86868b;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.close-btn:hover {
  background: #e8e8ed;
  color: #1d1d1f;
}

.capability-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px;
}

.capability-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: #f5f5f7;
  border-radius: 10px;
  animation: fadeIn 0.3s ease backwards;
}

.cap-icon {
  font-size: 24px;
}

.cap-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.cap-title {
  font-size: 13px;
  font-weight: 600;
  color: #1d1d1f;
}

.cap-desc {
  font-size: 11px;
  color: #86868b;
}

.comparison-section {
  background: white;
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.section-title {
  margin: 0 0 16px 0;
  font-size: 15px;
  font-weight: 600;
  color: #1d1d1f;
}

.comparison-table-wrapper {
  overflow-x: auto;
}

.comparison-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}

.comparison-table th {
  text-align: left;
  padding: 12px;
  background: #f5f5f7;
  font-weight: 600;
  color: #1d1d1f;
  border-bottom: 1px solid #e8e8ed;
}

.comparison-table td {
  padding: 12px;
  border-bottom: 1px solid #f5f5f7;
  color: #3a3a3c;
}

.aspect-col { width: 20%; }
.browser-col { width: 40%; color: #007aff !important; }
.server-col { width: 40%; color: #5856d6 !important; }

.aspect-cell {
  font-weight: 500;
  color: #1d1d1f;
}

.comparison-table tr:hover td {
  background: #fafafa;
}

@media (prefers-color-scheme: dark) {
  .browser-server-flow {
    background: linear-gradient(180deg, #1c1c1e 0%, #2c2c2e 100%);
  }

  .phase-indicator,
  .side-container,
  .capability-panel,
  .comparison-section {
    background: #2c2c2e;
  }

  .phase-text,
  .device-label,
  .panel-title,
  .section-title,
  .aspect-cell {
    color: #f5f5f7;
  }

  .click-hint {
    background: #3a3a3c;
    color: #8e8e93;
  }

  .device-icon {
    background: #3a3a3c;
  }

  .browser-side .device-icon {
    color: #0a84ff;
  }

  .server-side .device-icon {
    color: #5e5ce6;
  }

  .address-bar {
    background: #1c1c1e;
    color: #f5f5f7;
  }

  .url-text {
    color: #f5f5f7;
  }

  .browser-content {
    background: #1c1c1e;
  }

  .empty-state {
    color: #8e8e93;
  }

  .line {
    background: #3a3a3c;
  }

  .capability-item {
    background: #3a3a3c;
  }

  .cap-title {
    color: #f5f5f7;
  }

  .cap-desc {
    color: #8e8e93;
  }

  .comparison-table th {
    background: #3a3a3c;
    color: #f5f5f7;
    border-bottom-color: #48484a;
  }

  .comparison-table td {
    border-bottom-color: #3a3a3c;
    color: #aeaeb2;
  }

  .comparison-table tr:hover td {
    background: #3a3a3c;
  }

  .close-btn {
    background: #3a3a3c;
    color: #8e8e93;
  }

  .close-btn:hover {
    background: #48484a;
    color: #f5f5f7;
  }

  .phase-indicator.complete {
    background: #1c3a1c;
  }
}

@media (max-width: 640px) {
  .browser-server-flow {
    padding: 16px;
  }

  .flow-header {
    flex-direction: column;
    align-items: stretch;
  }

  .phase-indicator {
    min-width: auto;
  }

  .flow-visualization {
    flex-direction: column;
    min-height: auto;
  }

  .connection-area {
    height: 60px;
    flex-direction: row;
  }

  .connection-line {
    width: 100%;
    height: 2px;
  }

  .packet {
    top: 50% !important;
    left: auto !important;
    transform: translateY(-50%);
  }

  .capability-grid {
    grid-template-columns: 1fr;
  }

  .comparison-table {
    font-size: 11px;
  }

  .comparison-table th,
  .comparison-table td {
    padding: 8px;
  }
}
</style>