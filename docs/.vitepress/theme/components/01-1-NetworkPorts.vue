<script setup lang="ts">
import { ref, computed } from 'vue'

interface Port {
  number: number
  status: 'available' | 'occupied' | 'selected'
  service?: string
  icon?: string
}

const ports = ref<Port[]>([
  { number: 3000, status: 'occupied', service: 'Next.js 项目 A', icon: '⚛️' },
  { number: 3001, status: 'occupied', service: 'Next.js 项目 B', icon: '⚛️' },
  { number: 3002, status: 'available' },
  { number: 3003, status: 'available' },
  { number: 3004, status: 'available' },
  { number: 3005, status: 'available' },
  { number: 5173, status: 'occupied', service: 'Vite 项目', icon: '⚡' },
  { number: 5174, status: 'available' },
  { number: 8080, status: 'occupied', service: '静态服务器', icon: '📁' },
  { number: 8081, status: 'available' },
])

const selectedPort = ref<number | null>(null)
const showConnection = ref(false)
const connectionStatus = ref<'idle' | 'connecting' | 'connected' | 'error'>('idle')

const localhost = '127.0.0.1'

function selectPort(port: Port) {
  if (port.status === 'occupied') {
    connectionStatus.value = 'error'
    setTimeout(() => connectionStatus.value = 'idle', 1500)
    return
  }

  selectedPort.value = port.number
  connectionStatus.value = 'idle'

  // 重置其他选中状态
  ports.value = ports.value.map(p => ({
    ...p,
    status: p.number === port.number ? 'selected' : p.status === 'selected' ? 'available' : p.status
  }))
}

function connect() {
  if (!selectedPort.value) return

  connectionStatus.value = 'connecting'
  showConnection.value = true

  setTimeout(() => {
    connectionStatus.value = 'connected'
  }, 1000)
}

function reset() {
  selectedPort.value = null
  showConnection.value = false
  connectionStatus.value = 'idle'
  ports.value = ports.value.map(p => ({
    ...p,
    status: p.status === 'selected' ? 'available' : p.status
  }))
}

function getPortClass(port: Port): string {
  switch (port.status) {
    case 'occupied': return 'occupied'
    case 'selected': return 'selected'
    default: return 'available'
  }
}

const connectionUrl = computed(() => {
  if (!selectedPort.value) return ''
  return `http://localhost:${selectedPort.value}`
})
</script>

