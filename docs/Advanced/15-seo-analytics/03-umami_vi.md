---
title: "15.3 Triển khai thống kê Umami"
description: "Sử dụng 1Panel để triển khai hệ thống thống kê Umami"
chapter: "Chương 15"
priority: "🟡"
---

# 15.3 Triển khai thống kê Umami 🟡

> **Đọc xong phần này, bạn sẽ gặt hái được:**
>
> - Hiểu giá trị và tác dụng của thống kê trang web
> - Nắm vững phương pháp triển khai Umami bằng 1Panel
> - Học cách cấu hình và sử dụng Umami để theo dõi dữ liệu
> - Hiểu tầm quan trọng của việc bảo vệ quyền riêng tư

> Online không phải là kết thúc, mà là sự khởi đầu của sự thấu hiểu. Thống kê dữ liệu giúp bạn hiểu người dùng: Họ từ đâu đến? Dùng thiết bị gì? Tính năng nào được ưa chuộng?

---

## Tại sao cần thống kê trang web?

Thống kê trang web trả lời các câu hỏi cốt lõi của vận hành sản phẩm.

| Câu hỏi                      | Dữ liệu thống kê                         |
| ---------------------------- | ---------------------------------------- |
| Có bao nhiêu người truy cập? | Lượt xem trang, Khách truy cập duy nhất  |
| Họ từ đâu đến?               | Nguồn trang web, Từ khóa tìm kiếm        |
| Dùng thiết bị gì?            | Loại thiết bị, Hệ điều hành, Trình duyệt |
| Trang nào được ưa chuộng?    | Xếp hạng xem trang                       |
| Người dùng dừng lại bao lâu? | Thời lượng phiên, Tỷ lệ thoát            |

::: tip Sự kết hợp giữa dữ liệu và phản hồi

Dữ liệu cho bạn biết "chuyện gì đã xảy ra", phản hồi người dùng cho bạn biết "tại sao nó xảy ra". Kết hợp cả hai mới đưa ra được quyết định tốt hơn.

:::

---

## Giới thiệu Umami

**Umami** là công cụ phân tích trang web mã nguồn mở, chú trọng quyền riêng tư.

| Đặc tính                | Giải thích                           |
| ----------------------- | ------------------------------------ |
| **Mã nguồn mở**         | Code công khai, có thể tự triển khai |
| **Thân thiện riêng tư** | Không dùng Cookie, tuân thủ GDPR     |
| **Nhẹ**                 | Script nhỏ hơn 1KB                   |
| **Đơn giản**            | Giao diện tinh gọn, dễ sử dụng       |
| **Miễn phí**            | Tự triển khai không tốn thêm phí     |

### Umami vs Google Analytics

| So sánh              | Umami                            | Google Analytics             |
| -------------------- | -------------------------------- | ---------------------------- |
| Cách triển khai      | Tự lưu trữ (Self-host)           | Dịch vụ đám mây              |
| Quyền riêng tư       | Không theo dõi danh tính cá nhân | Theo dõi người dùng chi tiết |
| Kích thước script    | < 1KB                            | ~45KB                        |
| Giao diện            | Đơn giản                         | Chức năng phức tạp           |
| Quyền sở hữu dữ liệu | Kiểm soát hoàn toàn              | Thuộc về Google              |
| Đường cong học tập   | Thấp                             | Cao                          |

---

## Triển khai Umami bằng 1Panel

Nếu đã hoàn thành thiết lập VPS và 1Panel ở chương 14, triển khai Umami chỉ mất vài phút.

### Các bước triển khai

1. **Đăng nhập 1Panel**

   Truy cập `https://ip-server-cua-ban:port`, đăng nhập bảng quản trị.

2. **Vào Cửa hàng ứng dụng**

   Chọn "App Store" ở menu bên trái, tìm kiếm "Umami".

3. **Cài đặt Umami**

   Bấm cài đặt, cấu hình tham số cơ bản:
   - Tên ứng dụng: umami
   - Tên container: umami
   - Cổng: 3001 (hoặc tùy chỉnh)

4. **Cấu hình Database**

   Umami cần database PostgreSQL:
   - Có thể dùng dịch vụ database của 1Panel để tạo
   - Hoặc dùng database bên ngoài

5. **Hoàn tất cài đặt**

   Đợi container khởi động, truy cập `http://server-cua-ban:3001`.

### Đăng nhập lần đầu

Thông tin đăng nhập mặc định:

- Tên người dùng: admin
- Mật khẩu: umami

**Quan trọng**: Đăng nhập xong đổi mật khẩu ngay!

---

## Cấu hình Umami

### Tạo trang web

Sau khi đăng nhập, thêm trang web đầu tiên:

1. Bấm "Settings" → "Websites"
2. Bấm "Add website"
3. Điền thông tin:
   - Name: Tên trang web
   - Domain: Tên miền (như `example.com`)
4. Bấm lưu

### Lấy mã theo dõi

Sau khi thêm trang web sẽ hiện mã theo dõi:

```html
<script
  defer
  src="https://url-umami-cua-ban/script.js"
  data-website-id="id-website-cua-ban"
></script>
```

### Tích hợp vào Next.js

Tích hợp mã theo dõi vào dự án Next.js:

```typescript
// app/layout.tsx
import Script from 'next/script';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <head>
        <Script
          defer
          src="https://url-umami-cua-ban/script.js"
          data-website-id="id-website-cua-ban"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

Hoặc sử dụng biến môi trường:

```typescript
<Script
  defer
  src={process.env.NEXT_PUBLIC_UMAMI_URL}
  data-website-id={process.env.NEXT_PUBLIC_UMAMI_ID}
