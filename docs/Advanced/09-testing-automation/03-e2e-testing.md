---
title: "9.3 E2E测试与问题定位"
description: "E2E测试陷阱、日志定位、Playwright简介"
---

# 9.3 E2E测试与问题定位

> **待开发**

---

E2E测试模拟真实用户操作，覆盖核心流程。但维护成本高，需谨慎使用。

**E2E测试的陷阱**

| 陷阱 | 表现 | 解决 |
|------|------|------|
| **Flaky测试** | 有时通过有时失败 | 添加稳定等待，避免固定延时 |
| **过度测试** | 测了太多边缘UI | 只测核心流程，细节用API测 |
| **数据依赖** | 测试数据被其他测试修改 | 每个测试独立准备数据 |
| **环境差异** | 本地通过CI失败 | 统一环境配置 |

**测试失败时怎么看日志**

```
❌ FAIL: 用户下单流程
   Error: Timeout waiting for element "[data-testid='pay-button']"
```

排查步骤：
1. **看错误类型**：Timeout（等待超时）vs Assertion（断言失败）
2. **看截图**：Playwright会自动保存失败截图
3. **看网络请求**：API是否返回错误
4. **看控制台**：前端是否有JS报错

**常见错误定位**

| 错误信息 | 可能原因 | 检查点 |
|---------|---------|--------|
| Timeout waiting... | 元素未加载 | 网络慢？选择器变了？ |
| Expected A but got B | 逻辑错误 | 数据是否正确？ |
| 500 Internal Server Error | 后端问题 | API日志 |

**Playwright简介（工具补充）**

Playwright是微软开源的E2E测试工具，特点：
- 跨浏览器（Chrome、Firefox、Safari）
- 自动等待元素出现
- 支持录制生成代码
- 可截图、录视频

安装使用：
```bash
npm init playwright@latest
npx playwright test      # 运行测试
npx playwright test --ui # 可视化模式
```

但记住：工具只是手段，测试策略才是核心。

---

::: tip 日志是排查的关键

测试失败时，先看错误信息，再看截图，最后看网络请求。三步定位问题。

:::
