---
title: "1.7 Tạo dự án"
description: "Từ quy tắc đặt tên thư mục đến tạo mẫu dự án"
chapter: "Chương 1"
---

# 1.7 Tạo dự án

> **Đọc xong phần này, bạn sẽ thu hoạch được:**
>
> - Nắm vững quy tắc đặt tên thư mục, tránh các vấn đề phát triển do đường dẫn tiếng Trung (hoặc có dấu)
> - Học cách sử dụng công cụ tạo dự án (scaffold) chính thức để nhanh chóng tạo cấu trúc dự án chuẩn
> - Hiểu cấu trúc thư mục của dự án Next.js

Sai lầm dễ mắc phải nhất của người mới là: Nhận được code do AI sinh ra, rồi tạo thủ công từng file một. Cách làm đúng là sử dụng mẫu dự án, để AI thông qua lệnh tạo dự án giúp bạn tạo ra cấu trúc chuẩn.

## Công tác chuẩn bị

### Tạo thư mục dự án

Trước khi tạo dự án, hãy tạo một thư mục với **đường dẫn tiếng Anh** trong trình quản lý tệp.

**Quan trọng**: Mỗi cấp trong đường dẫn đầy đủ đều không được có tiếng Trung (tiếng Việt có dấu) hoặc dấu cách.

| Ví dụ sai                      | Nguyên nhân                               |
| ------------------------------ | ----------------------------------------- |
| `C:/Users/Trương Tam/projects` | Tên người dùng là tiếng Việt/Trung/có dấu |
| `C:/Users/Li/my project`       | Tên thư mục có dấu cách                   |

| Ví dụ đúng                   | Giải thích                     |
| ---------------------------- | ------------------------------ |
| `C:/Users/YourName/projects` | Toàn tiếng Anh, không dấu cách |
| `/Users/yourname/projects`   | Thư mục người dùng macOS       |

**Cấu trúc thư mục đề xuất**:

```
my-projects/          ← Thư mục tổng
├── my-first-app/     ← Dự án 1
├── blog-app/         ← Dự án 2
└── store-app/        ← Dự án 3
```

### Mở Terminal trong thư mục

Sau khi tạo xong thư mục, cần mở terminal tại đó để thực thi lệnh.

| Hệ thống           | Thao tác                                                                        |
| ------------------ | ------------------------------------------------------------------------------- |
| **Windows**        | Chuột phải vào chỗ trống trong thư mục → "Open in Terminal" (Mở trong Terminal) |
| **Windows bản cũ** | Giữ `Shift + Chuột phải` → "Open PowerShell window here"                        |
| **Mac**            | Finder → Services → New Terminal at Folder                                      |
| **IDE**            | Cursor/VS Code/Trae: File → Open Folder, terminal tích hợp sẽ tự động định vị   |

### Đường dẫn tệp là gì

Đường dẫn tệp là vị trí của tệp trong hệ thống tệp. Khi bảo AI "sửa src/app/page.tsx", AI cần thông qua đường dẫn để tìm tệp này.

**Đường dẫn tuyệt đối**: Đường dẫn đầy đủ bắt đầu từ thư mục gốc

```
Windows:  C:\Users\YourName\projects\my-app\package.json
macOS:    /Users/yourname/projects/my-app/package.json
```

**Đường dẫn tương đối**: Đường dẫn bắt đầu từ thư mục hiện tại

```
./package.json        # package.json nằm trong thư mục hiện tại
../other-project      # other-project nằm ở thư mục cấp cha
src/app/page.tsx      # src/app/page.tsx nằm trong thư mục hiện tại
```

## Quy tắc đặt tên

Công cụ phát triển hỗ trợ không tốt cho đường dẫn tiếng Trung/Việt có dấu, dễ dẫn đến đủ loại báo lỗi kỳ lạ.

| Ví dụ đúng     | Ví dụ sai                          |
| -------------- | ---------------------------------- |
| `my-project`   | `Dự án của tôi`、`my project`      |
| `user-profile` | `user profile`、`hồ sơ người dùng` |
| `app.tsx`      | `ứng dụng.tsx`、`app file.tsx`     |

**Quy tắc**:

- ✅ Sử dụng chữ cái tiếng Anh viết thường
- ✅ Sử dụng dấu gạch nối `-` để phân cách từ
- ❌ Tránh ký tự tiếng Trung/Việt, dấu cách, ký tự đặc biệt

::: tip Tại sao không được dùng tiếng Trung/Việt?

**Báo lỗi thường gặp**: `ENOENT: no such file or directory`, `MODULE_NOT_FOUND`

Đường dẫn tiếng Việt/Trung có thể dẫn đến vấn đề bảng mã (encoding), lỗi phân giải đường dẫn, vấn đề tương thích công cụ.

:::

## Tạo dự án

Các framework hiện đại đều cung cấp công cụ tạo dự án (scaffold) chính thức, chỉ cần một lệnh là tạo được dự án chuẩn.

```bash
# Tạo dự án Next.js (my-app là tên dự án, có thể sửa)
pnpm create next-app@latest my-app

# Tạo dự án Vite + React
pnpm create vite@latest my-app -- --template react
```

Khi tạo sẽ hỏi các tùy chọn cấu hình:

- **TypeScript**: Khuyên chọn Yes
- **ESLint**: Khuyên chọn Yes
- **Tailwind CSS**: Chọn tùy nhu cầu
- **src directory**: Khuyên chọn Yes (Code đặt trong thư mục src/, cấu trúc rõ ràng hơn)
- **App Router**: Khuyên chọn Yes

::: tip Không muốn nhớ lệnh?

Nếu không nhớ được lệnh, có thể sao chép trực tiếp lệnh mẫu trong giáo trình này. Nhưng lệnh rất đơn giản, khuyên bạn nên nhớ:

```bash
pnpm create next-app@latest my-app
```

:::

## Cấu trúc dự án Next.js

Sau khi tạo xong, bạn sẽ thấy cấu trúc như sau:

```
my-next-app/
├── src/
│   ├── app/                 # Trang và API
│   │   ├── page.tsx         # Trang chủ
│   │   ├── layout.tsx       # Bố cục toàn cục
│   │   └── api/             # Giao diện API
│   │
│   ├── components/          # UI Component
│   └── lib/                 # Hàm tiện ích
│
├── public/                  # Tài nguyên tĩnh (Ảnh, Font)
├── package.json             # Quản lý phụ thuộc
└── tsconfig.json            # Cấu hình TypeScript
```

**Hiểu đơn giản**:

- `src/app/` - Đặt file trang web và giao diện
- `src/components/` - Đặt các UI component có thể tái sử dụng
- `src/lib/` - Đặt các hàm công cụ/tiện ích
- `public/` - Đặt ảnh và tài nguyên tĩnh
- `package.json` - Quản lý thư viện
- `tsconfig.json` - Cấu hình TypeScript

::: tip Code đặt ở đâu?

Khi AI bảo "tạo trang danh sách người dùng", hãy tạo `users/page.tsx` trong `src/app/`.

Khi AI bảo "tạo một component nút bấm", hãy tạo `Button.tsx` trong `src/components/`.

:::

## Cách tiện lợi hơn: Sử dụng /project-init

::: tip Sắp ra mắt

Giáo trình này cung cấp skill `/project-init`, có thể tự động hóa toàn bộ quy trình khởi tạo dự án.

**Nó làm được gì**:

1. **Kiểm tra môi trường**: Tự động kiểm tra phiên bản Node.js, pnpm đã cài chưa
2. **Đề xuất mẫu thông minh**: Dựa trên nhu cầu của bạn (PRD, bản thiết kế, ý tưởng chức năng) để đề xuất Tech Stack phù hợp
3. **Mẫu cài sẵn**:
   - Cấu hình đề xuất (Thuần Frontend)
   - SaaS Fullstack (Kèm Database, Xác thực, Thanh toán)
   - Trang tiếp thị/Landing Page
   - Trang quản trị/Dashboard
   - SPA nhẹ nhàng
4. **Kiểm tra tương thích**: Tự động xử lý phiên bản React, Tailwind v4, xung đột thư viện component...
5. **Cài đặt tự động**: Lệnh phi tương tác, một click tạo dự án

**Ví dụ sử dụng**:

> Dùng /project-init tạo một dự án SaaS cần đăng nhập người dùng và cơ sở dữ liệu

Nó sẽ hướng dẫn bạn hoàn thành kiểm tra môi trường, phân tích nhu cầu, chọn mẫu, cài đặt dependency, cấu hình biến môi trường... toàn bộ quy trình.

Sau khi giáo trình phát hành chính thức, sẽ cung cấp phương pháp cài đặt. Muốn tìm hiểu thêm về Skills, xem chi tiết [2.3 Hệ thống Skills](../02-ai-tuning-guide/03-mcp-and-skills_vi.md).

:::

## Khởi động dự án

```bash
# Vào thư mục dự án (my-app sửa thành tên dự án bạn đã tạo)
cd my-app

# Khởi động server phát triển
pnpm dev
```

Mở trình duyệt truy cập `http://localhost:3000`, thấy trang chào mừng là tạo thành công.

## Câu hỏi thường gặp

### Q: Tôi nên dùng mẫu nào?

| Loại dự án         | Mẫu đề xuất  |
| ------------------ | ------------ |
| Ứng dụng Fullstack | Next.js      |
| Frontend SPA       | Vite + React |
| Web tĩnh           | Astro        |

Giáo trình này sử dụng **Next.js + TypeScript + Tailwind CSS**, đây là giải pháp Fullstack phù hợp cho AI hỗ trợ phát triển.

### Q: Đã lỡ dùng đường dẫn tiếng Trung/Việt rồi thì sao?

Thao tác trong trình quản lý tệp:

1. Xóa thư mục `node_modules`
2. Tạo thư mục tiếng Anh mới
3. Sao chép các file còn lại sang thư mục mới
4. Chạy `pnpm install` trong thư mục mới

### Q: Có thể để AI tạo từng file một không?

Không khuyến khích. Để AI tạo từng file dễ bị sót, tốn thời gian, có thể cấu hình sai. **Cách làm đúng**: Dùng scaffold tạo dự án chuẩn trước, rồi để AI sửa trên cấu trúc có sẵn.

## Triết lý cốt lõi

**Sử dụng mẫu, thay vì bắt đầu từ con số 0**.

| Cách thức         | Kết quả                                           |
| ----------------- | ------------------------------------------------- |
| Tạo bằng scaffold | Cấu trúc chuẩn, cấu hình sẵn, một click khởi động |
| Tạo thủ công      | Dễ sót file, sai cấu hình, lãng phí thời gian     |

**Danh sách kiểm tra tạo dự án**:

- [ ] Tên dự án không chứa tiếng Trung/Việt và dấu cách
- [ ] Sử dụng scaffold chính thức
- [ ] Hiểu công dụng của từng thư mục
- [ ] Dự án khởi động bình thường

## Nội dung liên quan

- Xem chi tiết: [1.5 Môi trường Node.js và Quản lý gói](./05-nodejs-and-pnpm_vi.md)
- Xem chi tiết: [1.8 Localhost và Cổng](./08-localhost-and-ports_vi.md)
- Tiếp theo: [Chương 2 Hướng dẫn huấn luyện AI](../02-ai-tuning-guide/)