<template>
  <div class="network-ports">
    <div class="ports-window">
      <!-- 标题栏 -->
      <div class="ports-header">
        <div class="window-controls">
          <span class="control close"></span>
          <span class="control minimize"></span>
          <span class="control maximize"></span>
        </div>
        <div class="ports-title">
          <svg class="ports-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="3"/>
            <path d="M12 1v6m0 6v6m4.22-10.22l4.24-4.24M6.34 17.66l-4.24 4.24M23 12h-6m-6 0H1m20.24 4.24l-4.24-4.24M6.34 6.34L2.1 2.1"/>
          </svg>
          Localhost 端口可视化
        </div>
        <div class="ports-actions">
          <button class="action-btn" @click="reset" title="重置">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="23 4 23 10 17 10"/>
              <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- 主要内容 -->
      <div class="ports-content">
        <!-- 电脑可视化 -->
        <div class="computer-section">
          <div class="computer-visual">
            <div class="laptop">
              <div class="laptop-screen">
                <div class="screen-content">
                  <div class="browser-bar">
                    <div class="browser-dots">
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                    <div class="browser-address">
                      <span v-if="connectionStatus === 'connected'" class="url-success">
                        {{ connectionUrl }}
                      </span>
                      <span v-else class="url-placeholder">
                        http://localhost:{{ selectedPort || '????' }}
                      </span>
                    </div>
                  </div>
                  <div class="browser-body">
                    <div v-if="connectionStatus === 'connected'" class="success-page">
                      <div class="success-icon">🎉</div>
                      <div class="success-text">连接成功！</div>
                      <div class="success-sub">你的应用正在运行</div>
                    </div>
                    <div v-else-if="connectionStatus === 'error'" class="error-page">
                      <div class="error-icon">❌</div>
                      <div class="error-text">端口被占用</div>
                      <div class="error-sub">EADDRINUSE: Address already in use</div>
                    </div>
                    <div v-else-if="connectionStatus === 'connecting'" class="loading-page">
                      <div class="loading-spinner"></div>
                      <div class="loading-text">连接中...</div>
                    </div>
                    <div v-else class="empty-page">
                      <div class="empty-icon">🌐</div>
                      <div class="empty-text">选择一个端口并连接</div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="laptop-base">
                <div class="laptop-keyboard"></div>
              </div>
            </div>
          </div>

          <!-- 连接可视化 -->
          <div v-if="showConnection" class="connection-visual">
            <div class="connection-line" :class="connectionStatus">
              <div class="connection-packets">
                <span class="packet"></span>
                <span class="packet"></span>
                <span class="packet"></span>
              </div>
            </div>
          </div>

          <!-- 本地主机信息 -->
          <div class="localhost-info">
            <div class="info-card">
              <div class="info-label">Localhost IP</div>
              <div class="info-value ip">{{ localhost }}</div>
              <div class="info-desc">代表"你自己的电脑"</div>
            </div>
            <div v-if="selectedPort" class="info-card selected">
              <div class="info-label">选中端口</div>
              <div class="info-value port">{{ selectedPort }}</div>
              <div class="info-desc">应用运行的"房间号"</div>
            </div>
          </div>
        </div>

        <!-- 端口网格 -->
        <div class="ports-section">
          <div class="section-header">
            <span class="section-title">可用端口</span>
            <div class="legend">
              <span class="legend-item">
                <span class="dot available"></span>
                可用
              </span>
              <span class="legend-item">
                <span class="dot occupied"></span>
                占用
              </span>
              <span class="legend-item">
                <span class="dot selected"></span>
                选中
              </span>
            </div>
          </div>

          <div class="ports-grid">
            <div
              v-for="port in ports"
              :key="port.number"
              class="port-item"
              :class="getPortClass(port)"
              @click="selectPort(port)"
            >
              <div class="port-number">{{ port.number }}</div>
              <div v-if="port.service" class="port-service">
                <span class="service-icon">{{ port.icon }}</span>
                <span class="service-name">{{ port.service }}</span>
              </div>
              <div v-else class="port-status">
                {{ port.status === 'selected' ? '已选择' : '可用' }}
              </div>
            </div>
          </div>
        </div>

        <!-- 连接按钮 -->
        <div class="action-section">
          <div class="action-wrapper">
            <button
              class="connect-btn"
              :class="{ disabled: !selectedPort, connected: connectionStatus === 'connected' }"
              :disabled="!selectedPort || connectionStatus === 'connected'"
              @click="connect"
            >
              <span v-if="connectionStatus === 'connected'" class="btn-icon">✓</span>
              <span v-else class="btn-icon">🔗</span>
              {{ connectionStatus === 'connected' ? '已连接' : '连接' }}
            </button>
            <div class="action-hint">
              <span class="hint-icon">💡</span>
              <span>运行 <code>pnpm dev</code> 时，可指定端口如 <code>--port 3002</code></span>
            </div>
          </div>
        </div>
      </div>

      <!-- 底部说明 -->
      <div class="ports-footer">
        <div class="footer-tip">
          <span class="tip-icon">💡</span>
          <span>一个端口同时只能容纳一个程序。如果看到 <code>EADDRINUSE</code> 错误，说明端口被占用了。</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.network-ports {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  margin: 20px 0;
}

.ports-window {
  background: #1e1e2e;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

/* Header */
.ports-header {
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

.ports-title {
  flex: 1;
  text-align: center;
  color: #a0a0b0;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.ports-icon {
  width: 16px;
  height: 16px;
  color: #63b3ed;
}

.ports-actions {
  display: flex;
  gap: 8px;
}

.action-btn {
  background: transparent;
  border: none;
  color: #888;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  transition: all 0.2s;
}

.action-btn:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.1);
}

.action-btn svg {
  width: 14px;
  height: 14px;
}

/* Content */
.ports-content {
  padding: 24px;
}

