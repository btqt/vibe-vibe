---
title: "4.8 Cấu trúc bản hướng dẫn dự án"
description: "Viết tài liệu README.md hoàn chỉnh cho dự án"
chapter: "Chương 4"
priority: "🟢"
---

# 4.8 Cấu trúc bản hướng dẫn dự án 🟢

> **Đọc xong phần này, bạn sẽ thu hoạch được:**
>
> - Hiểu giá trị và tác dụng của README.md
> - Nắm vững cấu trúc hoàn chỉnh của bản hướng dẫn dự án
> - Học cách viết tài liệu dự án rõ ràng
> - Hiểu tầm quan trọng của tài liệu trong việc cộng tác

> Code không chỉ để máy chạy, mà còn để người và AI đọc. README.md là "mặt tiền" và "hướng dẫn sử dụng" của dự án.

---

## Giá trị của README.md

README.md là ấn tượng đầu tiên về dự án, cũng là tài liệu quan trọng nhất. Một README xuất sắc sẽ giúp:

| Vai trò        | Nhận được gì                                                                |
| -------------- | --------------------------------------------------------------------------- |
| **Chính bạn**  | Không quên chi tiết dự án sau thời gian dài, khôi phục ngữ cảnh nhanh chóng |
| **Cộng sự**    | Hiểu nhanh dự án, bắt tay vào phát triển ngay                               |
| **AI**         | Có ngữ cảnh dự án toàn vẹn, sinh code chính xác hơn                         |
| **Người dùng** | Hiểu chức năng dự án, sử dụng sản phẩm đúng cách                            |

Viết README cũng là một bài luyện tập "ngoại hóa kiến thức". Khi cố gắng giải thích dự án bằng lời văn, bạn buộc phải chải chuốt lại những khái niệm mơ hồ và những giả định ngầm hiểu. Sự chải chuốt này không chỉ giúp người khác hiểu, mà còn giúp chính bạn có nhận thức rõ ràng hơn về dự án. Nhiều lập trình viên khi viết README mới phát hiện ra: Những quyết định thiết kế tưởng như "hiển nhiên" thực ra cần giải thích nhiều hơn; quy trình khởi động tưởng "đơn giản" thực ra có quá nhiều bước phụ thuộc. Những phát hiện này thường thúc đẩy bạn cải tiến chính dự án —— đơn giản hóa cấu hình, tối ưu cấu trúc, xóa bỏ sự nhập nhằng. Nhìn từ góc độ này, README không chỉ là tài liệu, mà còn là thước đo chất lượng dự án.

::: tip README là hướng dẫn sử dụng

Tưởng tượng bạn mua đồ điện tử về mà không có hướng dẫn sử dụng thì bối rối thế nào. Dự án cũng vậy, không có README, người khác (kể cả bạn của vài tháng sau) sẽ mù tịt.

:::

---

## Cấu trúc cốt lõi của README

Một dự án hoàn chỉnh cần có các phần sau trong README:

### 1. Giới thiệu dự án

Dùng một hai câu nói rõ dự án là gì, giải quyết vấn đề gì.

```markdown
# Danh sách việc cần làm tối giản

Một trang web To-do list tối giản cho cá nhân, hỗ trợ thêm, hoàn thành và xóa công việc.
```

### 2. Khởi động nhanh (Quick Start)

Chỉ dẫn người dùng cách chạy dự án nhanh nhất.

```markdown
## Khởi động nhanh

### Cài đặt dependency

\`\`\`bash
pnpm install
\`\`\`

### Chạy server phát triển

\`\`\`bash
pnpm dev
\`\`\`

Truy cập http://localhost:3000 để xem kết quả.
```

### 3. Biến môi trường

Liệt kê các biến môi trường dự án cần.

```markdown
## Biến môi trường

Sao chép `.env.example` thành `.env.local`, sau đó điền các biến sau:

\`\`\`bash

# Kết nối Database

DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# API Key

OPENAI_API_KEY=sk-xxx
\`\`\`
```

### 4. Chức năng cốt lõi

Giới thiệu các module chức năng chính của dự án.

