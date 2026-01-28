<script setup lang="ts">
import { ref, computed } from 'vue'

interface NodeVersion {
  version: string
  status: 'current' | 'installed' | 'available'
  lts?: string
}

const versions = ref<NodeVersion[]>([
  { version: 'v24.12.0', status: 'current', lts: 'Krypton' },
  { version: 'v24.11.1', status: 'installed' },
  { version: 'v22.21.1', status: 'available', lts: 'Jod' },
  { version: 'v20.19.6', status: 'available', lts: 'Iron' },
  { version: 'v18.20.8', status: 'available', lts: 'Hydrogen' },
])

const activeTab = ref<'list' | 'install' | 'alias'>('list')
const installInput = ref('')
const output = ref<string[]>([
  'Node Version Manager (v0.40.0)',
  '',
  '常用命令:',
  '  nvm list          查看已安装版本',
  '  nvm use <version> 切换到指定版本',
  '  nvm install <ver> 安装新版本',
  '  nvm current       查看当前版本',
  '  nvm alias <name>  设置别名',
  '',
  '输入命令体验 nvm 操作...',
])

const currentVersion = computed(() =>
  versions.value.find(v => v.status === 'current')
)

function executeCommand() {
  const cmd = installInput.value.trim()
  if (!cmd) return

  output.value.push(`$ ${cmd}`)

  const parts = cmd.split(' ')
  const command = parts[0]
  const args = parts.slice(1)

  switch (command) {
    case 'nvm':
      handleNvmCommand(args)
      break
    case 'node':
      if (args[0] === '-v' || args[0] === '--version') {
        output.value.push(currentVersion.value?.version || 'v24.12.0')
      } else {
        output.value.push('Usage: node [options] [script]')
      }
      break
    default:
      output.value.push(`command not found: ${command}`)
      output.value.push('提示: 请使用 nvm 命令管理 Node 版本')
  }

  installInput.value = ''
}

function handleNvmCommand(args: string[]) {
  const subCmd = args[0]

  switch (subCmd) {
    case 'list':
    case 'ls':
      showVersionList()
      break

    case 'use':
      const versionToUse = args[1]
      if (!versionToUse) {
        output.value.push('Usage: nvm use <version>')
        return
      }
      useVersion(versionToUse)
      break

    case 'install':
      const versionToInstall = args[1]
      if (!versionToInstall) {
        output.value.push('Usage: nvm install <version>')
        output.value.push('示例: nvm install 22  或  nvm install v22.12.0')
        return
      }
      installVersion(versionToInstall)
      break

    case 'current':
      output.value.push(currentVersion.value?.version || 'v24.12.0')
      break

    case 'alias':
      if (args.length < 2) {
        output.value.push('Usage: nvm alias <name> [version]')
        output.value.push('示例: nvm alias default 22')
        return
      }
      setAlias(args[1], args[2])
      break

    case 'uninstall':
    case 'rm':
      const versionToRemove = args[1]
      if (!versionToRemove) {
        output.value.push('Usage: nvm uninstall <version>')
        return
      }
      uninstallVersion(versionToRemove)
      break

    case 'help':
    case '--help':
      showHelp()
      break

    default:
      output.value.push(`Unknown command: nvm ${subCmd}`)
      output.value.push('输入 "nvm help" 查看可用命令')
  }
}

function showVersionList() {
  output.value.push('')
  output.value.push('已安装版本:')
  versions.value.filter(v => v.status !== 'available').forEach(v => {
    const marker = v.status === 'current' ? '->' : '  '
    const lts = v.lts ? ` (LTS: ${v.lts})` : ''
    output.value.push(`${marker} ${v.version}${lts}`)
  })

  const available = versions.value.filter(v => v.status === 'available')
  if (available.length > 0) {
    output.value.push('')
    output.value.push('可安装版本 (远程):')
    available.forEach(v => {
      const lts = v.lts ? ` (LTS: ${v.lts})` : ''
      output.value.push(`   ${v.version}${lts}`)
    })
  }
  output.value.push('')
}

function useVersion(version: string) {
  const normalizedVersion = version.startsWith('v') ? version : `v${version}`

  // 检查是否已安装
  const target = versions.value.find(v =>
    v.version.startsWith(normalizedVersion) || v.version === normalizedVersion
  )

  if (!target) {
    output.value.push(`Version '${version}' not found.`)
    output.value.push('使用 "nvm list" 查看已安装版本')
    return
  }

  if (target.status === 'available') {
    output.value.push(`Version ${target.version} is not installed.`)
    output.value.push(`Run "nvm install ${version}" to install it first.`)
    return
  }

  // 切换版本
  versions.value = versions.value.map(v => ({
    ...v,
    status: v.version === target.version ? 'current' : v.status === 'current' ? 'installed' : v.status
  }))

  output.value.push(`Now using node ${target.version}`)
}

