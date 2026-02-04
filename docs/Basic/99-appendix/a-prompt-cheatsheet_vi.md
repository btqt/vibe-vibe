---
title: "A. Danh sách tra cứu nhanh Prompt"
---

![99-appendix_a-prompt-cheatsheet.png](../../public/images/Basic/99-appendix_a-prompt-cheatsheet.png)

# A. Danh sách tra cứu nhanh Prompt

Tài liệu tham khảo nhanh khi viết Prompt. Giải thích chi tiết xem tại [Chương 3: Kỹ pháp](/Basic/03-technique/).

## Tra cứu nhanh khung S.C.A.F.F.

| Yếu tố            | Ý nghĩa             | Nhắc nhở một câu                                   |
| ----------------- | ------------------- | -------------------------------------------------- |
| **S** - Situation | Tình huống bối cảnh | Bạn đang làm dự án gì? Dùng công nghệ gì?          |
| **C** - Challenge | Thách thức cụ thể   | Hiện tại đang kẹt ở đâu? Cần giải quyết vấn đề gì? |
| **A** - Ask       | Yêu cầu rõ ràng     | Bạn muốn AI làm gì? Đầu ra là gì?                  |
| **F** - Format    | Định dạng đầu ra    | Muốn code? Muốn giải thích? Hay muốn danh sách?    |
| **F** - Filter    | Điều kiện lọc       | Cái gì không được làm? Có ràng buộc gì không?      |

## Các điểm chính trong kịch bản thường gặp

### Tạo dự án

- Nói rõ: Làm cái gì, cho ai dùng, tính năng cốt lõi (trong vòng 3 cái)
- Bắt đầu từ phiên bản đơn giản nhất trước

### Sửa đổi code

- Chỉ rõ vị trí: File nào, hàm nào
- Nói rõ: Hiện tại thế nào, muốn sửa thành thế nào
- Thêm một câu: "Chỉ sửa chỗ này, chỗ khác giữ nguyên"

### Sửa lỗi (Fix bug)

- Sao chép toàn bộ thông tin lỗi (hữu dụng gấp 100 lần so với nói "lỗi rồi")
- Giải thích: Lỗi xuất hiện khi thực hiện thao tác gì

### Giải thích code

- Dán code trực tiếp vào, hỏi "Đoạn code này đang làm gì"
- Có thể hỏi thêm: "Tại sao lại viết như thế này"

### Tối ưu hóa code

- Giải thích mục tiêu tối ưu: Dễ đọc? Hiệu năng? Hay giảm lặp lại?
- Để AI giải thích đã sửa những gì

## Mẹo nhỏ nâng cao hiệu quả

| Mẹo                               | Kịch bản áp dụng                           |
| --------------------------------- | ------------------------------------------ |
| Cho 1-2 ví dụ                     | Khi AI luôn hiểu sai ý đồ của bạn          |
| Để AI "nghĩ một chút rồi trả lời" | Logic phức tạp, nhiệm vụ nhiều bước        |
| Để AI tự kiểm tra                 | Khi không yên tâm lắm với code được tạo ra |
| Hỏi từng bước                     | Hỏi quá nhiều một lúc AI dễ bị loạn        |

## Hãy nhớ điều này

> **Cốt lõi của Prompt là "nói rõ ràng", không phải "ốp khuôn mẫu".**
>
> Sau khi học được khung tư duy, cứ dùng lời của chính bạn diễn đạt là được.
