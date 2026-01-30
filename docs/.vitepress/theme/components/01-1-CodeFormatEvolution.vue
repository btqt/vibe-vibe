<script setup lang="ts">
import { ref } from 'vue'

interface Stage {
  id: string
  year: string
  name: string
  icon: string
  description: string
  features: string[]
  codeExample: string
}

const stages: Stage[] = [
  {
    id: 'binary',
    year: '1940s',
    name: '机器语言',
    icon: '0️⃣1️⃣',
    description: '计算机原生语言，由0和1组成',
    features: ['直接执行', '效率最高', '人类难读'],
    codeExample: '10110000 01100001'
  },
  {
    id: 'assembly',
    year: '1950s',
    name: '汇编语言',
    icon: '📝',
    description: '用助记符代替二进制指令',
    features: ['符号化指令', '硬件相关', '需要汇编器'],
    codeExample: 'MOV AX, 61h\nINT 21h'
  },
  {
    id: 'compiled',
    year: '1970s',
    name: '高级语言',
    icon: '🔧',
    description: '接近人类语言，需编译执行',
    features: ['跨平台', '抽象度高', '需要编译'],
    codeExample: '#include <stdio.h>\nint main() {\n  printf("Hello");\n  return 0;\n}'
  },
  {
    id: 'modern',
    year: '2000s+',
    name: '现代语言',
    icon: '🚀',
    description: '简洁、安全、高效',
    features: ['类型安全', '自动内存', '丰富生态'],
    codeExample: 'console.log("Hello")'
  }
]

const currentStage = ref(0)

function selectStage(index: number) {
  currentStage.value = index
}
</script>

<template>
  <div class="code-format-evolution">
    <div class="timeline">
      <div
        v-for="(stage, index) in stages"
        :key="stage.id"
        class="timeline-node"
        :class="{ active: currentStage === index, completed: currentStage > index }"
        @click="selectStage(index)"
      >
        <div class="node-year">{{ stage.year }}</div>
        <div class="node-dot"></div>
        <div class="node-name">{{ stage.name }}</div>
      </div>
    </div>

    <div class="stage-detail">
      <div class="stage-header">
        <span class="stage-icon">{{ stages[currentStage].icon }}</span>
        <span class="stage-title">{{ stages[currentStage].name }}</span>
        <span class="stage-year">{{ stages[currentStage].year }}</span>
      </div>

      <p class="stage-desc">{{ stages[currentStage].description }}</p>

      <div class="stage-features">
        <span
          v-for="feature in stages[currentStage].features"
          :key="feature"
          class="feature-tag"
        >
          {{ feature }}
        </span>
      </div>

      <div class="code-window">
        <div class="code-header">
          <div class="code-dots">
            <span></span>
            <span></span>
            <span></span>
          </div>
          <span class="code-title">示例代码</span>
        </div>
        <pre class="code-content"><code>{{ stages[currentStage].codeExample }}</code></pre>
      </div>
    </div>

    <div class="evolution-arrow">
      <span>演变趋势：越来越接近人类语言</span>
      <div class="arrow">→</div>
    </div>
  </div>
</template>

<style scoped>
.code-format-evolution {
  background: linear-gradient(180deg, #f5f5f7 0%, #e8e8ed 100%);
  border-radius: 20px;
  padding: 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.timeline {
  display: flex;
  justify-content: space-between;
  margin-bottom: 24px;
  position: relative;
  padding: 0 10px;
}

.timeline::before {
  content: '';
  position: absolute;
  top: 35px;
  left: 15%;
  right: 15%;
  height: 2px;
  background: linear-gradient(90deg, #007aff 0%, #007aff calc(var(--progress, 0%)), #d1d1d6 calc(var(--progress, 0%)));
}

.timeline-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  z-index: 1;
}

.node-year {
  font-size: 11px;
  color: #8e8e93;
  font-weight: 500;
}

.node-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #d1d1d6;
  border: 3px solid white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.timeline-node.active .node-dot {
  background: #007aff;
  transform: scale(1.3);
}

.timeline-node.completed .node-dot {
  background: #34c759;
}

.node-name {
  font-size: 12px;
  color: #3a3a3c;
  font-weight: 500;
}

.timeline-node.active .node-name {
  color: #007aff;
}

.stage-detail {
  background: white;
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.stage-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.stage-icon {
  font-size: 24px;
}

.stage-title {
  flex: 1;
  font-size: 20px;
  font-weight: 600;
  color: #1d1d1f;
}

.stage-year {
  padding: 4px 10px;
  background: #f5f5f7;
  border-radius: 6px;
  font-size: 13px;
  color: #8e8e93;
}

.stage-desc {
  font-size: 14px;
  color: #3a3a3c;
  margin-bottom: 16px;
}

.stage-features {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
}

.feature-tag {
  padding: 6px 12px;
  background: rgba(0, 122, 255, 0.1);
  color: #007aff;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 500;
}

.code-window {
  border: 1px solid #e8e8ed;
  border-radius: 12px;
  overflow: hidden;
}

.code-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  background: #f5f5f7;
  border-bottom: 1px solid #e8e8ed;
}

.code-dots {
  display: flex;
  gap: 6px;
}

.code-dots span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #c7c7cc;
}

.code-dots span:nth-child(1) { background: #ff5f56; }
.code-dots span:nth-child(2) { background: #ffbd2e; }
.code-dots span:nth-child(3) { background: #27c93f; }

.code-title {
  font-size: 12px;
  color: #8e8e93;
}

.code-content {
  margin: 0;
  padding: 16px;
  background: #1e1e2e;
  color: #f0f0f0;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 13px;
  line-height: 1.6;
  overflow-x: auto;
}

.evolution-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-top: 20px;
  padding: 12px;
  background: rgba(0, 122, 255, 0.08);
  border-radius: 10px;
}

.evolution-arrow span {
  font-size: 13px;
  color: #007aff;
  font-weight: 500;
}

.arrow {
  font-size: 20px;
  color: #007aff;
}

@media (max-width: 640px) {
  .timeline {
    flex-wrap: wrap;
    gap: 16px;
  }

  .timeline::before {
    display: none;
  }

  .timeline-node {
    flex: 1;
    min-width: 70px;
  }
}
</style>
