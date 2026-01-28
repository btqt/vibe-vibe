<script setup lang="ts">
import { ref, computed, onMounted, nextTick, watch } from 'vue'

interface FileSystemItem {
  name: string
  type: 'file' | 'directory' | 'executable' | 'link'
  content?: string
  size?: number
  modified?: Date
  children?: Record<string, FileSystemItem>
  target?: string
}

interface CommandOutput {
  type: 'command' | 'output' | 'error' | 'system'
  content: string
  path?: string
  timestamp?: Date
}

// 文件系统
const fileSystem = ref<Record<string, FileSystemItem>>({
  '~': {
    name: '~',
    type: 'directory',
    modified: new Date('2024-01-15'),
    children: {
      'Documents': {
        name: 'Documents',
        type: 'directory',
        modified: new Date('2024-01-20'),
        children: {
          'projects': {
            name: 'projects',
            type: 'directory',
            modified: new Date('2024-01-25'),
            children: {
              'my-app': {
                name: 'my-app',
                type: 'directory',
                modified: new Date('2024-01-25'),
                children: {
                  'package.json': {
                    name: 'package.json',
                    type: 'file',
                    size: 856,
                    modified: new Date('2024-01-25'),
                    content: '{\n  "name": "my-app",\n  "version": "1.0.0",\n  "scripts": {\n    "dev": "next dev",\n    "build": "next build"\n  }\n}'
                  },
                  'src': {
                    name: 'src',
                    type: 'directory',
                    modified: new Date('2024-01-25'),
                    children: {
                      'app.tsx': { name: 'app.tsx', type: 'file', size: 234, modified: new Date('2024-01-25') },
                      'index.css': { name: 'index.css', type: 'file', size: 156, modified: new Date('2024-01-25') }
                    }
                  }
                }
              },
              'demo': {
                name: 'demo',
                type: 'directory',
                modified: new Date('2024-01-22'),
                children: {}
              }
            }
          },
          'readme.txt': {
            name: 'readme.txt',
            type: 'file',
            size: 128,
            modified: new Date('2024-01-18'),
            content: '欢迎使用 Terminal Pro!\n\n这是一个功能完整的终端模拟器。\n\n支持命令:\n- ls, pwd, cd, cat, echo\n- mkdir, touch, rm, cp, mv\n- tree, find, grep\n- history, clear, help'
          },
          'notes.md': {
            name: 'notes.md',
            type: 'file',
            size: 256,
            modified: new Date('2024-01-19'),
            content: '# 学习笔记\n\n## Vibe Coding\n\n- 用自然语言描述需求\n- AI 生成代码\n- 人工审核调整'
          }
        }
      },
      'Downloads': {
        name: 'Downloads',
        type: 'directory',
        modified: new Date('2024-01-23'),
        children: {
          'file.zip': { name: 'file.zip', type: 'file', size: 1024576, modified: new Date('2024-01-23') },
          'installer.run': { name: 'installer.run', type: 'executable', size: 5242880, modified: new Date('2024-01-23') }
        }
      },
      'Projects': {
        name: 'Projects',
        type: 'link',
        target: '~/Documents/projects',
        modified: new Date('2024-01-20')
      },
      '.config': {
        name: '.config',
        type: 'directory',
        modified: new Date('2024-01-16'),
        children: {
          'git': {
            name: 'git',
            type: 'directory',
            modified: new Date('2024-01-16'),
            children: {
              'config': { name: 'config', type: 'file', size: 89, modified: new Date('2024-01-16') }
            }
          }
        }
      },
      '.bashrc': {
        name: '.bashrc',
        type: 'file',
        size: 2048,
        modified: new Date('2024-01-10'),
        content: '#!/bin/bash\nexport PATH="$HOME/bin:$PATH"\nalias ll="ls -la"\nalias ..="cd .."'
      },
      'hello.py': {
        name: 'hello.py',
        type: 'executable',
        size: 45,
        modified: new Date('2024-01-12'),
        content: '#!/usr/bin/env python3\nprint("Hello, World!")'
      },
      'start.sh': {
        name: 'start.sh',
        type: 'executable',
        size: 128,
        modified: new Date('2024-01-15'),
        content: '#!/bin/bash\necho "Starting server..."\nnpm run dev'
      }
    }
  }
})