```markdown
## Chức năng cốt lõi

- **Quản lý tác vụ**: Thêm, hoàn thành, xóa việc cần làm
- **Dữ liệu bền vững**: F5 không mất dữ liệu
- **Giao diện tối giản**: Tập trung trải nghiệm cốt lõi, không xao nhãng
```

### 5. Tech Stack

Liệt kê công nghệ sử dụng trong dự án.

```markdown
## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Ngôn ngữ**: TypeScript
- **Style**: Tailwind CSS
- **Database**: PostgreSQL + Drizzle ORM
- **Deploy**: Vercel
```

### 6. Cấu trúc dự án

Hiển thị sơ đồ thư mục dự án.

```markdown
## Cấu trúc dự án

\`\`\`
src/
├── app/ # Next.js App Router
│ ├── page.tsx # Trang chủ
│ ├── layout.tsx # Layout
│ └── api/ # API Routes
├── components/ # React Component
├── lib/ # Hàm tiện ích
└── db/ # Cấu hình Database
\`\`\`
```

### 7. Hướng dẫn phát triển

(Tùy chọn) Chỉ dẫn chi tiết cho developer.

```markdown
## Hướng dẫn phát triển

### Thêm tính năng mới

1. Tạo API Route mới trong `src/app/api/`
2. Tạo UI Component tương ứng trong `src/components/`
3. Cập nhật `src/app/page.tsx` để tích hợp tính năng mới

### Phong cách code

Dự án dùng ESLint và Prettier để đảm bảo đồng nhất style code:

\`\`\`bash
pnpm lint # Kiểm tra code
pnpm format # Format code
\`\`\`
```

### 8. Hướng dẫn đóng góp

(Tùy chọn) Cho người khác biết cách tham gia dự án.

```markdown
## Đóng góp

Chào mừng submit Issue và Pull Request!

1. Fork dự án này
2. Tạo nhánh tính năng (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'feat: Thêm tính năng gì đó'`)
4. Push lên nhánh (`git push origin feature/AmazingFeature`)
5. Mở Pull Request
```

### 9. Giấy phép (License)

Tuyên bố giấy phép mã nguồn mở của dự án.

```markdown
## Giấy phép

[MIT License](LICENSE)
```

---

## Mẫu README

Dưới đây là một mẫu README hoàn chỉnh:

```markdown
# [Tên dự án]

[Một câu mô tả dự án]

## Giới thiệu

[Mô tả chi tiết bối cảnh, mục tiêu và giá trị cốt lõi của dự án]

## Khởi động nhanh

### Yêu cầu môi trường

- Node.js 18+
- pnpm

### Cài đặt

\`\`\`bash
git clone https://github.com/username/repo.git
cd repo
pnpm install
\`\`\`

### Cấu hình

\`\`\`bash
cp .env.example .env.local

# Sửa .env.local điền cấu hình

\`\`\`

### Chạy

\`\`\`bash
pnpm dev # Chế độ phát triển
pnpm build # Build
pnpm start # Chạy production
\`\`\`

## Đặc tính chức năng

- Chức năng 1: Mô tả
- Chức năng 2: Mô tả
- Chức năng 3: Mô tả

## Tech Stack

- Công nghệ A
- Công nghệ B
- Công nghệ C

## Cấu trúc dự án

\`\`\`
Sơ đồ cây thư mục
\`\`\`

## Hướng dẫn phát triển

[Chỉ dẫn liên quan phát triển]

## Deploy

[Chỉ dẫn liên quan deploy]

## Câu hỏi thường gặp

### Q: Câu hỏi thường gặp 1?

A: Giải đáp

## Đóng góp

[Hướng dẫn đóng góp]

## Giấy phép

[Thông tin giấy phép]

## Lời cảm ơn

[Danh sách cảm ơn]

---

**Lưu ý**: Xin đừng commit file `.env.local` chứa thông tin nhạy cảm lên Git.
```

---

## README thân thiện với AI

Trong thời đại phát triển với sự hỗ trợ của AI, README con đảm nhận nhiệm vụ cung cấp ngữ cảnh cho AI.

### Thêm ngữ cảnh dự án

Thêm nội dung sau vào README sẽ giúp AI hiểu dự án tốt hơn:

