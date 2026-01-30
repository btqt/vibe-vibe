---
title: "3.1 Cơ bản về kỹ thuật Prompt: Context is King"
---

![03-technique_3.1-prompt-basics_index.png](../../../public/images/Basic/03-technique_3.1-prompt-basics_index.png)

# 3.1 Cơ bản về kỹ thuật Prompt: Context is King

Ở Chương 2, bạn đã học được cách dùng công cụ tư duy của giám đốc sản phẩm để "nghĩ rõ" cần làm gì. Bây giờ, đã đến lúc học cách "nói rõ" —— diễn đạt những gì bạn đã nghĩ rõ theo cách mà AI có thể hiểu được.

## Sau bài học này, bạn sẽ nắm được

- Hiểu kỹ thuật Prompt là gì, cũng như xu hướng mới nhất năm 2025
- Nắm vững mô hình "ngữ cảnh ba tầng", biết nên nói cho AI thông tin gì
- Nhận diện và tránh 5 sai lầm người mới thường gặp nhất

## Insight cốt lõi của bài này

> "Chất lượng đầu ra của AI = Chất lượng ngữ cảnh bạn cung cấp × Năng lực của AI. Bạn chỉ có thể kiểm soát vế trước."

Rất nhiều người tưởng tượng "kỹ thuật Prompt" là một nghệ thuật niệm chú bí ẩn —— dường như tồn tại những từ ngữ ma thuật nào đó, nói đúng là AI sẽ đưa ra câu trả lời hoàn hảo.

Sự thật hoàn toàn ngược lại.

Cốt lõi của kỹ thuật Prompt không phải là "hỏi thế nào", mà là "nói cho AI biết cái gì". AI giống như một thực tập sinh năng lực rất mạnh nhưng mới vào làm: Nó cái gì cũng làm được, nhưng hoàn toàn không biết gì về dự án của bạn. Nhiệm vụ của bạn không phải là dạy nó lập trình, mà là nói cho nó biết đủ thông tin nền tảng.

**Nói trắng ra: Ngữ cảnh là vua, Context is King.**

## Cấu trúc bài này

```
3.1.1 Kỹ thuật Prompt là gì → Thiết lập nhận thức đúng đắn, xóa bỏ cảm giác bí ẩn
3.1.2 Context is King → Nắm vững mô hình ngữ cảnh ba tầng
3.1.3 Năm sai lầm người mới thường gặp → Đối chiếu kiểm tra, tránh hố thường gặp
```

## Mối liên hệ với Chương 2

Nội dung bài này liên kết chặt chẽ với Chương 2:

| Thành quả Chương 2                                                      | Ứng dụng trong bài này                   |
| :---------------------------------------------------------------------- | :--------------------------------------- |
| Ba câu hỏi linh hồn (Người dùng là ai, nỗi đau ở đâu, tại sao chọn bạn) | Nguyên liệu xây dựng "ngữ cảnh nhiệm vụ" |
| Chân dung người dùng                                                    | Giúp mô tả người dùng mục tiêu của dự án |
| Tư duy phép trừ (Danh sách không làm)                                   | Dùng để giới hạn phạm vi đầu ra của AI   |

Chương 2 giúp bạn "nghĩ rõ", bài này giúp bạn "nói rõ". Cả hai đều không thể thiếu.

Sẵn sàng chưa? Chúng ta hãy bắt đầu từ "Kỹ thuật Prompt là gì".
