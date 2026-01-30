<script setup lang="ts">
import { ref, computed } from 'vue'

interface TechItem {
  name: string
  icon: string
  description: string
}

interface Connection {
  from: string
  to: string
  label: string
  color: string
}

interface Layer {
  id: string
  name: string
  icon: string
  color: string
  description: string
  technologies: TechItem[]
  responsibilities: string[]
}

const layers: Layer[] = [
  {
    id: 'user',
    name: '用户层',
    icon: '👤',
    color: '#ff9500',
    description: '最终用户通过各种设备访问应用',
    responsibilities: ['发起请求', '交互操作', '查看结果'],
    technologies: [
      { name: '浏览器', icon: '🌐', description: 'Chrome, Safari, Firefox' },
      { name: '移动端', icon: '📱', description: 'iOS, Android App' },
      { name: '桌面端', icon: '💻', description: 'Windows, Mac, Linux' }
    ]
  },
  {
    id: 'frontend',
    name: '前端层',
    icon: '🎨',
    color: '#007aff',
    description: '用户直接看到的界面，运行在浏览器中',
    responsibilities: ['页面渲染', '用户交互', '状态管理', 'API 调用'],
    technologies: [
      { name: 'React', icon: '⚛️', description: '组件化 UI 库' },
      { name: 'TypeScript', icon: '📘', description: '类型安全的 JavaScript' },
      { name: 'Tailwind CSS', icon: '🎭', description: '实用优先的 CSS 框架' },
      { name: 'shadcn/ui', icon: '🧩', description: '可复用的 UI 组件库' }
    ]
  },
  {
    id: 'backend',
    name: '后端层',
    icon: '⚙️',
    color: '#5856d6',
    description: '处理业务逻辑，运行在服务器上',
    responsibilities: ['业务逻辑', '身份认证', '数据处理', 'API 设计'],
    technologies: [
      { name: 'Next.js', icon: '▲', description: '全栈 React 框架' },
      { name: 'Node.js', icon: '🟢', description: 'JavaScript 运行时' },
      { name: 'better-auth', icon: '🔐', description: '类型安全的认证库' },
      { name: 'AI SDK', icon: '🤖', description: 'Vercel AI SDK' }
    ]
  },
  {
    id: 'database',
    name: '数据层',
    icon: '💾',
    color: '#34c759',
    description: '存储和管理应用数据',
    responsibilities: ['数据持久化', '查询优化', '事务管理', '备份恢复'],
    technologies: [
      { name: 'PostgreSQL', icon: '🐘', description: '关系型数据库' },
      { name: 'Drizzle ORM', icon: '🌧️', description: '类型安全的 ORM' },
      { name: 'Redis', icon: '🔴', description: '内存缓存数据库' },
      { name: 'Supabase', icon: '⚡', description: '开源 Firebase 替代' }
    ]
  },
  {
    id: 'infra',
    name: '基础设施',
    icon: '🏗️',
    color: '#af52de',
    description: '支撑应用运行的基础环境',
    responsibilities: ['部署托管', '负载均衡', '安全防护', '监控日志'],
    technologies: [
      { name: 'Vercel', icon: '▲', description: '前端部署平台' },
      { name: 'Docker', icon: '🐳', description: '容器化技术' },
      { name: 'Nginx', icon: '🌊', description: '反向代理服务器' },
      { name: 'GitHub', icon: '🐙', description: '代码托管与 CI/CD' }
    ]
  }
]

const connections: Connection[] = [
  { from: 'user', to: 'frontend', label: 'HTTP/HTTPS', color: '#ff9500' },
  { from: 'frontend', to: 'backend', label: 'API 请求', color: '#007aff' },
  { from: 'backend', to: 'database', label: 'SQL/ORM', color: '#5856d6' },
  { from: 'backend', to: 'infra', label: '部署', color: '#34c759' },
  { from: 'frontend', to: 'infra', label: 'CDN', color: '#af52de' }
]

const selectedLayer = ref<string | null>(null)
const hoveredTech = ref<string | null>(null)
const showDataFlow = ref(false)

