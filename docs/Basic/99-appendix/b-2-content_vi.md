---
title: "B.2 Vấn đề CSS/Style"
---

![99-appendix_b-2-content.png](../../public/images/Basic/99-appendix_b-2-content.png)

# B.2 Vấn đề CSS/Style

Vấn đề style sẽ không báo lỗi đỏ, nhưng sẽ khiến trang của bạn "trông sai sai". Phần này giúp bạn nhanh chóng định vị và giải quyết các vấn đề style thường gặp.

## Style hoàn toàn không có tác dụng

**Hiện tượng**: Bạn viết CSS, nhưng trang hoàn toàn không thay đổi gì.

**Danh sách kiểm tra**:

| Mục kiểm tra                | Cách kiểm tra                                       | Cách giải quyết                                                |
| --------------------------- | --------------------------------------------------- | -------------------------------------------------------------- |
| Chưa import file CSS        | Xem HTML có thẻ `<link>` không                      | Thêm `<link rel="stylesheet" href="style.css">`                |
| Viết sai đường dẫn          | Kiểm tra đường dẫn file có đúng không               | Đảm bảo đường dẫn `href` tương ứng với vị trí thực tế của file |
| Viết sai bộ chọn (selector) | Kiểm tra tên class/id có khớp không                 | `.btn` (class) vs `#btn` (id), đừng nhầm lẫn                   |
| Bị style khác ghi đè        | Dùng công cụ nhà phát triển trình duyệt để kiểm tra | Tăng trọng số selector hoặc điều chỉnh thứ tự                  |
| Vấn đề cache                | Bắt buộc tải lại trang (Force refresh)              | Mac: `Cmd+Shift+R`, Win: `Ctrl+Shift+R`                        |

**Prompt sửa nhanh**:

```markdown
CSS style của tôi không có tác dụng.

Code HTML:
[Dán HTML liên quan]

Code CSS:
[Dán CSS]

Hãy giúp tôi kiểm tra tại sao style không có tác dụng.
```

## Bố cục lộn xộn

**Hiện tượng**: Vị trí các phần tử không đúng, chen chúc nhau, chạy lệch, hoặc tràn ra ngoài.

**Vấn đề thường gặp và cách giải quyết**:

### Các phần tử chen chúc nhau

```css
/* Vấn đề: Nhiều phần tử chen chúc trên một hàng */
/* Giải quyết: Cho phép chúng xuống dòng */
.container {
  display: flex;
  flex-wrap: wrap; /* Cho phép xuống dòng */
  gap: 10px; /* Thêm khoảng cách */
}
```

### Phần tử chạy ra ngoài màn hình

```css
/* Vấn đề: Nội dung vượt quá khung chứa */
/* Giải quyết: Giới hạn chiều rộng, cho phép cuộn hoặc ẩn đi */
.content {
  max-width: 100%; /* Không vượt quá khung cha */
  overflow: auto; /* Hiển thị thanh cuộn khi vượt quá */
}
```

### Căn giữa theo chiều dọc không được

```css
/* Cách căn giữa theo chiều dọc đơn giản nhất */
.parent {
  display: flex;
  justify-content: center; /* Căn giữa theo chiều ngang */
  align-items: center; /* Căn giữa theo chiều dọc */
  height: 100vh; /* Khung cha phải có chiều cao! */
}
```

::: warning Hố thường gặp
Căn giữa theo chiều dọc không được, 90% là do khung cha không được đặt chiều cao. `height: 100%` hoặc `height: 100vh` là giải pháp thường dùng.
:::

## Vấn đề Responsive (Tương thích thiết bị)

**Hiện tượng**: Trên máy tính thì đẹp, lên điện thoại thì vỡ giao diện.

**Kiểm tra nhanh**:

1. Có thêm thẻ meta viewport chưa?
2. Có đang dùng phần trăm/rem thay vì px cố định không?
3. Có viết media query không?

**Mẫu Responsive cơ bản**:

```html
<!-- Bắt buộc phải thêm dòng này trong <head> -->
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

```css
/* Style cơ bản (Ưu tiên điện thoại) */
.container {
  width: 100%;
  padding: 15px;
}

/* Máy tính bảng trở lên */
@media (min-width: 768px) {
  .container {
    width: 750px;
    margin: 0 auto;
  }
}

/* Máy tính */
@media (min-width: 1024px) {
  .container {
    width: 960px;
  }
}
```

## Bảng tra cứu nhanh lỗi style thường gặp

| Vấn đề                                  | Nguyên nhân có thể              | Sửa nhanh                                                 |
| --------------------------------------- | ------------------------------- | --------------------------------------------------------- |
| Cỡ chữ không đúng                       | Kế thừa style của phần tử cha   | Thiết lập `font-size` rõ ràng                             |
| Màu sắc không đúng                      | Trọng số selector không đủ      | Kiểm tra xem có bị ghi đè không, tăng trọng số lên        |
| Khoảng cách (margin/padding) không đúng | Nhầm lẫn giữa margin và padding | margin là lề ngoài, padding là lề trong                   |
| Ảnh bị biến dạng                        | Tỷ lệ khung hình bị phá vỡ      | Sử dụng `object-fit: cover`                               |
| Nút không bấm được                      | Bị phần tử khác che mất         | Kiểm tra `z-index` và position                            |
| Chữ bị tràn                             | Khung chứa quá nhỏ              | Sử dụng `overflow: hidden` hoặc `text-overflow: ellipsis` |

## Dùng trình duyệt để gỡ lỗi style

Đây là cách hiệu quả nhất để giải quyết vấn đề style:

1. **Mở công cụ nhà phát triển**: Chuột phải vào trang → Kiểm tra (Inspect) (hoặc ấn F12)
2. **Chọn phần tử**: Nhấn vào biểu tượng "Mũi tên chọn" ở góc trên bên trái, rồi nhấn vào phần tử trên trang
3. **Xem style**: Bên phải sẽ hiển thị tất cả style của phần tử này
4. **Sửa trực tiếp**: Sửa trực tiếp giá trị CSS ở bên phải, trang web sẽ cập nhật theo thời gian thực
5. **Tìm vấn đề**: Xem style nào bị gạch ngang (chứng tỏ bị ghi đè)

::: tip Mẹo nhỏ
Sau khi chỉnh style ngon lành trong công cụ nhà phát triển, hãy copy CSS đã sửa về file code của bạn. Nhanh hơn nhiều so với việc sửa mò.
:::
