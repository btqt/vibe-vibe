<script setup lang="ts">
import { ref, computed } from 'vue'

interface FileNode {
  name: string
  type: 'file' | 'directory' | 'executable'
  size?: string
  description?: string
  warning?: boolean
  children?: FileNode[]
}

const fileTree = ref<FileNode>({
  name: 'my-project',
  type: 'directory',
  description: '项目根目录',
  children: [
    {
      name: 'node_modules',
      type: 'directory',
      description: '依赖包目录 (自动生成)',
      children: [
        { name: '.bin', type: 'directory', description: '可执行命令' },
        { name: 'next', type: 'directory', description: 'Next.js 框架' },
        { name: 'react', type: 'directory', description: 'React 库' },
        { name: 'react-dom', type: 'directory', description: 'React DOM' },
        { name: 'typescript', type: 'directory', description: 'TypeScript 编译器' },
        { name: '@types', type: 'directory', description: '类型定义' },
        { name: 'tailwindcss', type: 'directory', description: 'Tailwind CSS' }
      ]
    },
    {
      name: 'src',
      type: 'directory',
      description: '源代码目录',
      children: [
        {
          name: 'app',
          type: 'directory',
          description: 'Next.js App Router',
          children: [
            { name: 'page.tsx', type: 'file', size: '2.3KB', description: '首页路由组件' },
            { name: 'layout.tsx', type: 'file', size: '1.8KB', description: '根布局组件' },
            { name: 'globals.css', type: 'file', size: '3.2KB', description: '全局样式' },
            { name: 'loading.tsx', type: 'file', size: '0.8KB', description: '加载状态组件' },
            { name: 'error.tsx', type: 'file', size: '1.2KB', description: '错误处理组件' },
            {
              name: 'dashboard',
              type: 'directory',
              description: '仪表盘路由',
              children: [
                { name: 'page.tsx', type: 'file', size: '1.5KB', description: '仪表盘页面' },
                { name: 'layout.tsx', type: 'file', size: '0.9KB', description: '仪表盘布局' }
              ]
            },
            {
              name: 'api',
              type: 'directory',
              description: 'API 路由',
              children: [
                { name: 'route.ts', type: 'file', size: '1.1KB', description: 'API 端点' }
              ]
            }
          ]
        },
        {
          name: 'components',
          type: 'directory',
          description: '可复用组件',
          children: [
            {
              name: 'ui',
              type: 'directory',
              description: 'UI 基础组件',
              children: [
                { name: 'button.tsx', type: 'file', size: '2.1KB', description: '按钮组件' },
                { name: 'card.tsx', type: 'file', size: '1.6KB', description: '卡片组件' },
                { name: 'input.tsx', type: 'file', size: '1.9KB', description: '输入框组件' },
                { name: 'modal.tsx', type: 'file', size: '2.4KB', description: '弹窗组件' }
              ]
            },
            {
              name: 'layout',
              type: 'directory',
              description: '布局组件',
              children: [
                { name: 'header.tsx', type: 'file', size: '1.8KB', description: '顶部导航' },
                { name: 'sidebar.tsx', type: 'file', size: '2.2KB', description: '侧边栏' },
                { name: 'footer.tsx', type: 'file', size: '1.3KB', description: '页脚' }
              ]
            }
          ]
        },
        {
          name: 'lib',
          type: 'directory',
          description: '工具库',
          children: [
            { name: 'utils.ts', type: 'file', size: '0.6KB', description: '工具函数' },
            { name: 'api.ts', type: 'file', size: '1.4KB', description: 'API 客户端' },
            { name: 'constants.ts', type: 'file', size: '0.8KB', description: '常量定义' }
          ]
        },
        {
          name: 'hooks',
          type: 'directory',
          description: '自定义 Hooks',
          children: [
            { name: 'useAuth.ts', type: 'file', size: '1.2KB', description: '认证 Hook' },
            { name: 'useFetch.ts', type: 'file', size: '1.5KB', description: '数据获取 Hook' }
          ]
        },
        {
          name: 'types',
          type: 'directory',
          description: '类型定义',
          children: [
            { name: 'index.ts', type: 'file', size: '0.9KB', description: '全局类型' },
            { name: 'api.ts', type: 'file', size: '1.1KB', description: 'API 类型' }
          ]
        }
      ]
    },
    {
      name: 'public',
      type: 'directory',
      description: '静态资源',
      children: [
        { name: 'favicon.ico', type: 'file', size: '4KB' },
        { name: 'logo.svg', type: 'file', size: '2KB', description: 'Logo' },
        { name: 'robots.txt', type: 'file', size: '0.1KB', description: '爬虫规则' },
        {
          name: 'images',
          type: 'directory',
          description: '图片资源',
          children: [
            { name: 'hero.png', type: 'file', size: '156KB' },
            { name: 'avatar.jpg', type: 'file', size: '24KB' }
          ]
        }
      ]
    },
    {
      name: '.next',
      type: 'directory',
      description: '构建输出 (自动生成)',
      children: [
        { name: 'static', type: 'directory' },
        { name: 'server', type: 'directory' },
        { name: 'build-manifest.json', type: 'file', size: '12KB' }
      ]
    },
    {
      name: 'scripts',
      type: 'directory',
      description: '脚本文件',
      children: [
        { name: 'build.sh', type: 'executable', size: '0.5KB', description: '构建脚本' },
        { name: 'deploy.sh', type: 'executable', size: '0.8KB', description: '部署脚本' }
      ]
    },
    {
      name: 'tests',
      type: 'directory',
      description: '测试文件',
      children: [
        { name: 'unit', type: 'directory', description: '单元测试' },
        { name: 'e2e', type: 'directory', description: '端到端测试' }
      ]
    },
    {
      name: 'docs',
      type: 'directory',
      description: '文档',
      children: [
        { name: 'README.md', type: 'file', size: '5KB' },
        { name: 'API.md', type: 'file', size: '8KB' }
      ]
    },
    {
      name: 'package.json',
      type: 'file',
      size: '2.4KB',
      description: '项目配置 & 依赖'
    },
    {
      name: 'tsconfig.json',
      type: 'file',
      size: '1.2KB',
      description: 'TypeScript 配置'
    },
    {
      name: 'next.config.js',
      type: 'file',
      size: '0.8KB',
      description: 'Next.js 配置'
    },
    {
      name: 'tailwind.config.ts',
      type: 'file',
      size: '1.5KB',
      description: 'Tailwind 配置'
    },
    {
      name: 'postcss.config.js',
      type: 'file',
      size: '0.3KB',
      description: 'PostCSS 配置'
    },
    {
      name: 'eslint.config.mjs',
      type: 'file',
      size: '0.9KB',
      description: 'ESLint 配置'
    },
    {
      name: 'prettier.config.js',
      type: 'file',
      size: '0.4KB',
      description: 'Prettier 配置'
    },
    {
      name: 'vitest.config.ts',
      type: 'file',
      size: '0.7KB',
      description: 'Vitest 测试配置'
    },
    {
      name: '.env.local',
      type: 'file',
      size: '0.5KB',
      description: '本地环境变量 (不提交)'
    },
    {
      name: '.env.example',
      type: 'file',
      size: '0.4KB',
      description: '环境变量示例'
    },
    {
      name: '.gitignore',
      type: 'file',
      size: '0.6KB',
      description: 'Git 忽略规则'
    },
    {
      name: 'README.md',
      type: 'file',
      size: '4.5KB',
      description: '项目说明文档'
    },
    {
      name: 'LICENSE',
      type: 'file',
      size: '1.1KB',
      description: '许可证'
    },
    {
      name: 'pnpm-lock.yaml',
      type: 'file',
      size: '245KB',
      description: '依赖锁定文件'
    }
  ]
})

