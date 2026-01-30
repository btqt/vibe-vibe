---
title: "3.3 Kỹ thuật Prompt nâng cao"
---

![03-technique_3.3-advanced-techniques_index.png](../../../public/images/Basic/03-technique_3.3-advanced-techniques_index.png)

# 3.3 Kỹ thuật Prompt nâng cao: Mở khóa năng lực ẩn giấu của AI

Ở bài 3.2, bạn đã học cách dùng khung cấu trúc hóa (S.C.A.F.F., R.G.C.) để tổ chức Prompt. Khung đã giải quyết vấn đề "tổ chức thông tin thế nào", nhưng vẫn còn một câu hỏi chưa được trả lời:

> "Cùng một thông tin, có cách 'hỏi' nào thông minh hơn để AI thể hiện tốt hơn không?"

Có. Đó chính là **Kỹ thuật Prompt nâng cao** được giới thiệu trong phần này.

## Sau bài học này, bạn sẽ nắm được

- **Zero-shot**: Hỏi trực tiếp, thích hợp cho nhiệm vụ AI đã "biết"
- **Few-shot**: Dùng ví dụ dạy AI, thích hợp cho đầu ra định dạng hóa
- **Chain of Thought**: Để AI suy nghĩ phân bước, thích hợp cho logic phức tạp
- **Tree of Thoughts**: Khám phá nhiều con đường, thích hợp so sánh phương án
- **Self-Critique**: Để AI tự kiểm tra, nâng cao chất lượng đầu ra
- **Hướng dẫn lựa chọn kỹ thuật**: Trường hợp nào dùng kỹ thuật gì

## Insight cốt lõi

> "Nhiệm vụ khác nhau cần cách tư duy khác nhau. Bản chất của kỹ thuật Prompt là dẫn dắt AI sử dụng cách thức phù hợp nhất để xử lý vấn đề của bạn."

Nghiên cứu năm 2024 chỉ ra rằng: Kỹ thuật Chain of Thought (Chuỗi suy nghĩ) có hiệu quả đáng kể trong các nhiệm vụ **toán học và suy luận ký hiệu**, nhưng lợi ích hạn chế trong các loại nhiệm vụ khác. Điều này có nghĩa là: **Không có kỹ thuật vạn năng, chỉ có kỹ thuật phù hợp nhất**.

Mục tiêu của phần này không phải để bạn nhớ hết tất cả kỹ thuật, mà là giúp bạn xây dựng một "trực giác lựa chọn kỹ thuật" —— nhìn thấy nhiệm vụ là biết ngay nên dùng cách nào để đối thoại với AI.

## Cấu trúc bài này

```
3.3.1 Zero-shot Prompting    → Cách hỏi cơ bản nhất, thích hợp nhập môn
3.3.2 Few-shot Prompting     → Dùng ví dụ dạy AI, công cụ sắc bén cho định dạng hóa
3.3.3 Chain of Thought       → Suy luận phân bước, trợ thủ đắc lực cho logic phức tạp
3.3.4 Tree of Thoughts       → Khám phá đa đường dẫn, chuyên dụng cho bối cảnh ra quyết định
3.3.5 Self-Critique          → AI tự kiểm tra, phòng tuyến cuối cùng đảm bảo chất lượng
3.3.6 Hướng dẫn lựa chọn kỹ thuật → Quyết định nhanh, bối cảnh nào dùng kỹ thuật gì
```

## Mối quan hệ với các chương trước

| Chương tiết            | Vấn đề giải quyết                     | Ví von                     |
| :--------------------- | :------------------------------------ | :------------------------- |
| 3.1 Cơ bản về Prompt   | Nên nói cho AI **thông tin gì**       | Chuẩn bị nguyên liệu       |
| 3.2 Khung cấu trúc hóa | Làm sao **tổ chức** các thông tin này | Sắp xếp theo công thức     |
| 3.3 Kỹ thuật nâng cao  | Dùng **cách thức** nào để AI xử lý    | Chọn phương pháp nấu nướng |

Ba phần này có quan hệ thăng tiến: Đầu tiên biết phải nói gì (3.1), sau đó học cách tổ chức (3.2), cuối cùng nắm vững các "cách hỏi" khác nhau (3.3).

## Tiếp nối Case Study: Danh sách việc cần làm của Tiểu Lý

Phần này tiếp tục sử dụng dự án danh sách việc cần làm của Tiểu Lý ở Chương 2 làm ví dụ xuyên suốt. Bạn sẽ thấy cùng một nhu cầu, dùng các kỹ thuật hỏi khác nhau sẽ nhận được hiệu quả khác nhau như thế nào.

## Lời khuyên học tập

1.  **Nắm vững Zero-shot và Few-shot trước**: Hai kỹ thuật này bao phủ 80% bối cảnh hàng ngày
2.  **Chain of Thought dùng theo nhu cầu**: Gặp logic phức tạp hẵng dùng
3.  **Tree of Thoughts biết là được**: Khi nào chọn kỹ thuật mới cần đến
4.  **Self-Critique tập thành thói quen**: Đầu ra quan trọng đều để AI tự kiểm tra lại một lượt

Sẵn sàng chưa? Hãy bắt đầu từ Zero-shot cơ bản nhất.
