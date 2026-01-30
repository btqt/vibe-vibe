---
title: "15.1 Open Graph 与社交分享"
description: "Open Graph 协议与社交平台优化"
chapter: "第十五章"
priority: "🔴"
---

# 15.1 Open Graph 与社交分享 🔴

> **阅读完本节后，你将会收获：**
> - 理解 Open Graph 协议的作用和原理
> - 掌握在 Next.js 中配置 OG 的方法
> - 学会设计有效的 OG 图片
> - 了解不同社交平台的优化策略
> - 掌握分享功能集成和数据追踪

> 把精心设计的网站链接分享到社交媒体，如果只显示一个蓝色链接，没有任何图片预览，点击率会非常低。Open Graph 协议就是解决这个问题的。

---

## 什么是 Open Graph

**Open Graph (OG)** 是 Facebook 推出的一种元数据协议，让网页在社交媒体上分享时能显示丰富的预览信息。

当你把链接分享到微信、Twitter、LinkedIn 等平台时，平台会抓取网页的 OG 标签来生成分享卡片。

### OG 标签的作用

| 有 OG 标签 | 无 OG 标签 |
|-----------|-----------|
| 精美的卡片预览 | 只有蓝色链接 |
| 标题、描述、图片 | 只有 URL |
| 高点击率 | 低点击率 |

::: tip 社交分享的重要性

社交分享是现代产品的重要流量来源。视觉吸引力直接决定点击率，第一印象影响用户决策。OG 优化不是可选项，是营销的基础设施。

:::

---

## Open Graph 基础标签

OG 协议定义了一组 `<meta>` 标签，放在 HTML 的 `<head>` 中：

### 核心 OG 标签

| 标签 | 说明 | 示例 |
|------|------|------|
| `og:title` | 分享卡片的标题 | "我的产品名称" |
| `og:description` | 分享卡片的描述 | "一句话说明产品价值" |
| `og:image` | 分享卡片的图片 URL | "https://..." |
| `og:url` | 页面的规范 URL | "https://..." |
| `og:type` | 内容类型 | "website" 或 "article" |

::: tip 让 AI 帮你配置

需要为 Next.js 项目配置 OG 标签？可以这样说：

> "帮我在 app/layout.tsx 中配置 metadata，添加 openGraph 设置，包括 title、description、url 和一张 1200x630 的图片。"

:::

---

## Next.js 中的 OG 配置

Next.js 提供了多种方式配置 OG 标签。

### 方法一：Metadata API

在 `layout.tsx` 或 `page.tsx` 中的 `metadata` 对象里配置 `openGraph` 字段。

### 方法二：OG 图片文件（推荐）

Next.js 支持通过放置特定文件名自动生成 OG 标签：

```
app/
├── opengraph-image.jpg      # 主 OG 图片
├── twitter-image.jpg        # Twitter 特定图片
└── (routes)/
    └── about/
        └── opengraph-image.jpg  # 特定页面 OG 图片
```

支持的文件名：
- `opengraph-image.{jpg,png,webp}`
- `twitter-image.{jpg,png,webp}`

::: tip 为什么推荐文件方式？

文件方式更直观，设计工具生成图片后直接放入即可。Next.js 会自动处理所有细节。

:::

### 方法三：动态生成 OG 图片

Next.js 可以用代码动态生成 OG 图片。使用 `next/og` 的 `ImageResponse`，在 `app/opengraph-image.tsx` 中返回包含标题和样式的 JSX。

::: tip 让 AI 帮你生成 OG 图片

需要动态生成带标题的 OG 图片？可以这样说：

> "帮我创建一个动态 OG 图片生成文件 app/opengraph-image.tsx，尺寸 1200x630，背景色白色，居中显示标题。使用 next/og 的 ImageResponse。"

:::

---

## 设计有效的 OG 图片

OG 图片是分享卡片的核心，好的设计能显著提升点击率。

### 推荐尺寸

| 平台 | 推荐尺寸 | 最低要求 |
|------|---------|---------|
| Facebook | 1200 x 630 | 600 x 315 |
| Twitter | 1200 x 675 | 600 x 335 |
| LinkedIn | 1200 x 627 | 1200 x 627 |

**通用推荐**：1200 x 630 像素，16:9 比例

### 设计原则

| 原则 | 说明 |
|------|------|
| **简洁明了** | 标题要短，突出核心信息 |
| **品牌一致** | 使用品牌色彩和字体 |
| **高质量** | 避免模糊、失真的图片 |
| **文字安全区** | 重要内容避开边缘（可能被裁剪） |
| **对比度** | 确保文字清晰可读 |

### 设计工具推荐

- Canva：有现成的 OG 图片模板
- Figma：专业设计工具
- Photoshop：传统设计软件
- 在线生成器：如 OG Image Generator

---

## 不同平台优化策略

各社交平台对 OG 的支持有差异，需要针对性优化。

### Twitter/X 卡片