const expandedNodes = ref<Set<string>>(new Set(['my-project', 'src', 'app']))
const selectedNode = ref<string | null>(null)
const showWarning = ref(false)

function toggleNode(node: FileNode, path: string) {
  if (node.type !== 'directory') {
    selectedNode.value = path
    return
  }

  if (expandedNodes.value.has(path)) {
    expandedNodes.value.delete(path)
  } else {
    expandedNodes.value.add(path)
  }
}

function isExpanded(path: string): boolean {
  return expandedNodes.value.has(path)
}

function getNodeIcon(node: FileNode): string {
  switch (node.type) {
    case 'directory': return '📁'
    case 'executable': return '⚡'
    default: return '📄'
  }
}

function getNodeClass(node: FileNode): string {
  const classes = [node.type]
  if (node.warning) classes.push('warning')
  return classes.join(' ')
}

function checkPathName(name: string): boolean {
  // 检查是否包含中文或空格
  return /[\u4e00-\u9fa5\s]/.test(name)
}

function showPathWarning() {
  showWarning.value = true
  setTimeout(() => showWarning.value = false, 3000)
}

function renderTree(node: FileNode, path: string = '', level: number = 0): { node: FileNode, path: string, level: number, isLast: boolean }[] {
  const currentPath = path ? `${path}/${node.name}` : node.name
  const result: { node: FileNode, path: string, level: number, isLast: boolean }[] = []

  result.push({ node, path: currentPath, level, isLast: !node.children || node.children.length === 0 })

  if (node.children && isExpanded(currentPath)) {
    node.children.forEach((child, index) => {
      result.push(...renderTree(child, currentPath, level + 1))
    })
  }

  return result
}