const currentLayer = computed(() => layers.find(l => l.id === selectedLayer.value))

function selectLayer(id: string) {
  selectedLayer.value = selectedLayer.value === id ? null : id
}

function getConnectedLayers(layerId: string) {
  return connections
    .filter(c => c.from === layerId || c.to === layerId)
    .map(c => c.from === layerId ? c.to : c.from)
}

function isConnected(layerId: string) {
  if (!selectedLayer.value) return false
  return getConnectedLayers(selectedLayer.value).includes(layerId)
}
</script>

<template>
  <div class="tech-stack-layers">
    <div class="controls">
      <button
        class="flow-toggle"
        :class="{ active: showDataFlow }"
        @click="showDataFlow = !showDataFlow"
      >
        <span class="toggle-icon">{{ showDataFlow ? '🔴' : '⚪' }}</span>
        <span>{{ showDataFlow ? '隐藏数据流' : '显示数据流' }}</span>
      </button>
    </div>

    <div class="architecture-container">
      <!-- 左侧：层级堆叠 -->
      <div class="layers-stack">
        <div
          v-for="(layer, index) in layers"
          :key="layer.id"
          class="layer-card"
          :class="{
            selected: selectedLayer === layer.id,
            connected: isConnected(layer.id),
            dimmed: selectedLayer && !isConnected(layer.id) && selectedLayer !== layer.id
          }"
          :style="{ '--layer-color': layer.color }"
          @click="selectLayer(layer.id)"
        >
          <div class="layer-header">
            <span class="layer-icon" :style="{ background: layer.color }">{{ layer.icon }}</span>
            <div class="layer-info">
              <span class="layer-name">{{ layer.name }}</span>
              <span class="layer-desc">{{ layer.description }}</span>
            </div>
            <span class="layer-number">{{ index + 1 }}</span>
          </div>

          <div class="layer-technologies">
            <div
              v-for="tech in layer.technologies"
              :key="tech.name"
              class="tech-item"
              :class="{ hovered: hoveredTech === tech.name }"
              @mouseenter="hoveredTech = tech.name"
              @mouseleave="hoveredTech = null"
            >
              <span class="tech-icon">{{ tech.icon }}</span>
              <div class="tech-info">
                <span class="tech-name">{{ tech.name }}</span>
                <span class="tech-desc">{{ tech.description }}</span>
              </div>
            </div>
          </div>

          <!-- 连接指示器 -->
          <div v-if="showDataFlow" class="connection-points">
            <div v-if="index > 0" class="connection-point in" :style="{ borderColor: layer.color }">
              ← 输入
            </div>
            <div v-if="index < layers.length - 1" class="connection-point out" :style="{ borderColor: layer.color }">
              输出 →
            </div>
          </div>
        </div>
      </div>

      <!-- 右侧：连接图 -->
      <div v-if="showDataFlow" class="connections-panel">
        <h4>🔗 层间连接</h4>
        <div class="connections-list">
          <div
            v-for="conn in connections"
            :key="`${conn.from}-${conn.to}`"
            class="connection-item"
            :class="{
              highlighted: selectedLayer && (conn.from === selectedLayer || conn.to === selectedLayer)
            }"
            :style="{ borderLeftColor: conn.color }"
          >
            <div class="connection-ends">
              <span class="from">{{ layers.find(l => l.id === conn.from)?.name }}</span>
              <span class="arrow">→</span>
              <span class="to">{{ layers.find(l => l.id === conn.to)?.name }}</span>
            </div>
            <span class="connection-label" :style="{ color: conn.color }">{{ conn.label }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 详情面板 -->
    <div v-if="currentLayer" class="detail-panel" :style="{ borderColor: currentLayer.color }">
      <div class="detail-header">
        <span class="detail-icon" :style="{ background: currentLayer.color }">
          {{ currentLayer.icon }}
        </span>
        <div>
          <h4 :style="{ color: currentLayer.color }">{{ currentLayer.name }}</h4>
          <p>{{ currentLayer.description }}</p>
        </div>
      </div>

      <div class="detail-sections">
        <div class="detail-section">
          <h5>📋 主要职责</h5>
          <ul>
            <li v-for="resp in currentLayer.responsibilities" :key="resp">{{ resp }}</li>
          </ul>
        </div>

        <div class="detail-section">
          <h5>🛠️ 核心技术</h5>
          <div class="tech-grid">
            <div
              v-for="tech in currentLayer.technologies"
              :key="tech.name"
              class="tech-card"
            >
              <span class="tech-card-icon">{{ tech.icon }}</span>
              <span class="tech-card-name">{{ tech.name }}</span>
              <span class="tech-card-desc">{{ tech.description }}</span>
            </div>
          </div>
        </div>

        <div v-if="selectedLayer !== 'user'" class="detail-section">
          <h5>🔗 数据流向</h5>
          <div class="data-flow">
            <div
              v-for="conn in connections.filter(c => c.from === selectedLayer || c.to === selectedLayer)"
              :key="`${conn.from}-${conn.to}`"
              class="flow-item"
            >
              <span v-if="conn.from === selectedLayer">
                输出到 <strong>{{ layers.find(l => l.id === conn.to)?.name }}</strong>
                <span class="flow-label" :style="{ color: conn.color }">({{ conn.label }})</span>
              </span>
              <span v-else>
                接收来自 <strong>{{ layers.find(l => l.id === conn.from)?.name }}</strong>
                <span class="flow-label" :style="{ color: conn.color }">({{ conn.label }})</span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 全栈概览 -->
    <div v-if="!selectedLayer" class="overview-panel">
      <h4>🎯 本教程技术栈概览</h4>
      <div class="stack-summary">
        <div class="summary-item">
          <span class="summary-icon" style="background: #007aff;">🎨</span>
          <div class="summary-content">
            <strong>前端</strong>
            <span>React + TypeScript + Tailwind CSS + shadcn/ui</span>
          </div>
        </div>
        <div class="summary-arrow">→</div>
        <div class="summary-item">
          <span class="summary-icon" style="background: #5856d6;">⚙️</span>
          <div class="summary-content">
            <strong>后端</strong>
            <span>Next.js + better-auth + AI SDK</span>
          </div>
        </div>
        <div class="summary-arrow">→</div>
        <div class="summary-item">
          <span class="summary-icon" style="background: #34c759;">💾</span>
          <div class="summary-content">
            <strong>数据</strong>
            <span>PostgreSQL + Drizzle ORM</span>
          </div>
        </div>
        <div class="summary-arrow">→</div>
        <div class="summary-item">
          <span class="summary-icon" style="background: #af52de;">🏗️</span>
          <div class="summary-content">
            <strong>部署</strong>
            <span>Vercel + Docker</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tech-stack-layers {
  background: linear-gradient(180deg, #f5f5f7 0%, #e8e8ed 100%);
  border-radius: 20px;
  padding: 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.controls {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 16px;
}

.flow-toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: white;
  border: 1px solid #d1d1d6;
  border-radius: 8px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.flow-toggle:hover {
  background: #f5f5f7;
}

.flow-toggle.active {
  background: #007aff;
  color: white;
  border-color: #007aff;
}

.toggle-icon {
  font-size: 14px;
}

.architecture-container {
  display: flex;
  gap: 20px;
}

.layers-stack {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.layer-card {
  background: white;
  border-radius: 16px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  position: relative;
}

.layer-card:hover {
  transform: translateX(8px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.layer-card.selected {
  border-color: var(--layer-color);
  box-shadow: 0 0 0 4px rgba(0, 0, 0, 0.04), 0 4px 20px rgba(0, 0, 0, 0.1);
}

.layer-card.connected {
  border-color: var(--layer-color);
  opacity: 0.9;
}

.layer-card.dimmed {
  opacity: 0.4;
}

.layer-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.layer-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
}

.layer-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.layer-name {
  font-size: 17px;
  font-weight: 600;
  color: #1d1d1f;
}

.layer-desc {
  font-size: 12px;
  color: #8e8e93;
}

.layer-number {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #f5f5f7;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 600;
  color: #8e8e93;
}

.layer-technologies {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 10px;
}

.tech-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  background: #f5f5f7;
  border-radius: 10px;
  transition: all 0.2s ease;
}

.tech-item:hover {
  background: #e8e8ed;
  transform: translateY(-2px);
}

.tech-item.hovered {
  background: rgba(0, 122, 255, 0.1);
}

.tech-icon {
  font-size: 18px;
}

.tech-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
}

.tech-name {
  font-size: 13px;
  font-weight: 600;
  color: #1d1d1f;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tech-desc {
  font-size: 10px;
  color: #8e8e93;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.connection-points {
  display: flex;
  justify-content: space-between;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px dashed #e8e8ed;
}

.connection-point {
  padding: 4px 12px;
  border: 1px solid;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 500;
}

.connections-panel {
  width: 240px;
  background: white;
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.connections-panel h4 {
  margin: 0 0 16px 0;
  font-size: 14px;
  color: #1d1d1f;
}

.connections-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.connection-item {
  padding: 12px;
  background: #f5f5f7;
  border-radius: 10px;
  border-left: 3px solid;
  transition: all 0.2s ease;
}

.connection-item.highlighted {
  background: rgba(0, 122, 255, 0.08);
  transform: scale(1.02);
}

.connection-ends {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  margin-bottom: 4px;
}

.connection-ends .from,
.connection-ends .to {
  font-weight: 500;
  color: #1d1d1f;
}

.connection-ends .arrow {
  color: #8e8e93;
}

.connection-label {
  font-size: 11px;
  font-weight: 500;
}

.detail-panel {
  margin-top: 20px;
  background: white;
  border-radius: 16px;
  padding: 24px;
  border-left: 4px solid;
  animation: slideUp 0.3s ease;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.detail-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.detail-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
}

.detail-header h4 {
  margin: 0 0 4px 0;
  font-size: 20px;
}

.detail-header p {
  margin: 0;
  font-size: 14px;
  color: #8e8e93;
}

.detail-sections {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.detail-section h5 {
  margin: 0 0 12px 0;
  font-size: 14px;
  color: #1d1d1f;
  font-weight: 600;
}

.detail-section ul {
  margin: 0;
  padding-left: 20px;
  font-size: 13px;
  color: #3a3a3c;
}

.detail-section li {
  margin-bottom: 6px;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 10px;
}

.tech-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 16px 12px;
  background: #f5f5f7;
  border-radius: 12px;
  text-align: center;
}

.tech-card-icon {
  font-size: 24px;
}

.tech-card-name {
  font-size: 13px;
  font-weight: 600;
  color: #1d1d1f;
}

.tech-card-desc {
  font-size: 10px;
  color: #8e8e93;
}

.data-flow {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.flow-item {
  padding: 10px 14px;
  background: #f5f5f7;
  border-radius: 8px;
  font-size: 13px;
  color: #3a3a3c;
}

.flow-label {
  font-weight: 500;
}

.overview-panel {
  margin-top: 20px;
  background: white;
  border-radius: 16px;
  padding: 24px;
}

.overview-panel h4 {
  margin: 0 0 20px 0;
  font-size: 16px;
  color: #1d1d1f;
}

.stack-summary {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.summary-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: #f5f5f7;
  border-radius: 12px;
  flex: 1;
  min-width: 200px;
}

.summary-icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}

.summary-content {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.summary-content strong {
  font-size: 14px;
  color: #1d1d1f;
}

.summary-content span {
  font-size: 12px;
  color: #8e8e93;
}

.summary-arrow {
  font-size: 20px;
  color: #c7c7cc;
}

@media (max-width: 768px) {
  .architecture-container {
    flex-direction: column;
  }

  .connections-panel {
    width: auto;
  }

  .layer-technologies {
    grid-template-columns: repeat(2, 1fr);
  }

  .stack-summary {
    flex-direction: column;
    align-items: stretch;
  }

  .summary-arrow {
    transform: rotate(90deg);
    text-align: center;
  }
}
</style>
