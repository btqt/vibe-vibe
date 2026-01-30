<script setup lang="ts">
import { ref, computed, onMounted, nextTick, watch } from 'vue'

interface FileSystemItem {
  name: string
  type: 'file' | 'directory' | 'executable'
  content?: string
  children?: Record<string, FileSystemItem>
}

interface CommandHistory {
  command: string
  output: string
  isError?: boolean
}

// 文件系统定义
const fileSystem: Record<string, FileSystemItem> = {
  '~': {
    name: '~',
    type: 'directory',
    children: {
      'Documents': {
        name: 'Documents',
        type: 'directory',
        children: {
          'readme.txt': { name: 'readme.txt', type: 'file' },
          'script.sh': { name: 'script.sh', type: 'executable' },
          'projects': {
            name: 'projects',
            type: 'directory',
            children: {
              'my-app': { name: 'my-app', type: 'directory', children: {} },
              'demo': { name: 'demo', type: 'directory', children: {} }
            }
          }
        }
      },
      'Downloads': {
        name: 'Downloads',
        type: 'directory',
        children: {
          'file.zip': { name: 'file.zip', type: 'file' },
          'installer.run': { name: 'installer.run', type: 'executable' }
        }
      },
      'Projects': {
        name: 'Projects',
        type: 'directory',
        children: {
          'app.js': { name: 'app.js', type: 'file' },
          'server.ts': { name: 'server.ts', type: 'file' },
          'start.sh': { name: 'start.sh', type: 'executable' }
        }
      },
      '.config': {
        name: '.config',
        type: 'directory',
        children: {
          'settings.json': { name: 'settings.json', type: 'file' }
        }
      },
      '.bashrc': { name: '.bashrc', type: 'file' },
      'hello.py': { name: 'hello.py', type: 'executable' }
    }
  }
}

// 状态
const currentDir = ref('~')
const input = ref('')
const history = ref<CommandHistory[]>([])
const historyIndex = ref(-1)
const commandHistory = ref<string[]>([])
const showSuggestions = ref(false)
const suggestions = ref<string[]>([])
const selectedSuggestion = ref(0)
const terminalBody = ref<HTMLElement | null>(null)
const inputRef = ref<HTMLInputElement | null>(null)

// 可用命令
const availableCommands = ['help', 'ls', 'pwd', 'cd', 'clear', 'cat', 'echo', 'whoami', 'date']

// 获取当前目录内容
const getCurrentDirContent = (): Record<string, FileSystemItem> | null => {
  const parts = currentDir.value.split('/').filter(p => p)
  let current: FileSystemItem | undefined = fileSystem['~']

  for (const part of parts.slice(1)) {
    if (current?.children?.[part]) {
      current = current.children[part]
    } else {
      return null
    }
  }
  return current?.children || null
}

// 获取文件/文件夹颜色类
const getItemColorClass = (item: FileSystemItem): string => {
  switch (item.type) {
    case 'directory':
      return 'dir-color'
    case 'executable':
      return 'exec-color'
    default:
      return 'file-color'
  }
}

// 获取文件图标
const getItemIcon = (item: FileSystemItem): string => {
  switch (item.type) {
    case 'directory':
      return '📁'
    case 'executable':
      return '⚡'
    default:
      return '📄'
  }
}

// 自动补全
const updateSuggestions = () => {
  const value = input.value
  const parts = value.split(' ')
  const cmd = parts[0]
  const arg = parts[parts.length - 1] || ''

  if (parts.length === 1) {
    // 命令补全
    suggestions.value = availableCommands.filter(c => c.startsWith(cmd) && c !== cmd)
  } else if (['cd', 'ls', 'cat'].includes(cmd)) {
    // 文件/目录补全
    const currentContent = getCurrentDirContent()
    if (currentContent) {
      const items = Object.values(currentContent)
        .filter(item => item.name.startsWith(arg))
        .map(item => item.name + (item.type === 'directory' ? '/' : ''))
      suggestions.value = items
    }
  } else {
    suggestions.value = []
  }

  showSuggestions.value = suggestions.value.length > 0
  selectedSuggestion.value = 0
}