/* Computer Section */
.computer-section {
  display: flex;
  gap: 24px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.computer-visual {
  flex: 2;
  min-width: 280px;
}

.laptop {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.laptop-screen {
  width: 100%;
  max-width: 360px;
  aspect-ratio: 16/10;
  background: #0d0d15;
  border-radius: 12px 12px 0 0;
  padding: 8px 8px 0;
  box-shadow: 0 0 0 2px #3d3d5c, 0 10px 40px rgba(0, 0, 0, 0.5);
}

.screen-content {
  width: 100%;
  height: 100%;
  background: #16162a;
  border-radius: 4px 4px 0 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.browser-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: #252542;
  border-bottom: 1px solid #2d2d4a;
}

.browser-dots {
  display: flex;
  gap: 4px;
}

.browser-dots span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4a5568;
}

.browser-address {
  flex: 1;
  padding: 4px 10px;
  background: #1e1e2e;
  border-radius: 4px;
  font-size: 11px;
  font-family: 'SF Mono', Monaco, monospace;
}

.url-placeholder {
  color: #718096;
}

.url-success {
  color: #68d391;
}

.browser-body {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.empty-page, .success-page, .error-page, .loading-page {
  text-align: center;
  padding: 20px;
}

.empty-icon, .success-icon, .error-icon {
  font-size: 40px;
  margin-bottom: 8px;
}

.empty-text, .success-text, .error-text {
  font-size: 14px;
  font-weight: 600;
}

.empty-text { color: #718096; }
.success-text { color: #68d391; }
.error-text { color: #fc8181; }

.success-sub, .error-sub {
  font-size: 11px;
  color: #a0aec0;
  margin-top: 4px;
}

.loading-spinner {
  width: 32px;
  height: 32px;
  border: 3px solid #2d3748;
  border-top-color: #63b3ed;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 8px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.laptop-base {
  width: 120%;
  height: 12px;
  background: linear-gradient(180deg, #3d3d5c 0%, #2d2d44 100%);
  border-radius: 0 0 8px 8px;
  position: relative;
}

.laptop-keyboard {
  position: absolute;
  top: 2px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 4px;
  background: #4a4a6a;
  border-radius: 0 0 4px 4px;
}

/* Connection Visual */
.connection-visual {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 60px;
}

.connection-line {
  width: 2px;
  height: 100px;
  background: #2d3748;
  position: relative;
}

.connection-line.connecting,
.connection-line.connected {
  background: linear-gradient(180deg, #63b3ed 0%, #68d391 100%);
}

.connection-packets {
  position: absolute;
  inset: 0;
}

.packet {
  position: absolute;
  width: 6px;
  height: 6px;
  background: #63b3ed;
  border-radius: 50%;
  opacity: 0;
  animation: packetMove 1.5s infinite;
}

.packet:nth-child(1) { animation-delay: 0s; }
.packet:nth-child(2) { animation-delay: 0.5s; }
.packet:nth-child(3) { animation-delay: 1s; }

@keyframes packetMove {
  0% {
    top: 0;
    opacity: 1;
  }
  100% {
    top: 100%;
    opacity: 0;
  }
}

/* Localhost Info */
.localhost-info {
  flex: 1;
  min-width: 140px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.info-card {
  padding: 16px;
  background: #252542;
  border-radius: 8px;
  border: 1px solid #2d2d4a;
}

.info-card.selected {
  border-color: #63b3ed;
  background: linear-gradient(135deg, #252542 0%, #1a365d 100%);
}

.info-label {
  font-size: 11px;
  color: #718096;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.info-value {
  font-size: 20px;
  font-weight: 600;
  font-family: 'SF Mono', Monaco, monospace;
}

.info-value.ip {
  color: #63b3ed;
}

.info-value.port {
  color: #68d391;
}

.info-desc {
  font-size: 11px;
  color: #a0aec0;
  margin-top: 4px;
}

/* Ports Section */
.ports-section {
  margin-bottom: 20px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.section-title {
  font-size: 13px;
  font-weight: 600;
  color: #e2e8f0;
}

.legend {
  display: flex;
  gap: 16px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  color: #a0aec0;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.dot.available { background: #68d391; }
.dot.occupied { background: #fc8181; }
.dot.selected { background: #63b3ed; }

.ports-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 8px;
}

.port-item {
  padding: 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
  border: 1px solid transparent;
}

.port-item.available {
  background: #252542;
  color: #e2e8f0;
}

.port-item.available:hover {
  background: #2d3748;
  border-color: #68d391;
}

.port-item.occupied {
  background: #3d2a2a;
  color: #fc8181;
  cursor: not-allowed;
  opacity: 0.7;
}

.port-item.selected {
  background: linear-gradient(135deg, #1a365d 0%, #2c5282 100%);
  color: white;
  border-color: #63b3ed;
  box-shadow: 0 0 0 2px rgba(99, 179, 237, 0.3);
}

.port-number {
  font-size: 14px;
  font-weight: 600;
  font-family: 'SF Mono', Monaco, monospace;
  margin-bottom: 4px;
}

.port-service {
  font-size: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

.service-icon {
  font-size: 14px;
}

.service-name {
  color: #a0aec0;
}

.port-status {
  font-size: 10px;
  color: #718096;
}

/* Action Section */
.action-section {
  display: flex;
  justify-content: center;
}

.connect-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 32px;
  background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.connect-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(66, 153, 225, 0.3);
}

.connect-btn.disabled {
  background: #2d3748;
  color: #718096;
  cursor: not-allowed;
}

.connect-btn.connected {
  background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
}

.btn-icon {
  font-size: 16px;
}

/* Action Wrapper */
.action-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.action-hint {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #718096;
}

.hint-icon {
  font-size: 14px;
}

.action-hint code {
  background: #2d3748;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'SF Mono', Monaco, monospace;
  color: #63b3ed;
  font-size: 11px;
}

/* Footer */
.ports-footer {
  padding: 16px 24px;
  background: #16162a;
  border-top: 1px solid #2d2d44;
}

.footer-tip {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: #a0aec0;
}

.tip-icon {
  font-size: 14px;
}

.footer-tip code {
  background: #2d3748;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'SF Mono', Monaco, monospace;
  color: #fc8181;
  font-size: 11px;
}

@media (max-width: 640px) {
  .computer-section {
    flex-direction: column;
  }

  .connection-visual {
    height: 60px;
  }

  .connection-line {
    width: 100px;
    height: 2px;
  }

  @keyframes packetMove {
    0% {
      left: 0;
      opacity: 1;
    }
    100% {
      left: 100%;
      opacity: 0;
    }
  }
}
</style>