function installVersion(version: string) {
  const normalizedVersion = version.startsWith('v') ? version : `v${version}`

  // 查找匹配版本
  const target = versions.value.find(v =>
    v.version.startsWith(normalizedVersion) || v.version === normalizedVersion
  )

  if (!target) {
    output.value.push(`Version '${version}' not found in remote repository.`)
    return
  }

  if (target.status !== 'available') {
    output.value.push(`Version ${target.version} is already installed.`)
    output.value.push(`Use "nvm use ${version}" to switch to it.`)
    return
  }

  // 模拟安装
  output.value.push(`Downloading and installing node ${target.version}...`)

  setTimeout(() => {
    versions.value = versions.value.map(v =>
      v.version === target.version ? { ...v, status: 'installed' } : v
    )
    output.value.push(`Installed node ${target.version}`)
    output.value.push(`Use "nvm use ${version}" to switch to it.`)
  }, 800)
}

function uninstallVersion(version: string) {
  const normalizedVersion = version.startsWith('v') ? version : `v${version}`

  const target = versions.value.find(v => v.version === normalizedVersion)

  if (!target || target.status === 'available') {
    output.value.push(`Version '${version}' is not installed.`)
    return
  }

  if (target.status === 'current') {
    output.value.push(`Cannot uninstall currently-active node version ${target.version}`)
    output.value.push('Please switch to another version first.')
    return
  }

  versions.value = versions.value.map(v =>
    v.version === target.version ? { ...v, status: 'available' } : v
  )

  output.value.push(`Uninstalled node ${target.version}`)
}

function setAlias(name: string, version?: string) {
  if (!version) {
    output.value.push(`Alias '${name}' -> ${currentVersion.value?.version}`)
    return
  }

  output.value.push(`Set alias '${name}' -> ${version}`)
  output.value.push('Alias saved. You can use "nvm use ' + name + '" to switch.')
}

function showHelp() {
  output.value.push('')
  output.value.push('Node Version Manager')
  output.value.push('')
  output.value.push('Usage:')
  output.value.push('  nvm list              列出已安装版本')
  output.value.push('  nvm use <version>     切换到指定版本')
  output.value.push('  nvm install <version> 安装新版本')
  output.value.push('  nvm uninstall <ver>   卸载指定版本')
  output.value.push('  nvm current           显示当前版本')
  output.value.push('  nvm alias <name> [v]  设置别名')
  output.value.push('  nvm help              显示帮助')
  output.value.push('')
}

function quickUse(version: string) {
  installInput.value = `nvm use ${version}`
  executeCommand()
}

function quickInstall(version: string) {
  installInput.value = `nvm install ${version}`
  executeCommand()
}
</script>

<template>
  <div class="nvm-demo">
    <div class="nvm-window">
      <!-- 标题栏 -->
      <div class="nvm-header">
        <div class="window-controls">
          <span class="control close"></span>
          <span class="control minimize"></span>
          <span class="control maximize"></span>
        </div>
        <div class="nvm-title">
          <svg class="nvm-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 6v6l4 2"/>
          </svg>
          Terminal - nvm
        </div>
      </div>

      <!-- 当前版本显示 -->
      <div class="current-version-bar">
        <div class="version-info">
          <span class="version-label">当前 Node 版本</span>
          <span class="version-value">{{ currentVersion?.version }}</span>
          <span v-if="currentVersion?.lts" class="lts-badge">{{ currentVersion.lts }}</span>
        </div>
      </div>

      <!-- 终端输出区域 -->
      <div class="terminal-output">
        <div v-for="(line, index) in output" :key="index" class="output-line">
          <span v-if="line.startsWith('$')" class="prompt">$</span>
          <span :class="{ 'command-text': line.startsWith('$') }">{{ line }}</span>
        </div>
      </div>

      <!-- 命令输入 -->
      <div class="command-input-line">
        <span class="prompt">$</span>
        <input
          v-model="installInput"
          @keydown.enter="executeCommand"
          type="text"
          class="command-input"
          placeholder="输入 nvm 命令，如: nvm list, nvm use 22..."
          spellcheck="false"
          autocomplete="off"
        />
      </div>

      <!-- 快捷操作 -->
      <div class="quick-actions">
        <div class="quick-title">快捷操作</div>
        <div class="quick-buttons">
          <button
            v-for="v in versions.filter(x => x.status !== 'current')"
            :key="v.version"
            class="quick-btn"
            :class="v.status"
            @click="v.status === 'installed' ? quickUse(v.version.replace('v', '')) : quickInstall(v.version.replace('v', ''))"
          >
            <span class="btn-icon">{{ v.status === 'installed' ? '⚡' : '⬇️' }}</span>
            <span class="btn-text">{{ v.status === 'installed' ? 'use' : 'install' }} {{ v.version }}</span>
          </button>
        </div>
      </div>

      <!-- 命令提示 -->
      <div class="command-hints">
        <div class="hint-item">
          <code>nvm list</code>
          <span>查看版本</span>
        </div>
        <div class="hint-item">
          <code>nvm use 22</code>
          <span>切换版本</span>
        </div>
        <div class="hint-item">
          <code>nvm install 20</code>
          <span>安装版本</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.nvm-demo {
  font-family: 'SF Mono', Monaco, 'Courier New', monospace;
  margin: 20px 0;
}

