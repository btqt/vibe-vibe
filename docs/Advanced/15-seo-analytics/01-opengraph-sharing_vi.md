---
title: "15.1 Open Graph và Chia sẻ mạng xã hội"
description: "Giao thức Open Graph và tối ưu hóa cho nền tảng xã hội"
chapter: "Chương 15"
priority: "🔴"
---

# 15.1 Open Graph và Chia sẻ mạng xã hội 🔴

> **Đọc xong phần này, bạn sẽ gặt hái được:**
>
> - Hiểu tác dụng và nguyên lý của giao thức Open Graph
> - Nắm vững cách cấu hình OG trong Next.js
> - Học cách thiết kế ảnh OG hiệu quả
> - Hiểu chiến lược tối ưu cho các nền tảng mạng xã hội khác nhau
> - Nắm vững tích hợp tính năng chia sẻ và theo dõi dữ liệu

> Hãy tưởng tượng bạn chia sẻ link trang web được thiết kế tâm huyết lên mạng xã hội, nhưng nếu chỉ hiện ra một đường link màu xanh, không có bất kỳ hình ảnh xem trước nào, tỷ lệ click sẽ cực thấp. Giao thức Open Graph chính là để giải quyết vấn đề này.

---

## Open Graph là gì?

**Open Graph (OG)** là một giao thức siêu dữ liệu (metadata) do Facebook giới thiệu, giúp trang web hiển thị thông tin xem trước phong phú khi được chia sẻ trên mạng xã hội.

Khi bạn chia sẻ link lên WeChat, Twitter (X), LinkedIn, Facebook, Zalo, v.v., các nền tảng này sẽ cào (crawl) thẻ OG của trang web để tạo ra thẻ (card) chia sẻ.

### Tác dụng của thẻ OG

| Có thẻ OG                | Không có thẻ OG      |
| ------------------------ | -------------------- |
| Thẻ xem trước đẹp mắt    | Chỉ có link màu xanh |
| Tiêu đề, mô tả, hình ảnh | Chỉ có URL           |
| Tỷ lệ click cao          | Tỷ lệ click thấp     |

::: tip Tầm quan trọng của chia sẻ mạng xã hội

Chia sẻ mạng xã hội là nguồn lưu lượng quan trọng của sản phẩm hiện đại. Sức hấp dẫn thị giác quyết định trực tiếp đến tỷ lệ click, ấn tượng đầu tiên ảnh hưởng đến quyết định của người dùng. Tối ưu OG không phải là tùy chọn, mà là cơ sở hạ tầng của tiếp thị.

:::

---

## Các thẻ Open Graph cơ bản

Giao thức OG định nghĩa một nhóm thẻ `<meta>`, đặt trong phần `<head>` của HTML:

### Các thẻ OG cốt lõi

| Thẻ              | Giải thích               | Ví dụ                             |
| ---------------- | ------------------------ | --------------------------------- |
| `og:title`       | Tiêu đề thẻ chia sẻ      | "Tên sản phẩm của tôi"            |
| `og:description` | Mô tả thẻ chia sẻ        | "Một câu nói rõ giá trị sản phẩm" |
| `og:image`       | URL hình ảnh thẻ chia sẻ | "https://..."                     |
| `og:url`         | URL chuẩn của trang      | "https://..."                     |
| `og:type`        | Loại nội dung            | "website" hoặc "article"          |

::: tip Nhờ AI giúp bạn cấu hình

Cần cấu hình thẻ OG cho dự án Next.js? Bạn có thể nói thế này:

> "Giúp tôi cấu hình metadata trong app/layout.tsx, thêm cài đặt openGraph, bao gồm title, description, url và một ảnh kích thước 1200x630."

:::

---

## Cấu hình OG trong Next.js

Next.js cung cấp nhiều cách để cấu hình thẻ OG.

### Cách 1: Metadata API

Cấu hình trường `openGraph` trong đối tượng `metadata` tại `layout.tsx` hoặc `page.tsx`.

### Cách 2: File ảnh OG (Khuyên dùng)

Next.js hỗ trợ tự động sinh thẻ OG bằng cách đặt file có tên quy định:

```
app/
├── opengraph-image.jpg      # Ảnh OG chính
├── twitter-image.jpg        # Ảnh đặc thù cho Twitter
└── (routes)/
    └── about/
        └── opengraph-image.jpg  # Ảnh OG cho trang cụ thể
```

Các tên file được hỗ trợ:

- `opengraph-image.{jpg,png,webp}`
- `twitter-image.{jpg,png,webp}`

::: tip Tại sao khuyên dùng cách file?

Cách dùng file trực quan hơn, dùng công cụ thiết kế sinh ảnh xong bỏ vào là được. Next.js sẽ tự động xử lý mọi chi tiết kỹ thuật.

:::

### Cách 3: Sinh ảnh OG động