// 状态
const currentPath = ref('~')
const input = ref('')
const outputs = ref<CommandOutput[]>([])
const commandHistory = ref<string[]>([])
const historyIndex = ref(-1)
const suggestions = ref<string[]>([])
const selectedSuggestion = ref(-1)
const terminalRef = ref<HTMLElement | null>(null)
const inputRef = ref<HTMLInputElement | null>(null)

// 可用命令
const commands = [
  'help', 'ls', 'pwd', 'cd', 'cat', 'echo', 'clear',
  'mkdir', 'touch', 'rm', 'cp', 'mv', 'tree', 'find', 'grep',
  'history', 'whoami', 'date', 'uname', 'which'
]

// 格式化文件大小
function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes}B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)}K`
  return `${(bytes / (1024 * 1024)).toFixed(1)}M`
}

// 格式化日期
function formatDate(date: Date): string {
  return date.toLocaleDateString('zh-CN', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
}

// 获取当前目录内容
function getCurrentDir(): FileSystemItem | null {
  const parts = currentPath.value.split('/').filter(p => p)
  let current: FileSystemItem | undefined = fileSystem.value['~']

  for (const part of parts.slice(1)) {
    if (current?.type === 'link' && current.target) {
      current = resolvePath(current.target)
    }
    if (current?.children?.[part]) {
      current = current.children[part]
    } else {
      return null
    }
  }
  return current || null
}

// 解析路径
function resolvePath(path: string): FileSystemItem | null {
  if (path.startsWith('~/')) {
    path = path.replace('~', '')
  }
  const parts = path.split('/').filter(p => p)
  let current: FileSystemItem | undefined = fileSystem.value['~']

  for (const part of parts) {
    if (current?.children?.[part]) {
      current = current.children[part]
    } else {
      return null
    }
  }
  return current || null
}

// 获取路径显示
function getDisplayPath(): string {
  if (currentPath.value === '~') return '~'
  const parts = currentPath.value.split('/')
  return parts[parts.length - 1] || '~'
}

// 格式化历史路径
function formatHistoryPath(path: string | undefined): string {
  if (!path || path === '~') return '~'
  const parts = path.split('/')
  return parts[parts.length - 1] || '~'
}

// 计算补全建议（不自动显示，不区分大小写）
function calculateSuggestions() {
  const value = input.value.trim()
  // 处理多个连续空格，过滤空字符串
  const parts = value.split(' ').filter(p => p.length > 0)
  const cmd = parts[0]?.toLowerCase() || ''

  // 只有命令，没有参数（如 "cd"）- 不补全
  if (parts.length === 1) {
    suggestions.value = commands.filter(c => c.startsWith(cmd) && c !== cmd)
    selectedSuggestion.value = 0
    return suggestions.value.length > 0
  }

  // 有参数的命令补全
  if (['cd', 'ls', 'cat', 'touch', 'rm', 'mkdir', 'cp', 'mv'].includes(cmd)) {
    let arg = parts[parts.length - 1] || ''

    // 处理特殊路径
    if (arg === '..' || arg === '../') {
      suggestions.value = ['../']
      selectedSuggestion.value = 0
      return true
    }

    // 解析路径：检查是否有斜杠及斜杠后是否有内容
    const slashIndex = arg.indexOf('/')
    const hasSlash = slashIndex !== -1
    const hasSlashWithContent = hasSlash && slashIndex < arg.length - 1

    let searchDir = getCurrentDir()
    let searchPrefix = arg
    let basePath = ''

    if (hasSlash) {
      basePath = arg.substring(0, slashIndex + 1) // 包含斜杠
      const dirName = arg.substring(0, slashIndex)
      const subPrefix = arg.substring(slashIndex + 1)

      // 在当前目录查找基础路径对应的目录
      const currentDir = getCurrentDir()
      let targetItem = currentDir?.children?.[dirName]

      // 尝试大小写不敏感匹配
      if (!targetItem && currentDir?.children) {
        targetItem = Object.values(currentDir.children).find(
          item => item.name.toLowerCase() === dirName.toLowerCase()
        )
      }

      if (targetItem?.type === 'directory') {
        if (hasSlashWithContent) {
          // 斜杠后有内容：进入子目录并搜索前缀
          searchDir = targetItem
          searchPrefix = subPrefix
        } else {
          // 以斜杠结尾（如 Documents/）：提取原目录名的首字符作为搜索前缀
          // 这样可以在当前目录中循环所有匹配的项目
          searchPrefix = dirName.charAt(0)
        }
      }
    }

    if (!searchDir?.children) {
      suggestions.value = []
      return false
    }

    // 获取所有匹配的项目
    const allItems = Object.values(searchDir.children)
    let matchedItems = allItems

    if (searchPrefix) {
      matchedItems = allItems.filter(item =>
        item.name.toLowerCase().startsWith(searchPrefix.toLowerCase())
      )
    }

    // 排序：目录在前，文件在后
    matchedItems.sort((a, b) => {
      if (a.type === 'directory' && b.type !== 'directory') return -1
      if (a.type !== 'directory' && b.type === 'directory') return 1
      return a.name.localeCompare(b.name)
    })

    // 构建建议路径
    suggestions.value = matchedItems.map(item => {
      const itemName = item.name + (item.type === 'directory' ? '/' : '')
      if (hasSlashWithContent) {
        // 斜杠后有内容：保留完整路径前缀
        // 例如：cd Documents/p -> cd Documents/projects/
        return basePath + itemName
      }
      // 当输入如 "Documents/" 时（hasSlash=true, hasSlashWithContent=false）
      // 我们在当前目录搜索，直接返回项目名用于替换整个参数
      return itemName
    })

    selectedSuggestion.value = -1
    return suggestions.value.length > 0
  }

  suggestions.value = []
  selectedSuggestion.value = -1
  return false
}

// 输入时重新计算建议
function updateSuggestions() {
  calculateSuggestions()
}


// 执行命令
function executeCommand() {
  const cmd = input.value.trim()
  if (!cmd) return

  commandHistory.value.push(cmd)
  historyIndex.value = -1

  outputs.value.push({
    type: 'command',
    content: cmd,
    path: currentPath.value,
    timestamp: new Date()
  })

  const parts = cmd.split(' ').filter(p => p)
  const command = parts[0]
  const args = parts.slice(1)

  let result: string | null = null
  let isError = false

  switch (command) {
    case 'help':
      result = `\x1b[1;36mTerminal Pro\x1b[0m - 可用命令:

\x1b[1m文件操作:\x1b[0m
  \x1b[32mls\x1b[0m [选项] [路径]     列出目录内容
  \x1b[32mpwd\x1b[0m                显示当前路径
  \x1b[32mcd\x1b[0m <目录>           切换目录
  \x1b[32mcat\x1b[0m <文件>          查看文件内容
  \x1b[32mtouch\x1b[0m <文件>        创建空文件
  \x1b[32mmkdir\x1b[0m <目录>        创建目录
  \x1b[32mrm\x1b[0m <文件>           删除文件
  \x1b[32mcp\x1b[0m <源> <目标>      复制文件
  \x1b[32mmv\x1b[0m <源> <目标>      移动文件

\x1b[1m系统命令:\x1b[0m
  \x1b[32mecho\x1b[0m <文本>        输出文本
  \x1b[32mdate\x1b[0m                显示日期时间
  \x1b[32mwhoami\x1b[0m              显示当前用户
  \x1b[32muname\x1b[0m               显示系统信息
  \x1b[32mhistory\x1b[0m             显示命令历史
  \x1b[32mclear\x1b[0m               清屏

\x1b[1m快捷键:\x1b[0m
  \x1b[33mTab\x1b[0m         自动补全
  \x1b[33m↑/↓\x1b[0m        历史命令
  \x1b[33mCtrl+L\x1b[0m      清屏
  \x1b[33mCtrl+C\x1b[0m      取消输入`
      break

    case 'ls':
      const showAll = args.includes('-a') || args.includes('-la') || args.includes('-al')
      const longFormat = args.includes('-l') || args.includes('-la') || args.includes('-al')
      const path = args.find(a => !a.startsWith('-')) || '.'

      let targetDir = getCurrentDir()
      if (path !== '.') {
        targetDir = resolvePath(path.startsWith('/') ? path : `${currentPath.value}/${path}`)
      }

      if (!targetDir || targetDir.type !== 'directory') {
        result = `ls: 无法访问 '${path}': 没有那个文件或目录`
        isError = true
      } else {
        const items = Object.values(targetDir.children || {})
          .filter(item => showAll || !item.name.startsWith('.'))

        if (longFormat) {
          result = items.map(item => {
            const type = item.type === 'directory' ? 'd' : item.type === 'link' ? 'l' : '-'
            const perms = item.type === 'directory' ? 'rwxr-xr-x' : item.type === 'executable' ? 'rwxr-xr-x' : 'rw-r--r--'
            const size = item.size || 0
            const date = formatDate(item.modified || new Date())
            const name = formatFileName(item)
            return `${type}${perms} user user ${size.toString().padStart(8)} ${date} ${name}`
          }).join('\n')
        } else {
          result = items.map(item => formatFileName(item)).join('  ')
        }
      }
      break

    case 'pwd':
      result = `/home/user${currentPath.value === '~' ? '' : currentPath.value.replace('~', '')}`
      break

    case 'cd':
      const target = args[0] || '~'
      if (target === '~' || target === '/') {
        currentPath.value = '~'
      } else if (target === '..') {
        const parts = currentPath.value.split('/').filter(p => p)
        if (parts.length > 1) {
          parts.pop()
          currentPath.value = parts.join('/')
        } else {
          currentPath.value = '~'
        }
      } else if (target === '-') {
        // 返回上次目录 (简化实现)
        currentPath.value = '~'
      } else {
        // 处理嵌套路径如 Documents/projects
        const pathParts = target.split('/').filter(p => p)
        let currentDir = getCurrentDir()
        let newPath = currentPath.value
        let valid = true

        for (const part of pathParts) {
          if (!currentDir?.children) {
            valid = false
            break
          }

          let targetItem = currentDir.children[part]

          // 尝试大小写不敏感匹配
          if (!targetItem) {
            targetItem = Object.values(currentDir.children).find(
              item => item.name.toLowerCase() === part.toLowerCase()
            )
          }

          if (targetItem?.type === 'link' && targetItem.target) {
            targetItem = resolvePath(targetItem.target)
          }

          if (targetItem?.type === 'directory') {
            currentDir = targetItem
            newPath = newPath === '~' ? `~/${targetItem.name}` : `${newPath}/${targetItem.name}`
          } else {
            valid = false
            result = `bash: cd: ${target}: 不是目录`
            isError = true
            break
          }
        }

        if (valid) {
          currentPath.value = newPath
        }
      }
      break

    case 'cat':
      if (!args[0]) {
        result = 'cat: 缺少文件参数'
        isError = true
      } else {
        const currentDir = getCurrentDir()
        const file = currentDir?.children?.[args[0]]
        if (!file) {
          result = `cat: ${args[0]}: 没有那个文件或目录`
          isError = true
        } else if (file.type === 'directory') {
          result = `cat: ${args[0]}: 是一个目录`
          isError = true
        } else {
          result = file.content || `[${file.name} - 二进制文件]`
        }
      }
      break

    case 'touch':
      if (!args[0]) {
        result = 'touch: 缺少文件参数'
        isError = true
      } else {
        const currentDir = getCurrentDir()
        if (currentDir?.children) {
          currentDir.children[args[0]] = {
            name: args[0],
            type: 'file',
            size: 0,
            modified: new Date(),
            content: ''
          }
          result = ''
        }
      }
      break

    case 'mkdir':
      if (!args[0]) {
        result = 'mkdir: 缺少目录参数'
        isError = true
      } else {
        const currentDir = getCurrentDir()
        if (currentDir?.children) {
          currentDir.children[args[0]] = {
            name: args[0],
            type: 'directory',
            modified: new Date(),
            children: {}
          }
          result = ''
        }
      }
      break

    case 'rm':
      if (!args[0]) {
        result = 'rm: 缺少操作数'
        isError = true
      } else {
        const currentDir = getCurrentDir()
        if (currentDir?.children?.[args[0]]) {
          delete currentDir.children[args[0]]
          result = ''
        } else {
          result = `rm: 无法删除 '${args[0]}': 没有那个文件或目录`
          isError = true
        }
      }
      break

    case 'tree':
      const treeDir = args[0] ? resolvePath(args[0]) : getCurrentDir()
      if (!treeDir) {
        result = `tree: '${args[0]}': 没有那个文件或目录`
        isError = true
      } else {
        result = generateTree(treeDir, '', true)
      }
      break

    case 'echo':
      result = args.join(' ').replace(/["']/g, '')
      break

    case 'date':
      result = new Date().toLocaleString('zh-CN', {
        weekday: 'short',
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
      break

    case 'whoami':
      result = 'developer'
      break

    case 'uname':
      result = 'Darwin MacBook-Pro.local 23.0.0 arm64'
      break

    case 'history':
      result = commandHistory.value.map((cmd, i) => `${(i + 1).toString().padStart(4)}  ${cmd}`).join('\n')
      break

    case 'clear':
    case 'cls':
      outputs.value = []
      input.value = ''
      return

    case 'which':
      if (!args[0]) {
        result = 'which: 缺少参数'
        isError = true
      } else if (commands.includes(args[0])) {
        result = `/usr/bin/${args[0]}`
      } else {
        result = `which: no ${args[0]} in (/usr/local/bin:/usr/bin:/bin)`
        isError = true
      }
      break

    case 'grep':
      if (args.length < 2) {
        result = '用法: grep <模式> <文件>'
        isError = true
      } else {
        const pattern = args[0].replace(/["']/g, '')
        const filename = args[1]
        const currentDir = getCurrentDir()
        const file = currentDir?.children?.[filename]
        if (!file || file.type !== 'file') {
          result = `grep: ${filename}: 没有那个文件或目录`
          isError = true
        } else {
          const lines = (file.content || '').split('\n')
          const matches = lines.filter(line => line.includes(pattern))
          result = matches.map((line, i) => `\x1b[32m${i + 1}\x1b[0m:${line.replace(pattern, `\x1b[1;31m${pattern}\x1b[0m`)}`).join('\n') || '(无匹配)'
        }
      }
      break

    case 'find':
      result = 'find: 功能开发中，请使用 ls 和 tree'
      break

    case 'cp':
    case 'mv':
      result = `${command}: 功能开发中`
      break

    default:
      result = `\x1b[31m${command}: command not found\x1b[0m\n输入 'help' 查看可用命令`
      isError = true
  }

  if (result !== null) {
    outputs.value.push({
      type: isError ? 'error' : 'output',
      content: result,
      timestamp: new Date()
    })
  }

  input.value = ''
}

// 生成树形结构
function generateTree(item: FileSystemItem, prefix: string, isLast: boolean): string {
  const connector = isLast ? '└── ' : '├── '
  const name = formatFileName(item)
  let result = prefix + connector + name + '\n'

  if (item.type === 'directory' && item.children) {
    const children = Object.values(item.children)
    children.forEach((child, index) => {
      const childPrefix = prefix + (isLast ? '    ' : '│   ')
      result += generateTree(child, childPrefix, index === children.length - 1)
    })
  }

  return result
}

// 格式化文件名（带颜色）
function formatFileName(item: FileSystemItem): string {
  if (item.type === 'directory') {
    return `\x1b[1;34m${item.name}\x1b[0m`
  } else if (item.type === 'executable') {
    return `\x1b[1;32m${item.name}\x1b[0m`
  } else if (item.type === 'link') {
    return `\x1b[1;36m${item.name}\x1b[0m -> ${item.target}`
  }
  return item.name
}

// 解析 ANSI 颜色
function parseAnsi(text: string): string {
  return text
    .replace(/\x1b\[0m/g, '</span>')
    .replace(/\x1b\[1m/g, '<span class="ansi-bold">')
    .replace(/\x1b\[1;30m/g, '<span class="ansi-bright-black">')
    .replace(/\x1b\[1;31m/g, '<span class="ansi-bright-red">')
    .replace(/\x1b\[1;32m/g, '<span class="ansi-bright-green">')
    .replace(/\x1b\[1;33m/g, '<span class="ansi-bright-yellow">')
    .replace(/\x1b\[1;34m/g, '<span class="ansi-bright-blue">')
    .replace(/\x1b\[1;36m/g, '<span class="ansi-bright-cyan">')
    .replace(/\x1b\[31m/g, '<span class="ansi-red">')
    .replace(/\x1b\[32m/g, '<span class="ansi-green">')
    .replace(/\x1b\[33m/g, '<span class="ansi-yellow">')
    .replace(/\x1b\[34m/g, '<span class="ansi-blue">')
    .replace(/\x1b\[36m/g, '<span class="ansi-cyan">')
}

// 键盘处理
function handleKeydown(e: KeyboardEvent) {
  // Tab 补全 - 直接轮询，不显示弹出框
  if (e.key === 'Tab') {
    e.preventDefault()
    const value = input.value.trim()
    const parts = value.split(' ').filter(p => p.length > 0)

    // 只有命令没有参数（如 "cd"），不补全
    if (parts.length === 1 && ['cd', 'ls', 'cat', 'touch', 'rm', 'mkdir', 'cp', 'mv'].includes(parts[0].toLowerCase())) {
      return
    }

    // 计算建议
    calculateSuggestions()
    if (suggestions.value.length > 0) {
      // 获取当前参数
      const inputParts = input.value.split(' ').filter(p => p.length > 0)
      const currentArg = inputParts.length > 1 ? inputParts[inputParts.length - 1] : ''

      // 如果还没有开始轮询，找到当前输入的匹配位置，从下一个开始
      if (selectedSuggestion.value < 0) {
        // 查找当前输入的参数在建议列表中的位置
        const currentIndex = suggestions.value.findIndex(s =>
          s.toLowerCase() === currentArg.toLowerCase()
        )
        if (currentIndex >= 0) {
          // 找到了，从下一个开始
          selectedSuggestion.value = (currentIndex + 1) % suggestions.value.length
        } else {
          selectedSuggestion.value = 0
        }
      } else {
        selectedSuggestion.value = (selectedSuggestion.value + 1) % suggestions.value.length
      }
      // 直接应用建议
      const suggestion = suggestions.value[selectedSuggestion.value]
      if (inputParts.length === 1) {
        // 命令补全
        input.value = suggestion
      } else {
        // 参数补全：保留命令，替换参数部分
        const cmd = inputParts[0]
        // 保留原始输入中的空格数量
        const originalParts = input.value.split(' ')
        const spaceCount = originalParts.length - inputParts.length
        const spaces = ' '.repeat(Math.max(1, spaceCount + 1))
        input.value = cmd + spaces + suggestion
      }
    }
    return
  }

  // Ctrl+L 清屏
  if (e.key === 'l' && e.ctrlKey) {
    e.preventDefault()
    outputs.value = []
    return
  }

  // Ctrl+C 取消
  if (e.key === 'c' && e.ctrlKey) {
    e.preventDefault()
    input.value = ''
    outputs.value.push({
      type: 'output',
      content: '^C',
      timestamp: new Date()
    })
    return
  }

  // 历史命令
  if (e.key === 'ArrowUp') {
    e.preventDefault()
    if (historyIndex.value < commandHistory.value.length - 1) {
      historyIndex.value++
      input.value = commandHistory.value[commandHistory.value.length - 1 - historyIndex.value]
    }
  } else if (e.key === 'ArrowDown') {
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

// 滚动到底部
watch(outputs, async () => {
  await nextTick()
  if (terminalRef.value) {
    terminalRef.value.scrollTop = terminalRef.value.scrollHeight
  }
}, { deep: true, flush: 'post' })

// 组件挂载时聚焦输入框
onMounted(() => {
  inputRef.value?.focus()
})

// 点击终端聚焦
function focusInput() {
  inputRef.value?.focus()
}

// 处理终端区域点击
function handleBodyClick() {
  focusInput()
}
</script>

<template>
  <div class="terminal-pro">
    <div class="terminal-window">
      <!-- 标题栏 -->
      <div class="terminal-header">
        <div class="window-controls">
          <span class="control close"></span>
          <span class="control minimize"></span>
          <span class="control maximize"></span>
        </div>

        <div class="terminal-title">
          <svg class="terminal-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="4 17 10 11 4 5"></polyline>
            <line x1="12" y1="19" x2="20" y2="19"></line>
          </svg>
          developer@VibeVibe: {{ getDisplayPath() }}
        </div>

        <div class="terminal-actions">
          <button class="action-btn" @click="outputs = []" title="清屏">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="3 6 5 6 21 6"></polyline>
              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- 终端内容 -->
      <div class="terminal-body" ref="terminalRef" @click="handleBodyClick">
        <!-- 欢迎信息 -->
        <div v-if="outputs.length === 0" class="welcome">
          <div class="welcome-logo">⌘</div>
          <div class="welcome-title">Terminal Pro</div>
          <div class="welcome-subtitle">输入 <code>help</code> 查看可用命令</div>
          <div class="welcome-shortcuts">
            <span><kbd>Tab</kbd> 补全</span>
            <span><kbd>↑↓</kbd> 历史</span>
            <span><kbd>Ctrl+L</kbd> 清屏</span>
          </div>
        </div>

        <!-- 输出内容 -->
        <div v-for="(output, index) in outputs" :key="index" class="output-item">
          <template v-if="output.type === 'command'">
            <div class="command-line">
              <span class="prompt">
                <span class="prompt-user">developer</span>
                <span class="prompt-at">@</span>
                <span class="prompt-host">VibeVibe</span>
                <span class="prompt-sep">:</span>
                <span class="prompt-path">{{ formatHistoryPath(output.path) }}</span>
                <span class="prompt-sym">$</span>
              </span>
              <span class="command-text">{{ output.content }}</span>
            </div>
          </template>
          <template v-else>
            <pre class="output-content" :class="output.type" v-html="parseAnsi(output.content)"></pre>
          </template>
        </div>

        <!-- 输入行 -->
        <div class="input-line" @click="focusInput">
          <span class="prompt">
            <span class="prompt-user">developer</span>
            <span class="prompt-at">@</span>
            <span class="prompt-host">VibeVibe</span>
            <span class="prompt-sep">:</span>
            <span class="prompt-path">{{ getDisplayPath() }}</span>
            <span class="prompt-sym">$</span>
          </span>
          <div class="input-wrapper" @click.stop>
            <input
              ref="inputRef"
              v-model="input"
              @keydown.enter="executeCommand"
              @keydown="handleKeydown"
              @input="updateSuggestions"
              type="text"
              class="terminal-input"
              spellcheck="false"
              autocomplete="off"
              autocapitalize="off"
            />
          </div>
        </div>

      </div>

      <!-- 状态栏 -->
      <div class="terminal-status">
        <span class="status-item">bash</span>
        <span class="status-item">UTF-8</span>
        <span class="status-item">{{ outputs.filter(o => o.type === 'command').length }} 命令</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.terminal-pro {
  font-family: 'SF Mono', 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 13px;
  line-height: 1.5;
}

.terminal-window {
  background: #1e1e1e;
  border-radius: 10px;
  overflow: hidden;
  box-shadow:
    0 0 0 1px rgba(255, 255, 255, 0.1),
    0 20px 40px rgba(0, 0, 0, 0.4);
}

/* Header */
.terminal-header {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: linear-gradient(180deg, #3c3c3c 0%, #323232 100%);
  border-bottom: 1px solid #1a1a1a;
}

.window-controls {
  display: flex;
  gap: 8px;
}

.control {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  position: relative;
}

.control.close { background: #ff5f56; }
.control.minimize { background: #ffbd2e; }
.control.maximize { background: #27c93f; }

.terminal-title {
  flex: 1;
  text-align: center;
  color: #b0b0b0;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.terminal-icon {
  width: 14px;
  height: 14px;
  color: #666;
}

.terminal-actions {
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

/* Body */
.terminal-body {
  padding: 16px;
  min-height: 320px;
  max-height: 450px;
  overflow-y: auto;
  background: #1e1e1e;
  color: #f0f0f0;
  position: relative;
  cursor: text;
}

/* Welcome */
.welcome {
  text-align: center;
  padding: 40px 20px;
  color: #666;
}

.welcome-logo {
  font-size: 48px;
  color: #4a9eff;
  margin-bottom: 16px;
}

.welcome-title {
  font-size: 18px;
  font-weight: 600;
  color: #f0f0f0;
  margin-bottom: 8px;
}

.welcome-subtitle {
  font-size: 13px;
  margin-bottom: 20px;
}

.welcome-subtitle code {
  background: #333;
  padding: 2px 8px;
  border-radius: 4px;
  color: #4a9eff;
}

.welcome-shortcuts {
  display: flex;
  justify-content: center;
  gap: 20px;
  font-size: 12px;
}

.welcome-shortcuts span {
  display: flex;
  align-items: center;
  gap: 6px;
}

kbd {
  background: #333;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 11px;
  border: 1px solid #444;
}

/* Output */
.output-item {
  margin-bottom: 4px;
}

.command-line {
  display: flex;
  align-items: center;
  gap: 8px;
}

.prompt {
  white-space: nowrap;
  font-weight: 500;
}

.prompt-user { color: #4a9eff; }
.prompt-at { color: #666; }
.prompt-host { color: #50fa7b; }
.prompt-sep { color: #666; }
.prompt-path { color: #f1fa8c; }
.prompt-sym { color: #666; margin-left: 4px; }

.command-text {
  color: #f8f8f2;
}

.output-content {
  margin: 4px 0 8px 0;
  padding-left: 8px;
  white-space: pre-wrap;
  word-break: break-all;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}

.output-content.error {
  color: #ff5555;
}

/* Input */
.input-line {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 4px;
  cursor: text;
  padding: 4px 0;
  border-radius: 4px;
  transition: background 0.2s;
}

.input-line:hover {
  background: rgba(255, 255, 255, 0.02);
}

.input-wrapper {
  flex: 1;
  position: relative;
}

.terminal-input {
  width: 100%;
  background: transparent;
  border: none;
  color: #f8f8f2;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  outline: none;
  caret-color: #4a9eff;
}

.cursor {
  display: none;
}


/* Status Bar */
.terminal-status {
  display: flex;
  gap: 16px;
  padding: 6px 16px;
  background: #252526;
  border-top: 1px solid #333;
  font-size: 11px;
  color: #888;
}

/* ANSI Colors */
:deep(.ansi-bold) { font-weight: 600; }
:deep(.ansi-red) { color: #ff5555; }
:deep(.ansi-green) { color: #50fa7b; }
:deep(.ansi-yellow) { color: #f1fa8c; }
:deep(.ansi-blue) { color: #4a9eff; }
:deep(.ansi-cyan) { color: #8be9fd; }
:deep(.ansi-bright-red) { color: #ff6e6e; }
:deep(.ansi-bright-green) { color: #69ff94; }
:deep(.ansi-bright-yellow) { color: #ffffa5; }
:deep(.ansi-bright-blue) { color: #d6acff; }
:deep(.ansi-bright-cyan) { color: #a4ffff; }
:deep(.ansi-bright-black) { color: #6272a4; }

/* Scrollbar */
.terminal-body::-webkit-scrollbar {
  width: 10px;
}

.terminal-body::-webkit-scrollbar-track {
  background: #1e1e1e;
}

.terminal-body::-webkit-scrollbar-thumb {
  background: #424242;
  border-radius: 5px;
  border: 2px solid #1e1e1e;
}

.terminal-body::-webkit-scrollbar-thumb:hover {
  background: #4f4f4f;
}

/* Selection */
::selection {
  background: #4a9eff;
  color: #fff;
}
</style>