.nvm-window {
  background: #1e1e2e;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

/* Header */
.nvm-header {
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

.nvm-title {
  flex: 1;
  text-align: center;
  color: #a0a0b0;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.nvm-icon {
  width: 14px;
  height: 14px;
  color: #68d391;
}

/* Current Version Bar */
.current-version-bar {
  padding: 16px 20px;
  background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
  border-bottom: 1px solid #2d2d44;
}

.version-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.version-label {
  font-size: 12px;
  color: #718096;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.version-value {
  font-size: 20px;
  font-weight: 600;
  color: #68d391;
}

.lts-badge {
  padding: 4px 10px;
  background: rgba(104, 211, 145, 0.2);
  color: #68d391;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 500;
}

/* Terminal Output */
.terminal-output {
  padding: 16px 20px;
  min-height: 200px;
  max-height: 280px;
  overflow-y: auto;
  background: #16162a;
}

.output-line {
  font-size: 13px;
  line-height: 1.6;
  color: #e2e8f0;
  white-space: pre-wrap;
  word-break: break-all;
}

.output-line .prompt {
  color: #68d391;
  margin-right: 8px;
  font-weight: 600;
}

.command-text {
  color: #63b3ed;
}

/* Command Input */
.command-input-line {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  background: #1e1e2e;
  border-top: 1px solid #2d2d44;
}

.command-input-line .prompt {
  color: #68d391;
  font-weight: 600;
  font-size: 14px;
}

.command-input {
  flex: 1;
  background: transparent;
  border: none;
  color: #e2e8f0;
  font-size: 14px;
  font-family: inherit;
  outline: none;
  caret-color: #68d391;
}

.command-input::placeholder {
  color: #4a5568;
}

/* Quick Actions */
.quick-actions {
  padding: 16px 20px;
  background: #1a1a2e;
  border-top: 1px solid #2d2d44;
}

.quick-title {
  font-size: 11px;
  color: #718096;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 12px;
}

.quick-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.quick-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  transition: all 0.2s;
}

.quick-btn.installed {
  background: rgba(99, 179, 237, 0.15);
  color: #63b3ed;
}

.quick-btn.installed:hover {
  background: rgba(99, 179, 237, 0.25);
}

.quick-btn.available {
  background: rgba(160, 174, 192, 0.15);
  color: #a0aec0;
}

.quick-btn.available:hover {
  background: rgba(160, 174, 192, 0.25);
}

.btn-icon {
  font-size: 12px;
}

/* Command Hints */
.command-hints {
  display: flex;
  gap: 16px;
  padding: 12px 20px;
  background: #16162a;
  border-top: 1px solid #2d2d44;
  flex-wrap: wrap;
}

.hint-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
}

.hint-item code {
  padding: 4px 8px;
  background: #2d3748;
  border-radius: 4px;
  color: #63b3ed;
  font-family: inherit;
}

.hint-item span {
  color: #718096;
}

/* Scrollbar */
.terminal-output::-webkit-scrollbar {
  width: 8px;
}

.terminal-output::-webkit-scrollbar-track {
  background: #16162a;
}

.terminal-output::-webkit-scrollbar-thumb {
  background: #2d3748;
  border-radius: 4px;
}

.terminal-output::-webkit-scrollbar-thumb:hover {
  background: #4a5568;
}
</style>