Next.js có thể dùng code để sinh ảnh OG động. Sử dụng `ImageResponse` của `next/og`, trả về JSX chứa tiêu đề và style trong file `app/opengraph-image.tsx`.

::: tip Nhờ AI giúp bạn sinh ảnh OG

Cần sinh ảnh OG động có tiêu đề? Bạn có thể nói:

> "Giúp tôi tạo file sinh ảnh OG động app/opengraph-image.tsx, kích thước 1200x630, nền trắng, tiêu đề căn giữa. Sử dụng ImageResponse của next/og."

:::

---

## Thiết kế ảnh OG hiệu quả

Ảnh OG là cốt lõi của thẻ chia sẻ, thiết kế tốt có thể tăng đáng kể tỷ lệ click.

### Kích thước đề xuất

| Nền tảng | Kích thước đề xuất | Yêu cầu tối thiểu |
| -------- | ------------------ | ----------------- |
| Facebook | 1200 x 630         | 600 x 315         |
| Twitter  | 1200 x 675         | 600 x 335         |
| LinkedIn | 1200 x 627         | 1200 x 627        |

**Đề xuất chung**: 1200 x 630 pixel, tỷ lệ 16:9

### Nguyên tắc thiết kế

| Nguyên tắc                | Giải thích                                    |
| ------------------------- | --------------------------------------------- |
| **Ngắn gọn rõ ràng**      | Tiêu đề ngắn, làm nổi bật thông tin cốt lõi   |
| **Nhất quán thương hiệu** | Sử dụng màu sắc và font chữ thương hiệu       |
| **Chất lượng cao**        | Tránh ảnh mờ, vỡ hạt                          |
| **Vùng an toàn cho chữ**  | Nội dung quan trọng tránh mép (có thể bị cắt) |
| **Độ tương phản**         | Đảm bảo chữ rõ ràng dễ đọc                    |

### Công cụ thiết kế đề xuất

- Canva: Có sẵn mẫu ảnh OG
- Figma: Công cụ thiết kế chuyên nghiệp
- Photoshop: Phần mềm thiết kế truyền thống
- Trình tạo trực tuyến: Như OG Image Generator

---

## Chiến lược tối ưu cho từng nền tảng

Mỗi mạng xã hội hỗ trợ OG có chút khác biệt, cần tối ưu theo đặc thù.

### Thẻ Twitter/X

Twitter hỗ trợ thẻ `twitter:card` chuyên biệt:

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@yourusername" />
<meta name="twitter:title" content="Tiêu đề" />
<meta name="twitter:description" content="Mô tả" />
<meta name="twitter:image" content="https://..." />
```

Các loại thẻ:

- `summary`: Thẻ ảnh nhỏ
- `summary_large_image`: Thẻ ảnh lớn (Khuyên dùng)
- `player`: Trình phát video

### Tối ưu chia sẻ WeChat/Zalo

WeChat/Zalo hỗ trợ OG có giới hạn, đề xuất:

- Đảm bảo `og:title` và `og:description` đầy đủ
- Sử dụng ảnh HTTPS
- Ảnh đừng quá nhỏ (Khuyên dùng > 300KB nhưng ko quá 5MB)
- Zalo: Quan tâm Zalo Developer để cấu hình chi tiết hơn nếu cần

### Tối ưu LinkedIn

LinkedIn tuân thủ nghiêm ngặt chuẩn OG, đảm bảo:

- `og:image` kích thước đúng (1200 x 627)
- URL ảnh có thể truy cập công khai
- Tránh dùng tham số phá cache (cache busting)

---

## Tích hợp tính năng chia sẻ

Thêm nút chia sẻ mạng xã hội vào website.

### Định dạng URL chia sẻ

| Nền tảng      | URL chia sẻ                                               |
| ------------- | --------------------------------------------------------- |
| Twitter       | `https://twitter.com/intent/tweet?text=Tiêu đề&url=URL`   |
| Facebook      | `https://www.facebook.com/sharer/sharer.php?u=URL`        |
| LinkedIn      | `https://www.linkedin.com/sharing/share-offsite/?url=URL` |
| Sao chép link | Dùng Clipboard API                                        |

### Component chia sẻ React

Tạo một Client Component, chứa liên kết chia sẻ các nền tảng và chức năng sao chép link.

URL chia sẻ:

- Twitter: `https://twitter.com/intent/tweet?text=Tiêu đề&url=URL`
- Facebook: `https://www.facebook.com/sharer/sharer.php?u=URL`
- LinkedIn: `https://www.linkedin.com/sharing/share-offsite/?url=URL`

Sử dụng `navigator.clipboard.writeText()` để sao chép link vào clipboard.

::: tip Nhờ AI giúp bạn tạo component chia sẻ

Cần nút chia sẻ mạng xã hội? Bạn có thể nói:

