---
title: "15.3 Umami 统计部署"
description: "使用 1Panel 部署 Umami 统计系统"
chapter: "第十五章"
priority: "🟡"
---

# 15.3 Umami 统计部署 🟡

> **阅读完本节后，你将会收获：**
> - 理解网站统计的价值和作用
> - 掌握使用 1Panel 部署 Umami 的方法
> - 学会配置和使用 Umami 追踪数据
> - 了解隐私保护的重要性

> 上线不是结束，而是理解的开始。数据统计让你理解用户：他们从哪里来？用什么设备？哪些功能受欢迎？

---

## 为什么需要网站统计

网站统计回答产品运营的核心问题。

| 问题 | 统计数据 |
|------|---------|
| 有多少人访问？ | 页面浏览量、独立访客 |
| 他们从哪里来？ | 来源网站、搜索关键词 |
| 用什么设备？ | 设备类型、操作系统、浏览器 |
| 哪些页面受欢迎？ | 页面浏览排行 |
| 用户停留多久？ | 会话时长、跳出率 |

::: tip 数据与反馈的结合

数据告诉你"发生了什么"，用户反馈告诉你"为什么发生"。两者结合才能做出更好的决策。

:::

---

## Umami 简介

**Umami** 是一个开源、注重隐私的网站分析工具。

| 特性 | 说明 |
|------|------|
| **开源** | 代码公开，可自部署 |
| **隐私友好** | 不使用 Cookie，符合 GDPR |
| **轻量** | 脚本小于 1KB |
| **简洁** | 界面简洁，易于使用 |
| **免费** | 自部署无额外费用 |

### Umami vs Google Analytics

| 对比 | Umami | Google Analytics |
|------|-------|------------------|
| 部署方式 | 自托管 | 云服务 |
| 隐私 | 不追踪个人身份 | 详细用户追踪 |
| 脚本大小 | < 1KB | ~45KB |
| 界面 | 简洁 | 功能复杂 |
| 数据所有权 | 完全控制 | 归 Google |
| 学习曲线 | 低 | 高 |

---

## 1Panel 部署 Umami

如果已完成第十四章的 VPS 和 1Panel 设置，部署 Umami 只需几分钟。

### 部署步骤

1. **登录 1Panel**

   访问 `https://your-server-ip:端口`，登录管理面板。

2. **进入应用商店**

   在左侧菜单选择"应用商店"，搜索"Umami"。

3. **安装 Umami**

   点击安装，配置基本参数：
   - 应用名称：umami
   - 容器名称：umami
   - 端口：3001（或自定义）

4. **配置数据库**

   Umami 需要 PostgreSQL 数据库：
   - 可以使用 1Panel 的数据库服务创建
   - 或使用外部数据库

5. **完成安装**

   等待容器启动，访问 `http://your-server:3001`。

### 初次登录

默认登录信息：
- 用户名：admin
- 密码：umami

**重要**：登录后立即修改密码！

---

## Umami 配置

### 创建网站

登录后添加第一个网站：

1. 点击"Settings" → "Websites"
2. 点击"Add website"
3. 填写信息：
   - Name：网站名称
   - Domain：网站域名（如 `example.com`）
4. 点击保存

### 获取追踪代码

添加网站后会显示追踪代码：

```html
<script
  defer
  src="https://your-umami-url/script.js"
  data-website-id="your-website-id"
></script>
```

### 集成到 Next.js

在 Next.js 项目中集成追踪代码：

```typescript
// app/layout.tsx
import Script from 'next/script';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN">
      <head>
        <Script
          defer
          src="https://your-umami-url/script.js"
          data-website-id="your-website-id"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

或使用环境变量：

```typescript
<Script
  defer
  src={process.env.NEXT_PUBLIC_UMAMI_URL}
  data-website-id={process.env.NEXT_PUBLIC_UMAMI_ID}
/>
```

---

## 核心指标解读

Umami 仪表板显示以下核心指标。

### 访问指标

| 指标 | 说明 |
|------|------|
| **Pageviews** | 页面浏览总量 |
| **Unique Visitors** | 独立访客数 |
| **Visits** | 访问次数（会话） |
| **Bounce Rate** | 跳出率（单页面访问比例） |

### 流量来源

| 来源 | 说明 |
|------|------|
| **Search** | 搜索引擎 |
| **Social** | 社交媒体 |
| **Direct** | 直接访问 |
| **Referral** | 其他网站链接 |

### 设备信息

| 指标 | 说明 |
|------|------|
| **Browser** | 浏览器类型 |
| **OS** | 操作系统 |
| **Device** | 设备类型（桌面/移动） |
| **Screen** | 屏幕分辨率 |

---

## 事件追踪

除页面浏览外，还可以追踪自定义事件。

### 追踪按钮点击

```typescript
// 追踪分享按钮点击
import { umami } from '@umami/node';

umami.track('share', {
  platform: 'twitter',
  content: 'article-slug',
});
```

或使用原生方式：

```typescript
// 通用事件追踪
window.umami?.track('share', {
  platform: 'twitter',
  content: 'article-slug',
});
```

### 常见事件类型

| 事件 | 说明 |
|------|------|
| `signup` | 用户注册 |
| `login` | 用户登录 |
| `purchase` | 购买完成 |
| `download` | 文件下载 |
| `share` | 内容分享 |
| `cta_click` | CTA 按钮点击 |

---

## 主要指标 vs 虚荣指标

区分有意义的指标和无意义的指标。

| 主要指标 | 虚荣指标 |
|---------|---------|
| 留存率 | 总浏览量 |
| 转化率 | 访客总数 |
| 活跃用户 | 页面停留时长 |
| 收入 | 社交媒体粉丝数 |

::: tip 关注有行动价值的指标

选择能够指导行动的指标。如果看到一个数据后你不知道要做什么，那可能是虚荣指标。

:::

---

## 隐私保护

Umami 的设计注重隐私保护。

### GDPR 合规

Umami 不存储个人身份信息：
- 不使用 Cookie
- 不追踪个人用户
- 不收集可识别数据
- 数据完全控制

### 隐私设置

在 Umami 设置中可以：
- 启用 IP 哈希（部分匿名化）
- 设置数据保留期限
- 禁用某些追踪功能

---

## 常见问题

### Q1: Umami 和 Google Analytics 可以同时用吗？

可以，但没必要。选择一个即可，使用多个会增加页面加载负担。

### Q2: 数据多久更新？

实时数据延迟约 1-2 分钟。仪表板自动刷新。

### Q3: 如何导出数据？

Umami 支持数据导出功能。在设置中可以选择导出格式和日期范围。

### Q4: 多个网站怎么管理？

在 Umami 中添加多个网站，每个网站有独立的追踪代码和 ID。

---

## 本节核心要点

- ✅ 网站统计帮助理解用户行为
- ✅ Umami 是开源、隐私友好的统计工具
- ✅ 1Panel 可以一键部署 Umami
- ✅ 核心指标包括访问量、来源、设备
- ✅ 事件追踪可以监控用户行为
- ✅ 关注主要指标而非虚荣指标
- ✅ 隐私保护是现代统计工具的基本要求

统计部署完成后，接下来了解法律合规要求。

---

## 相关内容

- 前置：[第十四章 VPS 运维与部署](../14-vps-ops-deploy/index.md)
- 前置：[15.1 Open Graph 分享](./01-opengraph-sharing.md)
- 详见：[15.4 法律合规实践](./04-legal.md)
