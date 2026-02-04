---
title: "1.6 Mô hình và Công cụ"
description: "Hiểu sự khác biệt giữa mô hình và công cụ, lựa chọn tổ hợp phát triển AI Coding"
chapter: "Chương 1"
---

# 1.6 Mô hình và Công cụ

> **Đọc xong phần này, bạn sẽ thu hoạch được:**
>
> - Hiểu sự khác biệt giữa mô hình AI, công cụ CLI và công cụ IDE
> - Nắm vững phương pháp cài đặt và cấu hình Claude Code + GLM-4.7
> - Biết cách lựa chọn công cụ phù hợp dựa trên nhu cầu

Sau khi xây dựng xong môi trường, việc chọn tổ hợp mô hình và công cụ phù hợp sẽ giúp việc lập trình AI đạt hiệu quả gấp đôi.

## Khái niệm cơ bản

### Mô hình AI

**Mô hình AI** chịu trách nhiệm hiểu ý định và tạo nội dung. Ví dụ bạn hỏi "Làm sao viết chức năng đăng nhập", mô hình sẽ phân tích và trả về phương án code.

| Phân loại      | Sản phẩm tiêu biểu                                                                                                                                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Trung Quốc** | [GLM](https://open.bigmodel.cn/) (Zhipu), [DeepSeek](https://www.deepseek.com/), [Kimi](https://kimi.moonshot.cn/) (Moonshot), [Doubao](https://www.doubao.com/) (ByteDance), [MiniMax](https://www.minimaxi.com/) |
| **Quốc tế**    | [GPT](https://openai.com/) (OpenAI), [Gemini](https://gemini.google.com/) (Google), [Claude](https://claude.ai/) (Anthropic)                                                                                       |

**Công cụ** chịu trách nhiệm thực thi các thao tác cụ thể, ví dụ như đọc tệp, chạy lệnh, gửi code (commit). Công cụ cần kết nối với mô hình mới có thể hoạt động.

::: tip Chế độ hội thoại vs Luồng công cụ (Tool flow)

Bình thường bạn dùng AI, có thể là đang trò chuyện trong khung chat trên trang web:

| Chế độ hội thoại                              | Chế độ luồng công cụ                       |
| --------------------------------------------- | ------------------------------------------ |
| Chỉ có thể trò chuyện, không thể thao tác tệp | Có thể trực tiếp đọc ghi tệp dự án của bạn |
| Sao chép code về rồi tự dán                   | AI tự động sửa code                        |
| Tự chạy lệnh                                  | AI tự động chạy lệnh                       |
| Thích hợp để hỏi, học tập                     | Thích hợp để phát triển thực tế            |

**Công cụ lập trình AI = Bộ não AI + Tay chân**. Mô hình là bộ não, công cụ là tay chân. Chỉ có não mà không có tay chân, bạn chỉ có thể sao chép code; có tay chân rồi, AI mới có thể thực sự giúp bạn làm việc.

:::

| Loại            | Sản phẩm tiêu biểu     | Đặc điểm                                    |
| --------------- | ---------------------- | ------------------------------------------- |
| **Công cụ CLI** | Claude Code            | Chạy trên dòng lệnh, không giao diện đồ họa |
| **Công cụ IDE** | Cursor, Windsurf, Trae | Giao diện đồ họa, thao tác trực quan        |

::: tip Chọn công cụ CLI hay IDE?

|                      | Công cụ CLI                                   | Công cụ IDE                                 |
| -------------------- | --------------------------------------------- | ------------------------------------------- |
| **Cách tương tác**   | Đọc thoại văn bản dòng lệnh                   | Giao diện đồ họa + Hội thoại                |
| **Trải nghiệm**      | Ngắn gọn tập trung, không nhiễu               | Trực quan, dễ nhìn                          |
| **Tính linh hoạt**   | Cao, dễ tích hợp script                       | Trung bình, bị giới hạn bởi giao diện       |
| **Ngữ cảnh áp dụng** | Giáo trình này khuyến nghị, phát triển server | Lập trình viên thích GUI (Giao diện đồ họa) |

**Năng lực cốt lõi như nhau**: Cả hai đều có thể trực tiếp thao tác tệp dự án, chạy lệnh, thao tác Git. Giáo trình này khuyến nghị công cụ CLI (như Claude Code), vì nó tinh gọn, mạnh mẽ, và phù hợp hơn để học bản chất của lập trình AI.

:::

::: tip Kết hợp sử dụng: Thực hành tốt nhất

**Mở terminal trong IDE, chạy công cụ CLI** —— Đây là cấu hình ưu tiên của nhiều lập trình viên:

- Bên trái là trình biên tập như VS Code/Trae, tiện để duyệt và xem tệp
- Terminal bên dưới chạy công cụ CLI như Claude Code, để nó giúp bạn sửa code
- Vừa xem cấu trúc tệp, vừa sai bảo công cụ CLI làm việc

Như vậy bạn có thể đồng thời tận hưởng sự tiện lợi trực quan của IDE và năng lực mạnh mẽ của công cụ CLI. Đương nhiên, gợi ý là luôn sử dụng cùng một mô hình AI để duy trì ngữ cảnh liền mạch.

:::

::: tip Mối quan hệ giữa IDE và VS Code

Đa số IDE AI được phát triển dựa trên **VS Code** (như Cursor, Windsurf, Trae), giao diện và thói quen thao tác nhất quán, plugin VS Code có thể dùng chung, chi phí học tập rất thấp.

:::

### Tổng quan công cụ chủ đạo

| Loại    | Hãng quốc tế                                                                                                                                                                                      | Hãng Trung Quốc                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **CLI** | [Claude Code](https://claude.com/product/claude-code), [Codex CLI](https://openai.com/), [Gemini CLI](https://gemini.google.com/), [Aider](https://aider.chat/), [OpenCode](https://opencode.ai/) | [Qoder CLI](https://qoder.com/), [iFlow CLI](https://iflow.cn/)                                      |
| **IDE** | [Cursor](https://cursor.com/), [Windsurf](https://windsurf.com/), [Zed](https://zed.dev/), [GitHub Copilot](https://github.com/features/copilot)                                                  | [Trae](https://www.trae.cn/), [Qoder](https://qoder.com/), [CodeBuddy](https://copilot.tencent.com/) |

::: tip Ưu thế của Claude Code

- **Công khai khả dụng**: Phát hành trên kho npm, không giới hạn khu vực
- **Hỗ trợ đa mô hình**: Có thể kết nối mô hình trong nước (GLM, DeepSeek...)
- **Quy trình làm việc mạnh mẽ**: Thao tác tệp, tìm kiếm code, tích hợp Git, cộng tác Agent con
- **Chi phí kiểm soát được**: Sử dụng API mô hình trong nước, giá thấp hơn nhiều so với Claude chính chủ

:::

## Cài đặt cấu hình: Claude Code + GLM-4.7

::: danger Bước 0: Cài đặt Git (Bắt buộc)

Không có Git, không thể quản lý phiên bản, không thể commit code. Công cụ lập trình AI dựa vào Git để theo dõi thay đổi code.

- **Windows**: https://registry.npmmirror.com/-/binary/git-for-windows/v2.52.0.windows.1/Git-2.52.0-64-bit.exe
- **Mac**: Hệ thống có sẵn, hoặc `brew install git`
- **Linux**: `sudo apt install git`

Cài xong kiểm tra: `git --version`

:::

### Bước 1: Cài đặt Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### Bước 2: Mua gói coding

Truy cập [Nền tảng mở Zhipu AI](https://open.bigmodel.cn/), mua gói coding chính thức, lấy API Key.

::: tip API Key là gì

API Key là "giấy thông hành" để gọi dịch vụ mô hình lớn, là chứng nhận danh tính để bạn giao tiếp với máy chủ Zhipu AI.

:::

### Bước 3: Cấu hình tự động

```bash
npx @z_ai/coding-helper
# Nhập API Key đã lấy, công cụ sẽ tự động hoàn tất mọi cấu hình
```

### So sánh chi phí

| Hạng mục        | Claude chính chủ              | Gói coding GLM-4.7           |
| --------------- | ----------------------------- | ---------------------------- |
| Giá cả          | Khoảng ¥110/¥540 mỗi 1M Token | Khoảng 0.1% giá API          |
| Một lần gọi     | ~¥0.22                        | ~¥0.02                       |
| Môi trường mạng | Cần trung chuyển              | Kết nối trực tiếp trong nước |

**Kết luận**: Đối với phát triển hàng ngày, gói coding GLM-4.7 có hiệu suất chi phí cực cao.

## Công cụ phát triển khác

Những công cụ dưới đây **không bắt buộc**, cài đặt tùy nhu cầu:

| Loại công cụ      | Sản phẩm đề xuất           | Khi nào cần                  |
| ----------------- | -------------------------- | ---------------------------- |
| **Git GUI**       | GitHub Desktop, Sourcetree | Không quen lệnh Git          |
| **Cơ sở dữ liệu** | DBeaver, Drizzle Studio    | Thường xuyên xem/sửa dữ liệu |
| **Kiểm thử API**  | Postman, Thunder Client    | Debug giao diện API          |

::: tip Cấu hình tối thiểu

Claude Code + GLM-4.7 + Terminal hệ thống + Trình duyệt, là có thể bắt đầu phát triển.

:::

## Câu hỏi thường gặp

### Q: Có bắt buộc dùng trình biên tập AI không?

Có, đây là cốt lõi của giáo trình này. Triết lý Vibecoding được xây dựng trên nền tảng phát triển AI Native. Bạn có thể chọn bất kỳ IDE AI nào mình thích (Cursor/Windsurf/Trae...), hoặc sử dụng công cụ Claude Code CLI.

### Q: Cursor và VS Code khác gì nhau?

Cursor là bản VS Code tăng cường AI. VS Code cần cài plugin AI thủ công, Cursor thì tích hợp sâu năng lực AI. Nếu bạn đã quen VS Code, chuyển sang Cursor chi phí rất thấp.

## Triết lý cốt lõi

**Việc muốn làm tốt, trước tiên phải làm sắc công cụ**.

**Nguyên tắc chọn công cụ**:

1. **Ưu tiên AI Native**: Phát triển hiện đại không thể thiếu AI
2. **Cân nhắc đa nền tảng**: Công cụ dùng được trên cả Mac/Windows
3. **Chi phí học tập thấp**: Tránh công cụ quá phức tạp
4. **Cộng đồng sôi nổi**: Có tài liệu, có cập nhật

**Cấu hình tối thiểu**: Claude Code + GLM-4.7 + Terminal + Trình duyệt

## Nội dung liên quan

- Xem chi tiết: [Chương 2 Hướng dẫn huấn luyện AI](../02-ai-tuning-guide/)
- Xem chi tiết: [2.2 Giải thích quy trình VibeCoding](../02-ai-tuning-guide/02-vibecoding-workflow_vi.md)
- Trước đó: [1.4 Nhập môn Terminal](./04-terminal-basics_vi.md)
- Trước đó: [1.5 Môi trường Node.js và Quản lý gói](./05-nodejs-and-pnpm_vi.md)