> "Giúp tôi tạo một React Client Component tên ShareButtons, nhận tham số title và url. Bao gồm 3 link chia sẻ Twitter, Facebook, LinkedIn (mở tab mới), và một nút sao chép link. Sao chép thành công hiện 'Đã sao chép!', sau 2 giây khôi phục. Sử dụng layout flex gap-4 của Tailwind CSS."

:::

### Cập nhật OG động

Đối với trang động (như bài viết blog), sử dụng hàm `generateMetadata`, dựa vào tham số route (như `params.slug`) để lấy thông tin bài viết từ database, thiết lập thẻ OG động.

::: tip Nhờ AI giúp bạn cấu hình OG động

Cần cấu hình OG động cho bài viết blog? Bạn có thể nói:

> "Giúp tôi tạo hàm generateMetadata trong app/blog/[slug]/page.tsx. Lấy bài viết từ hàm `getPost(slug)` trong `lib/posts.ts`, trả về metadata bao gồm title, description, ogImage (ảnh bìa bài viết), loại openGraph đặt là 'article'."

:::

---

## Theo dõi dữ liệu chia sẻ

Hiểu hiệu quả chia sẻ giúp tối ưu chiến lược.

### Theo dõi tham số UTM

Thêm tham số UTM vào URL chia sẻ để theo dõi nguồn:

- `utm_source`: Nền tảng nguồn (như twitter)
- `utm_medium`: Loại phương tiện (như social)
- `utm_campaign`: Tên chiến dịch

### Theo dõi sự kiện Umami

Sử dụng `window.umami.track('eventName', properties)` để theo dõi sự kiện click nút chia sẻ.

---

## Kiểm thử và Gỡ lỗi

Sau khi cấu hình, cần kiểm tra hiệu quả chia sẻ.

### Công cụ kiểm thử

| Công cụ                 | Link                                   | Chức năng                   |
| ----------------------- | -------------------------------------- | --------------------------- |
| Facebook Debugger       | developers.facebook.com/tools/debug/   | Kiểm tra thẻ OG             |
| Twitter Card Validator  | cards-dev.twitter.com/validator        | Kiểm tra thẻ Twitter        |
| LinkedIn Post Inspector | linkedin.com/post-inspector/           | Kiểm tra xem trước LinkedIn |
| Zalo Debugger           | developers.zalo.me/tools/debug-sharing | Kiểm tra chia sẻ Zalo       |

### Xóa Cache

Mạng xã hội sẽ cache thông tin chia sẻ, sau khi cập nhật OG cần:

1. Sử dụng tính năng "Scrape Again" (Thu thập lại) của công cụ gỡ lỗi
2. Hoặc thêm tham số như `?v=2` vào sau URL để buộc làm mới

---

## Câu hỏi thường gặp

### Q1: Ảnh OG không hiện thì làm sao?

Kiểm tra:

1. URL ảnh có truy cập công khai được không
2. Định dạng ảnh có đúng không (JPG/PNG)
3. Ảnh có quá lớn không (Khuyên dùng < 5MB)
4. Dùng công cụ gỡ lỗi (Debugger) để xem lỗi cụ thể

### Q2: Các trang khác nhau dùng ảnh OG khác nhau được không?

Được. Tạo file `opengraph-image.{jpg,png}` tương ứng cho mỗi route, hoặc ghi đè metadata trong `page.tsx` cấp trang.

### Q3: Tại sao chia sẻ Zalo/WeChat không hiện ảnh?

Zalo/WeChat có cơ chế riêng, có thể cần đảm bảo kích thước ảnh đủ lớn, hoặc tên miền không bị chặn.

### Q4: Làm thế nào để tăng tỷ lệ chia sẻ?

1. Tối ưu ảnh OG cho hấp dẫn
2. Sử dụng tiêu đề và mô tả thu hút hơn
3. Bản thân nội dung phải có giá trị chia sẻ
4. Đơn giản hóa quy trình chia sẻ, một nút bấm là xong

---

## Trọng tâm phần này

- ✅ Giao thức Open Graph giúp hiển thị thông tin xem trước phong phú khi chia sẻ web
- ✅ Next.js hỗ trợ cấu hình OG qua metadata API và qua file ảnh
- ✅ Kích thước ảnh OG khuyến nghị là 1200 x 630
- ✅ Các nền tảng mạng xã hội khác nhau có yêu cầu tối ưu riêng
- ✅ Nút chia sẻ cần đơn giản hóa, bấm là xong
- ✅ Sử dụng tham số UTM để theo dõi hiệu quả chia sẻ

Sau khi tối ưu OG, tiếp theo hãy tìm hiểu cấu hình SEO cơ bản.

---

## Nội dung liên quan

- Chi tiết: [15.2 SEO Toàn tập](./02-seo-guide_vi.md)
- Trước đó: [Chương 14: Vận hành VPS và Deploy](../14-vps-ops-deploy/index_vi.md)