const flattenedTree = computed(() => renderTree(fileTree.value))
</script>

<template>
  <div class="fs-tree">
    <div class="tree-window">
      <!-- 标题栏 -->
      <div class="tree-header">
        <div class="window-controls">
          <span class="control close"></span>
          <span class="control minimize"></span>
          <span class="control maximize"></span>
        </div>
        <div class="tree-title">
          <svg class="tree-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
          </svg>
          项目文件结构
        </div>
        <div class="tree-actions">
          <button class="action-btn" @click="showPathWarning" title="路径规范检查">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
              <line x1="12" y1="9" x2="12" y2="13"/>
              <line x1="12" y1="17" x2="12.01" y2="17"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- 警告提示 -->
      <div v-if="showWarning" class="warning-banner">
        <span class="warning-icon">⚠️</span>
        <div class="warning-content">
          <strong>路径规范提醒</strong>
          <span>文件夹和文件名应避免使用中文和空格，以防止工具报错。</span>
        </div>
      </div>

      <!-- 文件树 -->
      <div class="tree-content">
        <div
          v-for="item in flattenedTree"
          :key="item.path"
          class="tree-node"
          :class="{
            selected: selectedNode === item.path,
            expandable: item.node.type === 'directory',
            expanded: isExpanded(item.path)
          }"
          :style="{ paddingLeft: `${item.level * 20 + 12}px` }"
          @click="toggleNode(item.node, item.path)"
        >
          <!-- 展开/折叠指示器 -->
          <span v-if="item.node.type === 'directory'" class="expand-icon">
            {{ isExpanded(item.path) ? '▼' : '▶' }}
          </span>
          <span v-else class="expand-icon placeholder"></span>

          <!-- 文件图标 -->
          <span class="node-icon">{{ getNodeIcon(item.node) }}</span>

          <!-- 文件名 -->
          <span
            class="node-name"
            :class="{ 'has-warning': checkPathName(item.node.name) }"
          >
            {{ item.node.name }}
          </span>

          <!-- 文件大小 -->
          <span v-if="item.node.size" class="node-size">{{ item.node.size }}</span>

          <!-- 描述 -->
          <span v-if="item.node.description" class="node-desc">{{ item.node.description }}</span>

          <!-- 中文/空格警告 -->
          <span v-if="checkPathName(item.node.name)" class="name-warning" title="包含中文或空格">
            ⚠️
          </span>
        </div>
      </div>

      <!-- 底部说明 -->
      <div class="tree-footer">
        <div class="footer-stats">
          <span class="stat-item">
            <span class="stat-icon">📁</span>
            目录
          </span>
          <span class="stat-item">
            <span class="stat-icon">📄</span>
            文件
          </span>
          <span class="stat-item">
            <span class="stat-icon">⚡</span>
            可执行
          </span>
        </div>
        <div class="footer-tip">
          💡 点击文件夹展开/折叠，点击文件查看详情
        </div>
      </div>
    </div>

    <!-- 路径规范提示 -->
    <div class="naming-guide">
      <div class="guide-title">
        <span>✅</span>
        <span>推荐命名规范</span>
      </div>
      <div class="guide-content">
        <div class="guide-item good">
          <span class="guide-marker">✓</span>
          <code>my-project</code>
          <span>使用英文连字符</span>
        </div>
        <div class="guide-item good">
          <span class="guide-marker">✓</span>
          <code>my_project</code>
          <span>使用下划线</span>
        </div>
        <div class="guide-item bad">
          <span class="guide-marker">✗</span>
          <code>我的项目</code>
          <span>避免中文</span>
        </div>
        <div class="guide-item bad">
          <span class="guide-marker">✗</span>
          <code>my project</code>
          <span>避免空格</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.fs-tree {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  margin: 20px 0;
}