// 应用补全
const applySuggestion = (suggestion: string) => {
  const parts = input.value.split(' ')
  if (parts.length === 1) {
    input.value = suggestion + ' '
  } else {
    parts[parts.length - 1] = suggestion
    input.value = parts.join(' ')
  }
  showSuggestions.value = false
  inputRef.value?.focus()
}

// 处理 Tab 键
const handleTab = (e: Event) => {
  e.preventDefault()
  if (suggestions.value.length > 0) {
    applySuggestion(suggestions.value[selectedSuggestion.value])
  }
}

// 处理键盘导航
const handleKeydown = (e: KeyboardEvent) => {
  if (showSuggestions.value) {
    if (e.key === 'ArrowDown') {
      e.preventDefault()
      selectedSuggestion.value = (selectedSuggestion.value + 1) % suggestions.value.length
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      selectedSuggestion.value = (selectedSuggestion.value - 1 + suggestions.value.length) % suggestions.value.length
    } else if (e.key === 'Escape') {
      showSuggestions.value = false
    }
  }

  // 历史命令
  if (e.key === 'ArrowUp' && !showSuggestions.value) {
    e.preventDefault()
    if (historyIndex.value < commandHistory.value.length - 1) {
      historyIndex.value++
      input.value = commandHistory.value[commandHistory.value.length - 1 - historyIndex.value]
    }
  } else if (e.key === 'ArrowDown' && !showSuggestions.value) {
    e.preventDefault()
    if (historyIndex.value > 0) {
      historyIndex.value--
      input.value = commandHistory.value[commandHistory.value.length - 1 - historyIndex.value]
    } else if (historyIndex.value === 0) {
      historyIndex.value = -1
      input.value = ''
    }
  }
}

// 执行命令
const executeCommand = () => {
  const cmd = input.value.trim()
  if (!cmd) return

  commandHistory.value.push(cmd)
  historyIndex.value = -1

  const parts = cmd.split(' ').filter(p => p)
  const command = parts[0]
  const args = parts.slice(1)

  let output = ''
  let isError = false

  switch (command) {
    case 'help':
      output = `可用命令：
  \x1b[36mls\x1b[0m              列出目录内容
  \x1b[36mpwd\x1b[0m             显示当前路径
  \x1b[36mcd [目录]\x1b[0m       切换目录
  \x1b[36mcat [文件]\x1b[0m      查看文件内容
  \x1b[36mecho [文本]\x1b[0m     输出文本
  \x1b[36mclear\x1b[0m           清屏
  \x1b[36mwhoami\x1b[0m          显示当前用户
  \x1b[36mdate\x1b[0m            显示日期时间
  \x1b[36mhelp\x1b[0m            显示此帮助

提示：按 \x1b[33mTab\x1b[0m 键自动补全命令和文件名`
      break

    case 'ls':
      const content = getCurrentDirContent()
      if (content) {
        const items = Object.values(content)
        output = items.map(item => {
          const color = item.type === 'directory' ? '\x1b[34m' :
                       item.type === 'executable' ? '\x1b[32m' : '\x1b[0m'
          return `${color}${item.name}\x1b[0m`
        }).join('  ')
      }
      break

    case 'pwd':
      output = `/home/user${currentDir.value === '~' ? '' : '/' + currentDir.value.replace('~', '')}`
      break

    case 'cd':
      const target = args[0] || '~'
      if (target === '~' || target === '/') {
        currentDir.value = '~'
      } else if (target === '..') {
        const parts = currentDir.value.split('/').filter(p => p)
        if (parts.length > 1) {
          parts.pop()
          currentDir.value = parts.join('/')
        } else {
          currentDir.value = '~'
        }
      } else {
        const currentContent = getCurrentDirContent()
        const dirName = target.replace(/\/$/, '')
        if (currentContent?.[dirName]?.type === 'directory') {
          currentDir.value = currentDir.value === '~' ? `~/${dirName}` : `${currentDir.value}/${dirName}`
        } else {
          output = `cd: 不是目录: ${target}`
          isError = true
        }
      }
      break

    case 'cat':
      if (!args[0]) {
        output = 'cat: 缺少文件参数'
        isError = true
      } else {
        const currentContent = getCurrentDirContent()
        const file = currentContent?.[args[0]]
        if (!file) {
          output = `cat: ${args[0]}: 没有那个文件或目录`
          isError = true
        } else if (file.type === 'directory') {
          output = `cat: ${args[0]}: 是一个目录`
          isError = true
        } else {
          const fileContents: Record<string, string> = {
            'readme.txt': '欢迎使用 Terminal Simulator!\n这是一个交互式终端模拟器。',
            '.bashrc': '#!/bin/bash\nexport PATH="$HOME/bin:$PATH"',
            'settings.json': '{\n  "theme": "dark",\n  "fontSize": 14\n}',
            'app.js': 'console.log("Hello World!");',
            'server.ts': 'import { serve } from "https://deno.land/std/http/server.ts";',
            'hello.py': '#!/usr/bin/env python3\nprint("Hello, World!")'
          }
          output = fileContents[file.name] || `[${file.name} 的内容]`
        }
      }
      break

    case 'echo':
      output = args.join(' ')
      break

    case 'whoami':
      output = 'user'
      break

    case 'date':
      output = new Date().toLocaleString('zh-CN')
      break

    case 'clear':
      history.value = []
      input.value = ''
      return

    default:
      output = `命令未找到: ${command}\n输入 'help' 查看可用命令`
      isError = true
  }

  history.value.push({ command: cmd, output, isError })
  input.value = ''
  showSuggestions.value = false
}

