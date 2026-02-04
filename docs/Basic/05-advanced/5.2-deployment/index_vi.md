---
title: "5.2 Mở mang tầm mắt: Đưa trang web lên Internet"
order: 1
---

![05-advanced_5.2-deployment_index.png](../../../public/images/Basic/05-advanced_5.2-deployment_index.png)

# 5.2 Mở mang tầm mắt: Đưa trang web lên Internet

Còn nhớ dự án danh sách việc cần làm bạn làm ở chương 4 không? Hiện tại nó chỉ có thể chạy trên máy tính của chính bạn. Phần này sẽ đưa bạn đi phát hành nó lên internet, để cả thế giới đều có thể truy cập.

## Sau bài học này, bạn sẽ nắm được

- Hiểu ý nghĩa của "triển khai", xóa bỏ nỗi sợ việc phát hành (online)
- Chọn nền tảng triển khai phù hợp với tình huống của mình
- Hoàn thành quy trình hoàn chỉnh từ dự án cục bộ đến trang web trực tuyến
- Nhận được một địa chỉ web thực sự có thể chia sẻ cho bất kỳ ai

## Bây giờ vs Sau khi triển khai

| Hạng mục so sánh        | Bây giờ (Cục bộ)                     | Sau khi triển khai             |
| ----------------------- | ------------------------------------ | ------------------------------ |
| Cách truy cập           | Chỉ mở được trên máy tính của bạn    | Mọi thiết bị đều truy cập được |
| Địa chỉ web             | localhost:3000                       | your-todo.zeabur.app           |
| Chia sẻ                 | Phải đưa máy tính cho người khác xem | Chỉ cần gửi một liên kết       |
| Sử dụng trên điện thoại | Không thể sử dụng                    | Sử dụng mọi lúc mọi nơi        |
| Sau khi tắt máy         | Người khác không thể truy cập        | Trực tuyến 24 giờ              |

## Điều hướng chương

| Mục                                 | Chủ đề                                             | Thời gian dự kiến |
| ----------------------------------- | -------------------------------------------------- | ----------------- |
| [5.2.1](./5.2.1-why-deploy_vi.md)      | Tại sao phải triển khai trực tuyến                 | 3 phút            |
| [5.2.2](./5.2.2-platform-guide_vi.md)  | Hướng dẫn chọn nền tảng triển khai                 | 5 phút            |
| [5.2.3](./5.2.3-zeabur_vi.md)          | Thực chiến triển khai Zeabur (Ưu tiên cho Đại lục) | 10 phút           |
| [5.2.4](./5.2.4-vercel_vi.md)          | Thực chiến triển khai Vercel                       | 8 phút            |
| [5.2.5](./5.2.5-after-deploy_vi.md)    | Các thao tác thiết thực sau khi triển khai         | 5 phút            |
| [5.2.6](./5.2.6-china-solution_vi.md)  | Giải pháp truy cập tại Đại lục                     | 5 phút            |
| [5.2.7](./5.2.7-other-platforms_vi.md) | Các lựa chọn triển khai khác                       | 3 phút            |
| [5.2.8](./5.2.8-faq_vi.md)             | Các câu hỏi thường gặp về triển khai               | 3 phút            |
| [5.2.9](./5.2.9-checklist_vi.md)       | Danh sách kiểm tra phần này                        | 2 phút            |

**Tổng thời gian dự kiến: khoảng 40-45 phút**

::: tip Gợi ý
Nếu bạn ở Trung Quốc đại lục, khuyên bạn nên ưu tiên đọc 5.2.2 và 5.2.3, sử dụng Zeabur để triển khai. Nếu bạn ở nước ngoài hoặc có tên miền tùy chỉnh, có thể chọn Vercel.
:::

→ [5.2.1 Tại sao phải triển khai trực tuyến](./5.2.1-why-deploy_vi.md)
