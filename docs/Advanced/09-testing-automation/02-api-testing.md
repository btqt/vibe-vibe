---
title: "9.2 API测试"
description: "让AI生成API测试，覆盖正常和异常场景"
---

# 9.2 API测试

> **待开发**

---

API测试比UI测试更稳定，不受界面变化影响。优先测试API。

**为什么先测API**

| UI测试 | API测试 |
|--------|---------|
| 按钮位置一变就失效 | 接口契约稳定 |
| 加载慢导致失败 | 响应明确 |
| 维护成本高 | 维护成本低 |

**让AI生成API测试**

引用你的API文件夹，给AI下指令：

> "阅读`app/api`文件夹下的所有路由，为每个API生成测试：
> - 正常请求（200 OK）
> - 参数错误（400 Bad Request）
> - 未授权（401 Unauthorized）
> - 服务器错误（500 Internal Server Error）"

AI会遍历你的接口，自动生成测试代码。

**测试覆盖要点**

- **成功路径**：正常参数返回预期数据
- **参数校验**：缺少必填项、格式错误
- **权限控制**：未登录、无权限访问
- **边界情况**：空数组、超长字符串、特殊字符

**示例：用户注册接口**

```typescript
// 正常注册
POST /api/register
{ "email": "test@example.com", "password": "123456" }
// 期望：201 Created，返回用户ID

// 邮箱已存在
POST /api/register
{ "email": "existing@example.com", "password": "123456" }
// 期望：409 Conflict，错误提示"邮箱已注册"

// 密码太短
POST /api/register
{ "email": "test@example.com", "password": "123" }
// 期望：400 Bad Request，错误提示"密码至少6位"
```

---

::: tip 一个API至少3个测试

成功、失败、边界。覆盖这三种，API基本可靠。

:::