```markdown
## Ngữ cảnh dự án cho AI

### Mục tiêu dự án

[Mô tả rõ ràng vấn đề dự án cần giải quyết]

### Khái niệm cốt lõi

[Giải thích các thuật ngữ và khái niệm quan trọng trong dự án]

### Quy ước quan trọng

[Liệt kê quy ước về style code, cách đặt tên...]

### Tác vụ thường gặp

[Liệt kê cách thao tác các tác vụ thường gặp, ví dụ "cách thêm trang mới"]
```

::: tip README là kho ngữ cảnh của AI

Khi bạn nhờ AI xử lý vấn đề dự án, việc cung cấp đầy đủ nội dung README giúp AI hiểu dự án chính xác hơn, sinh ra code phù hợp với phong cách dự án hơn.

:::

---

## Thực hành tốt nhất cho README

| Thực hành          | Giải thích                                            |
| ------------------ | ----------------------------------------------------- |
| **Giữ cập nhật**   | Code đổi thì tài liệu cũng phải đổi theo              |
| **Súc tích**       | Không viết lan man, đi thẳng vào trọng tâm            |
| **Code mẫu**       | Dùng khối code (code block) hiển thị lệnh và cấu hình |
| **Trực quan**      | Dùng emoji, bảng biểu, danh sách để tăng tính dễ đọc  |
| **Link hợp lệ**    | Kiểm tra tất cả link nội bộ và link ngoài             |
| **Badge huy hiệu** | Hiển thị trạng thái build, phiên bản...               |

### Ví dụ về Badge huy hiệu

```markdown
[![Build Status](https://img.shields.io/github/actions/workflow/status/username/repo/ci.yml)](https://github.com/username/repo/actions)
[![Version](https://img.shields.io/npm/v/package-name)](https://www.npmjs.com/package-name)
[![License](https://img.shields.io/npm/l/package-name)](LICENSE)
```

---

## Câu hỏi thường gặp

### Q1: README nên viết dài bao nhiêu?

Tùy quy mô dự án. Dự án nhỏ thì ngắn gọn, dự án lớn cần chi tiết. Nguyên tắc là: Để người mới vào có thể hiểu và chạy được dự án trong vòng 5 phút.

### Q2: Viết README bằng tiếng Việt được không?

Được. Nếu dự án chủ yếu hướng tới người dùng tiếng Việt thì viết tiếng Việt. Dự án quốc tế hóa thì nên dùng tiếng Anh.

### Q3: README khác gì tài liệu kỹ thuật?

README là "cổng vào" và "tổng quan" của dự án, tài liệu kỹ thuật là giải thích chi tiết về hiện thực. README nên súc tích, tài liệu kỹ thuật có thể tường tận.

### Q4: Nhờ AI viết README được không?

Đưa thông tin cơ bản của dự án cho AI, bảo nó sinh khung sườn, rồi người sửa lại chi tiết. Hoặc bảo AI dựa vào cấu trúc code hiện có để sinh bản nháp README.

---

## Trọng điểm cốt lõi

- ✅ README.md là mặt tiền và hướng dẫn sử dụng của dự án
- ✅ README hoàn chỉnh gồm: Giới thiệu, Khởi động nhanh, Biến môi trường, Chức năng, Tech Stack
- ✅ README tốt giúp cộng tác hiệu quả hơn, AI làm việc chính xác hơn
- ✅ Phải giữ README cập nhật đồng bộ với code
- ✅ Dùng code block, bảng biểu, danh sách để tăng khả năng đọc
- ✅ Thêm phần "Ngữ cảnh dự án cho AI" để nâng cao hiệu quả hỗ trợ của AI

Chương 4 hoàn thành! Tiếp theo sẽ tìm hiểu 3 trạng thái của code khi vận hành và nguyên lý build.

---

## Nội dung liên quan

- Trước đó: [4.2 Mối quan hệ giữa PRD và Tài liệu kỹ thuật](./02-prd-and-tech-docs_vi.md)
- Trước đó: [4.6 Định dạng file cấu hình](./06-config-formats_vi.md)
- Trước đó: [4.7 Thực chiến tích hợp API](./07-api-integration_vi.md)
- Chi tiết: [Chương 5: 3 trạng thái vận hành của code](../05-build-and-runtime-modes/index_vi.md)
