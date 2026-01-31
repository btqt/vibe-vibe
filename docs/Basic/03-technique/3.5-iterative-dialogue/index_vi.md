---
title: "3.5 Nghệ thuật đối thoại lặp lại"
---


![03-technique_3.5-iterative-dialogue_index.png](../../../public/images/Basic/03-technique_3.5-iterative-dialogue_index.png)
# 3.5 Nghệ thuật đối thoại lặp lại: Từ "làm một lần xong ngay" đến "từng bước tiếp cận"

> **Mục tiêu phần này**: Nắm vững kỹ thuật đối thoại nhiều vòng, học cách từng bước tiếp cận kết quả lý tưởng trong quá trình đối thoại

Bạn đã học được cách viết prompt có cấu trúc (3.2), nắm vững kỹ thuật nâng cao (3.3), thậm chí có thể viết ra một bản PRD hoàn chỉnh (3.4). Nhưng khi bạn giao tất cả những thứ này cho AI, rất có thể bạn sẽ phát hiện ra: **Output lần đầu tiên thường không phải là thứ bạn muốn**.

Đây không phải vấn đề của bạn, cũng không phải vấn đề của AI. Đây là bản chất của đối thoại.

## Sự thấu hiểu cốt lõi

> "Theo đuổi 'một lần hoàn hảo' là ảo giác, 'từng bước tiếp cận' mới là chính đạo."

Tưởng tượng bạn đang sửa nhà. Bạn sẽ không kỳ vọng thợ sơn quét xong nước đầu tiên mà đã hoàn hảo không tì vết. Bạn sẽ xem hiệu quả, góp ý, rồi điều chỉnh lại. Đối thoại với AI cũng như vậy — nó là một **quá trình hợp tác**, không phải một lần **thực thi mệnh lệnh**.

## Qua phần học này, bạn sẽ nắm vững

- Hiểu tại sao "đặt câu hỏi một lần" thường là chưa đủ
- Nắm vững mô hình ba giai đoạn của đối thoại lặp lại: Xem hướng đi → Sửa vấn đề → Mài giũa chi tiết
- Học cách dùng khung SBI để phản hồi hiệu quả cho AI
- Quản lý ngữ cảnh của cuộc đối thoại dài, tránh để AI "mất trí nhớ"
- Biết khi nào nên bắt đầu cuộc hội thoại mới, và làm thế nào để "chuyển nhà"

## Vị trí của phần này trong chương 3

```
3.1 Cơ bản về Prompt        →  Biết nên nói cho AI thông tin gì
      ↓
3.2 Khung cấu trúc          →  Học cách tổ chức các thông tin này
      ↓
3.3 Kỹ thuật nâng cao       →  Nắm vững các "cách hỏi" khác nhau
      ↓
3.4 Bản PRD đầu tiên        →  Tích hợp tư duy, hình thành bản nhiệm vụ
      ↓
3.5 Đối thoại lặp lại (Phần này) →  Điều chỉnh từng bước trong khi thực thi, tiếp cận kết quả lý tưởng
      ↓
3.6 Chiến lược Debug        →  Cách sửa chữa khi AI mắc lỗi
```

Nếu nói 3.1-3.4 là dạy bạn "cách mở đầu tốt", thì phần này chính là dạy bạn "cách chạy hết chặng đường".

## Cấu trúc phần này

| Tiểu tiết | Nội dung cốt lõi | Bạn sẽ nhận được |
|-----|---------|---------|
| 3.5.1 | Tại sao hỏi một lần thường là chưa đủ | Kỳ vọng đúng đắn: Lặp lại là bình thường, không phải thất bại |
| 3.5.2 | Mô hình cơ bản của đối thoại lặp lại | Mô hình ba giai đoạn + Ví dụ đối thoại đầy đủ |
| 3.5.3 | Nghệ thuật phản hồi hiệu quả | Khung SBI + Kho mẫu câu phản hồi |
| 3.5.4 | Quản lý ngữ cảnh | Bốn kỹ thuật tránh để AI "mất trí nhớ" |
| 3.5.5 | Biết khi nào nên bắt đầu đối thoại mới | Phán đoán thời điểm "chuyển nhà" + Mẫu khởi động |

## Tiếp nối trường hợp: Danh sách việc cần làm của Tiểu Lý

Phần này tiếp tục sử dụng dự án danh sách việc cần làm của Tiểu Lý. Bạn sẽ thấy một quá trình lặp lại hoàn chỉnh:

```
Nhu cầu ban đầu: "Giúp tôi thực hiện chức năng thêm nhiệm vụ"
    ↓
Vòng 1: AI đưa ra bản thực hiện cơ bản (Hướng đi đúng, nhưng chi tiết kém)
    ↓
Phản hồi: "Ô nhập liệu nhỏ quá, hơn nữa chưa có xác thực nhập rỗng"
    ↓
Vòng 2: AI sửa chữa, thêm xác thực (Chức năng đúng, nhưng cấu trúc chưa ưng ý)
    ↓
Phản hồi: "Logic xác thực đang để trong component, tôi muốn tách thành hàm độc lập"
    ↓
Vòng 3: Phiên bản cuối cùng (Cấu trúc rõ ràng, dễ bảo trì)
```

Ba vòng đối thoại, từ "dùng được" đến "dùng tốt". Đây chính là sức mạnh của sự lặp lại.

## Lời khuyên học tập

1. **Điều chỉnh kỳ vọng**: Output lần đầu không hoàn hảo là bình thường, đừng nản lòng
2. **Vừa học vừa luyện**: Mỗi tiểu tiết đều có mẫu có thể sao chép, khuyên bạn nên sử dụng thực tế
3. **Ghi chép kinh nghiệm**: Thu thập các mẫu câu phản hồi hiệu quả, hình thành "kho vũ khí" của riêng mình

Sẵn sàng chưa? Hãy bắt đầu từ "Tại sao hỏi một lần thường là chưa đủ".