// 处理提交
const handleSubmit = () => {
  executeCommand()
}

// 滚动到底部
watch(history, () => {
  nextTick(() => {
    terminalBody.value?.scrollTo(0, terminalBody.value.scrollHeight)
  })
}, { deep: true })

// 解析 ANSI 颜色代码
const parseAnsi = (text: string): string => {
  return text
    .replace(/\x1b\[0m/g, '</span>')
    .replace(/\x1b\[36m/g, '<span class="ansi-cyan">')
    .replace(/\x1b\[34m/g, '<span class="ansi-blue">')
    .replace(/\x1b\[32m/g, '<span class="ansi-green">')
    .replace(/\x1b\[33m/g, '<span class="ansi-yellow">')
    .replace(/\x1b\[31m/g, '<span class="ansi-red">')
}

onMounted(() => {
  inputRef.value?.focus()
})
</script>

<template>
  <div class="terminal-container">
    <div class="terminal">
      <div class="terminal-header">
        <span class="dot dot-red"></span>
        <span class="dot dot-yellow"></span>
        <span class="dot dot-green"></span>
        <span class="terminal-title">bash — Terminal Simulator</span>
      </div>

      <div class="terminal-body" ref="terminalBody">
        <div class="welcome-msg">
          <span class="ansi-green">✓</span> Terminal Simulator 已启动<br>
          输入 <span class="ansi-cyan">help</span> 查看可用命令，按 <span class="ansi-yellow">Tab</span> 键自动补全
        </div>

        <div v-for="(item, index) in history" :key="index" class="history-item">
          <div class="command-line">
            <span class="prompt">➜</span>
            <span class="path">{{ item.command.startsWith('cd ') && item.command.split(' ')[1] && !item.isError ?
              (currentDir === '~' ? '~' : currentDir.replace('~/', '')) :
              (currentDir === '~' ? '~' : currentDir.replace('~/', '')) }}</span>
            <span class="command">{{ item.command }}</span>
          </div>
          <div v-if="item.output" class="output" :class="{ 'error': item.isError }"
               v-html="parseAnsi(item.output).replace(/\n/g, '<br>')"></div>
        </div>

        <div class="input-line">
          <span class="prompt">➜</span>
          <span class="path">{{ currentDir === '~' ? '~' : currentDir.replace('~/', '') }}</span>
          <input
            ref="inputRef"
            v-model="input"
            @keydown.enter="handleSubmit"
            @keydown.tab="handleTab"
            @keydown="handleKeydown"
            @input="updateSuggestions"
            type="text"
            class="terminal-input"
            spellcheck="false"
            autocomplete="off"
          />
        </div>

        <!-- 自动补全建议 -->
        <div v-if="showSuggestions" class="suggestions">
          <div
            v-for="(suggestion, idx) in suggestions"
            :key="suggestion"
            class="suggestion-item"
            :class="{ 'selected': idx === selectedSuggestion }"
            @click="applySuggestion(suggestion)"
          >
            {{ suggestion }}
          </div>
        </div>
      </div>
    </div>

    <div class="hint">
      💡 提示: 蓝色=文件夹, 绿色=可执行文件, 白色=普通文件 | Tab 补全 | ↑↓ 历史命令
    </div>
  </div>
</template>

<style scoped>
.terminal-container {
  width: 100%;
  font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, monospace;
}

.terminal {
  background: #1a1a2e;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.terminal-header {
  background: #0f3460;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.dot-red { background: #ff5f56; }
.dot-yellow { background: #ffbd2e; }
.dot-green { background: #27c93f; }

.terminal-title {
  color: #a0a0a0;
  font-size: 13px;
  margin-left: 10px;
}

.terminal-body {
  padding: 16px;
  min-height: 320px;
  max-height: 400px;
  overflow-y: auto;
  color: #e0e0e0;
  font-size: 14px;
  line-height: 1.6;
}

.welcome-msg {
  color: #888;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid #333;
}

.history-item {
  margin-bottom: 8px;
}

.command-line {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.prompt {
  color: #27c93f;
  font-weight: bold;
}

.path {
  color: #5fafd7;
}

.command {
  color: #e0e0e0;
}

.output {
  color: #e0e0e0;
  margin-top: 4px;
  margin-left: 20px;
  white-space: pre-wrap;
  word-break: break-all;
}

.output.error {
  color: #ff6b6b;
}

.input-line {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 8px;
  position: relative;
}

.terminal-input {
  background: transparent;
  border: none;
  color: #e0e0e0;
  font-family: inherit;
  font-size: 14px;
  flex: 1;
  outline: none;
  min-width: 50px;
  caret-color: #27c93f;
}

/* ANSI Colors */
:deep(.ansi-cyan) { color: #5fafd7; }
:deep(.ansi-blue) { color: #5f87d7; }
:deep(.ansi-green) { color: #27c93f; }
:deep(.ansi-yellow) { color: #ffbd2e; }
:deep(.ansi-red) { color: #ff5f56; }

/* Suggestions */
.suggestions {
  background: #16213e;
  border: 1px solid #0f3460;
  border-radius: 6px;
  margin-top: 8px;
  padding: 4px 0;
  max-height: 150px;
  overflow-y: auto;
}

.suggestion-item {
  padding: 6px 12px;
  cursor: pointer;
  color: #e0e0e0;
  transition: background 0.2s;
}

.suggestion-item:hover,
.suggestion-item.selected {
  background: #0f3460;
}

/* Hint */
.hint {
  text-align: center;
  color: #888;
  font-size: 12px;
  margin-top: 12px;
  padding: 8px;
  background: rgba(15, 52, 96, 0.3);
  border-radius: 6px;
}

/* Scrollbar */
.terminal-body::-webkit-scrollbar {
  width: 8px;
}

.terminal-body::-webkit-scrollbar-track {
  background: #1a1a2e;
}

.terminal-body::-webkit-scrollbar-thumb {
  background: #0f3460;
  border-radius: 4px;
}

.terminal-body::-webkit-scrollbar-thumb:hover {
  background: #1a4a7a;
}
</style>
