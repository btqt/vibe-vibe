---
title: "3.6 Khi AI không nghe lời"
---


![03-technique_3.6-debugging-ai_index.png](../../../public/images/Basic/03-technique_3.6-debugging-ai_index.png)
# 3.6 Khi AI không nghe lời: Chiến lược gỡ lỗi, sửa chữa và dự phòng

## Qua phần học này, bạn sẽ nắm vững

- Nhận biết sáu loại vấn đề phổ biến trong output của AI
- "Phương pháp nhanh 3 phút" chẩn đoán gốc rễ vấn đề
- Bốn chiến lược sửa chữa để AI sửa đúng
- Phương án dự phòng khi AI thực sự "bó tay"
- Kỹ thuật thực dụng để phòng ngừa vấn đề phát sinh

## Tại sao cần học "gỡ lỗi AI"

Trong các chương trước, bạn đã học cách viết prompt tốt (3.1-3.4), cũng nắm vững kỹ thuật đối thoại lặp lại (3.5). Nhưng ngay cả khi bạn làm tốt đến đâu, AI đôi khi vẫn sẽ "không nghe lời":

- Code đưa ra không chạy được
- Ý hiểu khác với suy nghĩ của bạn
- Giới thiệu thư viện hoàn toàn không tồn tại
- Sửa đi sửa lại nhưng càng sửa càng loạn

Đừng lo, chuyện này rất bình thường.

Khác với sai lầm của con người, sai lầm của AI thường là **có thể dự đoán được, có quy luật**. Một khi bạn nắm vững những quy luật này, bạn có thể chuyển từ "hoảng loạn" sang "ung dung" — biết vấn đề nằm ở đâu, biết sửa thế nào, và cũng biết khi nào nên đổi phương án.

## Cấu trúc phần này

| Tiểu tiết | Chủ đề | Bạn sẽ học được |
|-----|------|---------|
| 3.6.1 | Các biểu hiện "không nghe lời" thường gặp của AI | Sáu loại vấn đề, trọng điểm: Ảo giác AI và rủi ro bảo mật |
| 3.6.2 | Chẩn đoán vấn đề: AI sai ở đâu | Phương pháp chẩn đoán 3 phút, bốn góc phần tư phân tích nguyên nhân gốc rễ |
| 3.6.3 | Chiến lược sửa chữa: Làm sao để AI sửa đúng | Bốn chiến lược sửa chữa, phát triển định hướng bởi lỗi |
| 3.6.4 | Chiến lược dự phòng: Khi AI thực sự "bó tay" | Giới hạn năng lực AI, mô hình phát triển hỗn hợp |
| 3.6.5 | Phòng bệnh hơn chữa bệnh | Tự kiểm tra trước khi gửi, kỹ thuật thuật lại, bước nhỏ chạy nhanh |

## Tâm pháp cốt lõi

> **AI mắc lỗi không đáng sợ, đáng sợ là không biết nó sai.**

Trong Vibe Coding, vai trò của bạn không phải là viết code, mà là **chỉ huy và nghiệm thu**. Điều này có nghĩa là bạn cần trang bị năng lực nhận biết vấn đề, hướng dẫn sửa chữa. Phần này chính là dạy năng lực đó.

Sẵn sàng chưa? Hãy bắt đầu từ việc nhận biết các biểu hiện "không nghe lời" khác nhau của AI.