Twitter 支持专门的 `twitter:card` 标签：

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@yourusername" />
<meta name="twitter:title" content="标题" />
<meta name="twitter:description" content="描述" />
<meta name="twitter:image" content="https://..." />
```

卡片类型：
- `summary`：小图卡片
- `summary_large_image`：大图卡片（推荐）
- `player`：视频播放器

### 微信分享优化

微信对 OG 支持有限，建议：
- 确保 `og:title` 和 `og:description` 完整
- 使用 HTTPS 图片
- 图片不要太小（建议 > 300KB）
- 考虑使用微信 JS-SDK 自定义分享内容

### LinkedIn 优化

LinkedIn 严格遵循 OG 标准，确保：
- `og:image` 尺寸正确（1200 x 627）
- 图片 URL 可公开访问
- 避免使用缓存破坏参数

---

## 分享功能集成

为网站添加社交分享按钮。

### 分享 URL 格式

| 平台 | 分享 URL |
|------|---------|
| Twitter | `https://twitter.com/intent/tweet?text=标题&url=URL` |
| Facebook | `https://www.facebook.com/sharer/sharer.php?u=URL` |
| LinkedIn | `https://www.linkedin.com/sharing/share-offsite/?url=URL` |
| 复制链接 | 使用 Clipboard API |

### React 分享组件

创建一个客户端组件，包含各平台的分享链接和复制链接功能。

分享 URL 格式：
- Twitter：`https://twitter.com/intent/tweet?text=标题&url=URL`
- Facebook：`https://www.facebook.com/sharer/sharer.php?u=URL`
- LinkedIn：`https://www.linkedin.com/sharing/share-offsite/?url=URL`

使用 `navigator.clipboard.writeText()` 复制链接到剪贴板。

::: tip 让 AI 帮你创建分享组件

需要社交分享按钮？可以这样说：

> "帮我创建一个 React 客户端组件 ShareButtons，接收 title 和 url 参数。包含 Twitter、Facebook、LinkedIn 三个分享链接（新窗口打开），和一个复制链接按钮。复制成功后显示'已复制！'，2秒后恢复。使用 Tailwind CSS 的 flex gap-4 布局。"

:::

### 动态 OG 更新

对于动态页面（如博客文章），使用 `generateMetadata` 函数，根据路由参数（如 `params.slug`）从数据库获取文章信息，动态设置 OG 标签。

::: tip 让 AI 帮你配置动态 OG

需要为博客文章配置动态 OG？可以这样说：

> "帮我在 app/blog/[slug]/page.tsx 中创建 generateMetadata 函数。从 `lib/posts.ts` 的 `getPost(slug)` 函数获取文章，返回包含 title、description、ogImage（文章封面图）的 metadata，openGraph 类型设为 'article'。"

:::

---

## 分享数据追踪

了解分享效果有助于优化策略。

### UTM 参数追踪

在分享 URL 中添加 UTM 参数来追踪来源：
- `utm_source`：来源平台（如 twitter）
- `utm_medium`：媒介类型（如 social）
- `utm_campaign`：活动名称

### Umami 事件追踪

使用 `window.umami.track('eventName', properties)` 追踪分享按钮点击事件。

---

## 测试和调试

配置完成后，需要测试分享效果。

### 测试工具

| 工具 | 链接 | 功能 |
|------|------|------|
| Facebook Debugger | developers.facebook.com/tools/debug/ | 验证 OG 标签 |
| Twitter Card Validator | cards-dev.twitter.com/validator | 验证 Twitter 卡片 |
| LinkedIn Post Inspector | linkedin.com/post-inspector/ | 验证 LinkedIn 预览 |

### 清除缓存

社交平台会缓存分享信息，更新 OG 后需要：
1. 使用调试工具的"Scrape Again"功能
2. 或在 URL 后加 `?v=2` 等参数强制刷新

---

## 常见问题

### Q1: OG 图片不显示怎么办？

检查：
1. 图片 URL 是否可公开访问
2. 图片格式是否正确（JPG/PNG）
3. 图片是否太大（建议 < 5MB）
4. 使用调试工具查看具体错误

### Q2: 不同页面可以用不同 OG 图片吗？

可以。为每个路由创建对应的 `opengraph-image.{jpg,png}` 文件，或在页面级 `page.tsx` 中覆盖 metadata。

### Q3: 微信分享为什么不显示图片？

微信有自己的机制，可能需要使用微信 JS-SDK 自定义分享内容，或确保图片尺寸足够大。

### Q4: 如何提高分享率？

1. 优化 OG 图片吸引力
2. 使用更吸引人的标题和描述
3. 让内容本身更有分享价值
4. 简化分享流程，一键完成

---

## 本节核心要点

- ✅ Open Graph 协议让网页分享时显示丰富的预览信息
- ✅ Next.js 支持 metadata API 和文件方式配置 OG
- ✅ OG 图片推荐尺寸是 1200 x 630
- ✅ 不同社交平台有特定的优化要求
- ✅ 分享按钮要简化流程，一键完成
- ✅ 使用 UTM 参数追踪分享效果

OG 优化完成后，接下来了解 SEO 基础配置。

---

## 相关内容

- 详见：[15.2 SEO 全攻略](./02-seo-guide.md)
- 前置：[第十四章 VPS 运维与部署](../14-vps-ops-deploy/index.md)