/>
```

---

## Giải mã các chỉ số cốt lõi

Bảng điều khiển Umami hiển thị các chỉ số cốt lõi sau.

### Chỉ số truy cập

| Chỉ số              | Giải thích                             |
| ------------------- | -------------------------------------- |
| **Pageviews**       | Tổng lượt xem trang                    |
| **Unique Visitors** | Số khách truy cập duy nhất             |
| **Visits**          | Số lượt truy cập (phiên/session)       |
| **Bounce Rate**     | Tỷ lệ thoát (tỷ lệ truy cập trang đơn) |

### Nguồn lưu lượng

| Nguồn        | Giải thích             |
| ------------ | ---------------------- |
| **Search**   | Công cụ tìm kiếm       |
| **Social**   | Mạng xã hội            |
| **Direct**   | Truy cập trực tiếp     |
| **Referral** | Link từ trang web khác |

### Thông tin thiết bị

| Chỉ số      | Giải thích                     |
| ----------- | ------------------------------ |
| **Browser** | Loại trình duyệt               |
| **OS**      | Hệ điều hành                   |
| **Device**  | Loại thiết bị (Desktop/Mobile) |
| **Screen**  | Độ phân giải màn hình          |

---

## Theo dõi sự kiện (Event Tracking)

Ngoài xem trang, còn có thể theo dõi sự kiện tùy chỉnh.

### Theo dõi click nút

```typescript
// Theo dõi click nút chia sẻ
import { umami } from "@umami/node";

umami.track("share", {
  platform: "twitter",
  content: "article-slug",
});
```

Hoặc dùng cách nguyên bản:

```typescript
// Theo dõi sự kiện chung
window.umami?.track("share", {
  platform: "twitter",
  content: "article-slug",
});
```

### Các loại sự kiện thường gặp

| Sự kiện     | Giải thích                        |
| ----------- | --------------------------------- |
| `signup`    | Đăng ký người dùng                |
| `login`     | Đăng nhập người dùng              |
| `purchase`  | Hoàn tất mua hàng                 |
| `download`  | Tải xuống file                    |
| `share`     | Chia sẻ nội dung                  |
| `cta_click` | Click nút kêu gọi hành động (CTA) |

---

## Chỉ số chính vs Chỉ số hư danh (Vanity Metrics)

Phân biệt chỉ số có ý nghĩa và chỉ số vô nghĩa.

| Chỉ số chính                        | Chỉ số hư danh        |
| ----------------------------------- | --------------------- |
| Tỷ lệ giữ chân                      | Tổng lượt xem         |
| Tỷ lệ chuyển đổi                    | Tổng số khách         |
| Người dùng hoạt động (Active Users) | Thời gian ở lại trang |
| Doanh thu                           | Số fan mạng xã hội    |

::: tip Tập trung vào chỉ số có giá trị hành động

Chọn chỉ số có thể chỉ dẫn hành động. Nếu nhìn một dữ liệu xong bạn không biết phải làm gì, thì đó có thể là chỉ số hư danh.

:::

---

## Bảo vệ quyền riêng tư

Thiết kế của Umami chú trọng bảo vệ quyền riêng tư.

### Tuân thủ GDPR

Umami không lưu trữ thông tin nhận dạng cá nhân:

- Không dùng Cookie
- Không theo dõi người dùng cá nhân
- Không thu thập dữ liệu định danh
- Kiểm soát dữ liệu hoàn toàn

### Cài đặt riêng tư

Trong cài đặt Umami có thể:

- Bật băm IP (ẩn danh một phần)
- Thiết lập thời hạn lưu giữ dữ liệu
- Vô hiệu hóa một số tính năng theo dõi

---

## Câu hỏi thường gặp

### Q1: Dùng đồng thời Umami và Google Analytics được không?

Được, nhưng không cần thiết. Chọn một cái thôi, dùng nhiều cái sẽ tăng gánh nặng tải trang.

### Q2: Dữ liệu bao lâu cập nhật?

Dữ liệu thời gian thực trễ khoảng 1-2 phút. Bảng điều khiển tự động làm mới.

### Q3: Làm thế nào xuất dữ liệu?

Umami hỗ trợ chức năng xuất dữ liệu. Trong cài đặt có thể chọn định dạng xuất và khoảng thời gian.

### Q4: Quản lý nhiều website thế nào?

Thêm nhiều website trong Umami, mỗi website có mã theo dõi và ID độc lập.

---

## Trọng tâm phần này

- ✅ Thống kê trang web giúp hiểu hành vi người dùng
- ✅ Umami là công cụ thống kê nguồn mở, thân thiện riêng tư
- ✅ 1Panel có thể triển khai Umami bằng một cú nhấp chuột
- ✅ Chỉ số cốt lõi gồm lượng truy cập, nguồn, thiết bị
- ✅ Theo dõi sự kiện giúp giám sát hành vi người dùng cụ thể
- ✅ Tập trung vào chỉ số chính thay vì chỉ số hư danh
- ✅ Bảo vệ quyền riêng tư là yêu cầu cơ bản của công cụ thống kê hiện đại

Sau khi triển khai thống kê, tiếp theo hãy tìm hiểu yêu cầu tuân thủ pháp lý.

---

## Nội dung liên quan

- Trước đó: [Chương 14: Vận hành VPS và Deploy](../14-vps-ops-deploy/index_vi.md)
- Trước đó: [15.1 Chia sẻ Open Graph](./01-opengraph-sharing_vi.md)
- Chi tiết: [15.4 Thực hành tuân thủ pháp lý](./04-legal_vi.md)
