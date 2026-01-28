<script setup lang="ts">
import { ref, computed } from 'vue'

interface Package {
  name: string
  category: string
  description: string
}

const packages: Package[] = [
  { name: 'react', category: 'UI 框架', description: '用于构建用户界面的 JavaScript 库' },
  { name: 'next', category: '全栈框架', description: 'React 全栈框架，支持 SSR 和静态生成' },
  { name: 'vue', category: 'UI 框架', description: '渐进式 JavaScript 框架' },
  { name: 'axios', category: 'HTTP 请求', description: '基于 Promise 的 HTTP 客户端' },
  { name: 'lodash', category: '工具库', description: '现代 JavaScript 实用工具库' },
  { name: 'dayjs', category: '日期处理', description: '轻量级日期处理库' },
  { name: 'zod', category: '数据验证', description: 'TypeScript 优先的模式验证' },
  { name: 'tailwindcss', category: 'CSS 框架', description: '实用优先的 CSS 框架' },
  { name: '@tanstack/query', category: '数据管理', description: '强大的异步状态管理' },
  { name: 'prisma', category: 'ORM', description: '下一代 Node.js 和 TypeScript ORM' },
  { name: 'typescript', category: '开发工具', description: 'JavaScript 的超集，添加类型系统' },
  { name: 'vite', category: '构建工具', description: '下一代前端构建工具' },
  { name: 'eslint', category: '代码质量', description: '可插拔的 JavaScript 代码检查工具' },
  { name: 'prettier', category: '代码格式化', description: '固执的代码格式化工具' },
  { name: 'shadcn/ui', category: 'UI 组件', description: '设计精美的可复用组件' },
  { name: 'motion', category: '动画', description: 'React 动画库（原 Framer Motion）' },
  { name: 'express', category: '后端框架', description: '极简的 Node.js Web 框架' },
  { name: 'hono', category: '后端框架', description: '轻量级、高性能的 Web 框架' },
  { name: 'trpc', category: 'API', description: '端到端类型安全的 API 框架' },
  { name: 'zustand', category: '状态管理', description: '轻量级的 React 状态管理' },
]

const categories = ['全部', 'UI 框架', '全栈框架', '后端框架', 'HTTP 请求', '工具库', 'CSS 框架', '数据管理', '状态管理', 'API', 'ORM', '代码质量', '代码格式化', 'UI 组件', '动画', '开发工具', '构建工具']
const activeCategory = ref('全部')

const filteredPackages = computed(() => {
  if (activeCategory.value === '全部') return packages
  return packages.filter(p => p.category === activeCategory.value)
})
</script>

<template>
  <div class="package-list">
    <div class="category-tabs">
      <button
        v-for="cat in categories"
        :key="cat"
        class="tab-btn"
        :class="{ active: activeCategory === cat }"
        @click="activeCategory = cat"
      >
        {{ cat }}
      </button>
    </div>

    <div class="packages-list">
      <div
        v-for="pkg in filteredPackages"
        :key="pkg.name"
        class="package-item"
      >
        <div class="pkg-main">
          <code class="pkg-name">{{ pkg.name }}</code>
          <span class="pkg-category">{{ pkg.category }}</span>
        </div>
        <div class="pkg-desc">{{ pkg.description }}</div>
      </div>
    </div>

    <div class="list-footer">
      <span>在 <a href="https://www.npmjs.com" target="_blank" rel="noopener">npmjs.com</a> 发现更多包</span>
    </div>
  </div>
</template>

<style scoped>
.package-list {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #1e1e2e;
  border-radius: 10px;
  overflow: hidden;
}

.category-tabs {
  display: flex;
  gap: 6px;
  padding: 12px 16px;
  background: #16162a;
  border-bottom: 1px solid #2d2d44;
  overflow-x: auto;
}

.tab-btn {
  padding: 4px 10px;
  background: transparent;
  border: 1px solid #2d2d44;
  border-radius: 12px;
  color: #a0aec0;
  font-size: 11px;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.tab-btn:hover {
  border-color: #4a5568;
  color: #e2e8f0;
}

.tab-btn.active {
  background: #CB3837;
  border-color: #CB3837;
  color: white;
}

.packages-list {
  padding: 8px;
  max-height: 320px;
  overflow-y: auto;
}

.package-item {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.03);
}

.package-item:last-child {
  border-bottom: none;
}

.pkg-main {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.pkg-name {
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 13px;
  color: #63b3ed;
  font-weight: 500;
}

.pkg-category {
  font-size: 10px;
  padding: 1px 6px;
  background: rgba(104, 211, 145, 0.15);
  color: #68d391;
  border-radius: 8px;
}

.pkg-desc {
  font-size: 12px;
  color: #a0aec0;
}

.list-footer {
  padding: 10px 16px;
  background: #16162a;
  border-top: 1px solid #2d2d44;
  font-size: 11px;
  color: #718096;
  text-align: center;
}

.list-footer a {
  color: #CB3837;
  text-decoration: none;
}

.list-footer a:hover {
  text-decoration: underline;
}
</style>