.tree-window {
  background: #1e1e2e;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

/* Header */
.tree-header {
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

.tree-title {
  flex: 1;
  text-align: center;
  color: #a0a0b0;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.tree-icon {
  width: 16px;
  height: 16px;
  color: #f6ad55;
}

.tree-actions {
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

/* Warning Banner */
.warning-banner {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: linear-gradient(135deg, #744210 0%, #975a16 100%);
  color: #faf089;
  font-size: 13px;
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

.warning-icon {
  font-size: 20px;
}

.warning-content {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.warning-content strong {
  color: #fff;
}

/* Tree Content */
.tree-content {
  padding: 8px 0;
  max-height: 400px;
  overflow-y: auto;
}

.tree-node {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 12px;
  color: #e2e8f0;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.15s;
  border-left: 2px solid transparent;
}

.tree-node:hover {
  background: #252542;
}

.tree-node.selected {
  background: #2c5282;
  border-left-color: #63b3ed;
}

.expand-icon {
  width: 14px;
  text-align: center;
  font-size: 10px;
  color: #718096;
  transition: transform 0.2s;
}

.expand-icon.placeholder {
  visibility: hidden;
}

.node-icon {
  font-size: 14px;
}

.node-name {
  font-family: 'SF Mono', Monaco, monospace;
}

.node-name.has-warning {
  color: #f6ad55;
}

.node-size {
  margin-left: auto;
  font-size: 11px;
  color: #718096;
  font-family: 'SF Mono', Monaco, monospace;
}

.node-desc {
  margin-left: 8px;
  font-size: 11px;
  color: #718096;
}

.name-warning {
  font-size: 12px;
  color: #f6ad55;
  cursor: help;
}

/* Footer */
.tree-footer {
  padding: 12px 16px;
  background: #16162a;
  border-top: 1px solid #2d2d44;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}

.footer-stats {
  display: flex;
  gap: 16px;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: #a0aec0;
}

.stat-icon {
  font-size: 12px;
}

.footer-tip {
  font-size: 11px;
  color: #718096;
}

/* Naming Guide */
.naming-guide {
  margin-top: 16px;
  padding: 16px;
  background: #f7fafc;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.guide-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 12px;
}

.guide-content {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
}

.guide-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 13px;
}

.guide-item.good {
  background: #f0fff4;
}

.guide-item.bad {
  background: #fff5f5;
}

.guide-marker {
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-size: 11px;
  font-weight: 600;
}

.guide-item.good .guide-marker {
  background: #48bb78;
  color: white;
}

.guide-item.bad .guide-marker {
  background: #f56565;
  color: white;
}

.guide-item code {
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 12px;
  padding: 2px 6px;
  background: #fff;
  border-radius: 4px;
  border: 1px solid #e2e8f0;
}

.guide-item span:last-child {
  color: #718096;
  font-size: 12px;
}

@media (max-width: 480px) {
  .guide-content {
    grid-template-columns: 1fr;
  }
}
</style>
