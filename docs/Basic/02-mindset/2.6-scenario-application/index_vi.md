---
title: '2.6 Ứng dụng bối cảnh: Những công cụ tư duy này không chỉ dùng để "làm sản phẩm"'
---

![02-mindset_2.6-scenario-application_index.png](../../../public/images/Basic/02-mindset_2.6-scenario-application_index.png)

# 2.6 Ứng dụng bối cảnh: Những công cụ tư duy này không chỉ dùng để "làm sản phẩm"

Năm phần trước, chúng ta đã học năm loại công cụ tư duy: Tư duy JTBD, Tư duy ngược, Tư duy phép trừ, Tư duy câu chuyện, Ba câu hỏi linh hồn.

Có thể bạn sẽ nghĩ: Những cái này chẳng phải đều là thứ mà giám đốc sản phẩm, người khởi nghiệp dùng sao? Có liên quan gì đến tôi đâu?

Phần này sẽ nói cho bạn biết: **Bản chất của những công cụ tư duy này là năng lực "nghĩ rõ vấn đề", mà năng lực này áp dụng cho bất kỳ bối cảnh nào bạn có thể nghĩ tới.**

## Sau khi học xong bài này, bạn sẽ nắm được

- Hiểu tính phổ quát của công cụ tư duy: Cùng một phương pháp, ứng dụng trong các bối cảnh khác nhau
- Nắm được phương pháp mô tả nhu cầu và mẫu Prompt trong bối cảnh phân tích dữ liệu
- Nắm được cách đánh giá nhiệm vụ và mẫu Prompt trong bối cảnh script tự động hóa
- Nắm được nguyên tắc thiết kế trong bối cảnh công cụ cá nhân và công cụ cho người nhà
- Có được một bộ thư viện mẫu Prompt theo bối cảnh có thể sao chép dùng ngay

## Insight cốt lõi

> **Bất kể bạn muốn làm gì —— công cụ nhỏ, phân tích dữ liệu, script tự động hóa —— tư duy cốt lõi đều giống nhau: Nghĩ rõ vấn đề trước, rồi mới bắt tay giải quyết.**

Các công cụ tư duy phía trước không phải "độc quyền của giám đốc sản phẩm", mà là "độc quyền để định nghĩa vấn đề".

- Bạn làm phân tích dữ liệu, cũng cần hỏi "ai cần xem phân tích này? họ cần ra quyết định gì?" —— đây là Tư duy JTBD
- Bạn viết script tự động hóa, cũng cần nghĩ "trường hợp nào sẽ bị lỗi?" —— đây là Tư duy ngược
- Bạn tự làm công cụ nhỏ cho mình, cũng cần kiềm chế sự thôi thúc "càng nhiều tính năng càng tốt" —— đây là Tư duy phép trừ

**Công cụ tư duy là vạn năng, cái thay đổi chỉ là bối cảnh ứng dụng.**

## Sơ lược bốn bối cảnh lớn

Phần này bao phủ bốn loại bối cảnh Vibe Coding thường gặp nhất:

| Bối cảnh                  | Nhu cầu điển hình                          | Thách thức cốt lõi                    | Trọng tâm công cụ tư duy                                                                  |
| :------------------------ | :----------------------------------------- | :------------------------------------ | :---------------------------------------------------------------------------------------- |
| **Phân tích dữ liệu**     | Phân tích Excel, làm biểu đồ, viết báo cáo | Không biết phải trả lời câu hỏi gì    | JTBD (phân tích cho ai), Phép trừ (tập trung vấn đề cốt lõi)                              |
| **Script tự động hóa**    | Xử lý file hàng loạt, tác vụ định kỳ       | Không biết bắt đầu tự động hóa từ đâu | Tư duy ngược (nhận diện bối cảnh lỗi), Phép trừ (làm bước đau nhất trước)                 |
| **Công cụ cá nhân**       | Ghi chép chi tiêu, Pomodoro, ghi chú       | Dễ thiết kế quá mức                   | Phép trừ (chỉ làm tính năng cốt lõi), Ba câu hỏi linh hồn (nỗi đau thực sự của mình)      |
| **Công cụ cho người nhà** | Nhắc uống thuốc, album ảnh, lối tắt        | Không hiểu bối cảnh sử dụng thực tế   | Tư duy câu chuyện (đứng ở góc độ của họ), Tư duy ngược (điều gì khiến họ không dùng được) |

## Cấu trúc bài học

Tiếp theo, chúng ta sẽ lần lượt triển khai bốn bối cảnh này:

1.  **Insight cốt lõi**: Tại sao cùng một bộ công cụ tư duy có thể ứng dụng cho các bối cảnh khác nhau
2.  **Bối cảnh phân tích dữ liệu**: Cách dùng công cụ tư duy để AI thực hiện phân tích có giá trị
3.  **Bối cảnh script tự động hóa**: Cách nhận diện nhiệm vụ đáng tự động hóa, tránh các bẫy thường gặp
4.  **Bối cảnh công cụ cá nhân**: Cách kiềm chế xung động thiết kế quá mức, làm ra công cụ thực sự dùng được
5.  **Bối cảnh công cụ cho người nhà**: Cách thiết kế công cụ đơn giản dễ dùng cho người dùng không rành kỹ thuật
6.  **Tổng kết**: Bảng tra cứu mẫu Prompt theo bối cảnh

Mỗi bối cảnh đều sẽ cung cấp:

- Phương pháp ứng dụng cụ thể của công cụ tư duy
- Trường hợp thực tế và ví dụ Prompt hoàn chỉnh
- Lầm tưởng thường gặp và hướng dẫn tránh bẫy
- Mẫu có thể sao chép dùng ngay

Sẵn sàng chưa? Hãy bắt đầu từ "Insight cốt lõi".
