---
title: "3.2 Khung Prompt cấu trúc hóa"
---

![03-technique_3.2-structured-frameworks_index.png](../../../public/images/Basic/03-technique_3.2-structured-frameworks_index.png)

# 3.2 Khung Prompt cấu trúc hóa: Từ "nói tùy tiện" đến "có bài có bản"

Ở bài 3.1, bạn đã học được nguyên tắc cốt lõi "ngữ cảnh là vua", biết được nên nói cho AI thông tin gì. Nhưng có thể bạn vẫn còn một nỗi phiền lòng:

> "Đạo lý thì tôi hiểu rồi, nhưng mỗi lần viết Prompt vẫn phải nghĩ từ đầu, có cách nào đỡ tốn sức hơn không?"

Có. Đó chính là ý nghĩa tồn tại của **khung cấu trúc hóa**.

## Sau bài học này, bạn sẽ nắm được

- Hiểu giá trị của khung tư duy: Tại sao "ốp công thức" lại viết được Prompt tốt hơn
- Nắm vững khung S.C.A.F.F.: Cấu trúc hoàn chỉnh thích hợp cho nhiệm vụ phát triển kỹ thuật
- Nắm vững khung R.G.C.: Cấu trúc tinh gọn thích hợp cho câu hỏi nhanh
- Nhận được mẫu Prompt vạn năng: Lựa chọn bảo đảm khi không chắc dùng khung nào
- Học cách lựa chọn khung phù hợp tùy theo bối cảnh

## Mối quan hệ với Chương 2

Chương 2 bài 2.4.5 đã giới thiệu **Prompt câu chuyện** (Thân phận - Hiện trạng - Nỗi đau - Kỳ vọng), nó đặc biệt thích hợp cho các bối cảnh cần diễn đạt cảm xúc và nỗi đau người dùng.

Khung cấu trúc hóa của bài này có mối quan hệ **bổ sung** với Prompt câu chuyện, chứ không phải thay thế:

| Loại khung         | Đặc điểm cốt lõi                               | Bối cảnh áp dụng                     |
| :----------------- | :--------------------------------------------- | :----------------------------------- |
| Prompt câu chuyện  | Cảm xúc thúc đẩy, nhấn mạnh nỗi đau người dùng | Thiết kế sản phẩm, giao tiếp nhu cầu |
| Khung cấu trúc hóa | Logic thúc đẩy, nhấn mạnh ràng buộc kỹ thuật   | Triển khai code, nhiệm vụ kỹ thuật   |

Bạn có thể linh hoạt lựa chọn tùy theo tính chất nhiệm vụ, thậm chí kết hợp sử dụng.

## Cấu trúc bài này

```
3.2.1 Tại sao cần khung tư duy → Hiểu giá trị của khung, xóa bỏ hiểu lầm "ốp công thức là ngốc nghếch"
3.2.2 Khung S.C.A.F.F. → Khung 5 yếu tố hoàn chỉnh, thích hợp nhiệm vụ phức tạp
3.2.3 Khung R.G.C. → Khung 3 yếu tố tinh gọn, thích hợp hỏi nhanh
3.2.4 Mẫu Prompt vạn năng → Lựa chọn bảo đảm khi không chắc dùng cái nào
3.2.5 Hướng dẫn lựa chọn khung tư duy → Bối cảnh nào dùng khung gì
```

Sẵn sàng chưa? Hãy bắt đầu từ "Tại sao cần khung tư duy".
