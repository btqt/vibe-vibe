---
title: "4.5 Thực chiến Debug: Khi mã AI bị lỗi"
order: 1
---


![04-practice-0-to-1_4.5-debug_index.png](../../../public/images/Basic/04-practice-0-to-1_4.5-debug_index.png)
# 4.5 Thực chiến Debug: Khi mã AI bị lỗi

Qua phần học này, bạn sẽ nắm bắt được:
- Nhận diện 4 loại lỗi thường gặp trong quá trình phát triển danh sách việc cần làm
- Quy trình chuẩn dùng AI chẩn đoán và sửa lỗi mã nguồn
- Kỹ năng đối thoại hoàn chỉnh để xử lý báo lỗi thực tế
- Xây dựng tâm thái Debug "không sợ báo lỗi"

## Mối quan hệ với chương 3

Phần 3.6 của chương 3 giảng về **phương diện nguyên lý**: AI có những biểu hiện "không nghe lời" nào, làm sao nhận biết ảo giác của AI, khung tư duy chẩn đoán vấn đề.

Phần này giảng về **phương diện thực hành**: Xoay quanh dự án danh sách việc cần làm bạn đang phát triển, trình bày các thông tin báo lỗi thực tế, hội thoại sửa chữa hoàn chỉnh, và các mẫu Prompt có thể sao chép dùng ngay.

Nói đơn giản: 3.6 dạy bạn "gặp vấn đề nên nghĩ thế nào", 4.5 dạy bạn "gặp vấn đề nên làm thế nào".

## Tại sao báo lỗi là bình thường

Trong quá trình phát triển danh sách việc cần làm, có thể bạn đã gặp phải một số báo lỗi. Đừng lo lắng, chuyện này hoàn toàn bình thường.

| Hiểu lầm | Sự thật |
|------|------|
| "Báo lỗi chứng tỏ tôi làm sai" | Báo lỗi là mã đang nói với bạn chỗ nào cần điều chỉnh |
| "Lập trình viên chuyên nghiệp sẽ không gặp lỗi" | Lập trình viên chuyên nghiệp ngày nào cũng debug, chỉ là họ biết cách giải quyết |
| "Mã do AI tạo ra chắc không có vấn đề" | AI không hiểu môi trường cụ thể của bạn, cần bạn giúp nó điều chỉnh |

Tin tốt là: **AI có thể giúp bạn giải quyết 90% các vấn đề thường gặp**. Bạn chỉ cần học được "cách hỏi".

## Điều hướng chương

| Tiểu tiết | Chủ đề | Bạn sẽ học được |
|------|------|---------|
| [4.5.1](./4.5.1-error-types_vi.md) | Tra cứu nhanh các loại lỗi thường gặp | Phương pháp nhận diện 4 loại lỗi, cách đọc báo lỗi console |
| [4.5.2](./4.5.2-fix-with-ai_vi.md) | Dùng AI giúp bạn sửa mã AI | Các mẫu Prompt hoàn chỉnh để chẩn đoán, sửa chữa, xác thực |
| [4.5.3](./4.5.3-real-cases_vi.md) | Phân tích trường hợp thực tế | 6 lỗi điển hình trong phát triển danh sách việc cần làm và quá trình giải quyết |
| [4.5.4](./4.5.4-debug-mindset_vi.md) | Tâm pháp Debug tổng kết | Xây dựng thói quen và tâm thái debug đúng đắn |

**Thời gian học tập dự kiến: Khoảng 25-30 phút**

## Trước khi bắt đầu

Đảm bảo bạn đã hoàn thành việc phát triển từ 4.2-4.4, trên tay có một danh sách việc cần làm cơ bản dùng được. Nếu mã hiện tại của bạn chạy bình thường, cũng có thể xem qua nội dung chương này trước, đợi khi gặp vấn đề thì quay lại tra cứu.

Sẵn sàng chưa? Hãy bắt đầu từ việc nhận biết các loại lỗi thường gặp.

→ [4.5.1 Tra cứu nhanh các loại lỗi thường gặp](./4.5.1-error-types_vi.md)
