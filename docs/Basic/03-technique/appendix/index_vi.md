---
title: "Phụ lục: Thư viện mẫu Prompt thường dùng"
---


![03-technique_appendix_index.png](../../../public/images/Basic/03-technique_appendix_index.png)
# Phụ lục: Thư viện mẫu Prompt thường dùng

Phụ lục này cung cấp một loạt mẫu Prompt có thể sao chép trực tiếp để sử dụng, bao phủ bốn ngữ cảnh lớn: tạo dự án, sửa đổi code, giải quyết vấn đề và tạo tài liệu.

## Cách sử dụng thư viện mẫu này

1. **Tìm ngữ cảnh của bạn**: Dựa vào bảng chỉ mục bên dưới, nhanh chóng định vị mẫu phù hợp với bạn
2. **Sao chép mẫu**: Sao chép mẫu vào cửa sổ chat với AI
3. **Thay thế placeholder**: Thay thế `[nội dung trong ngoặc vuông]` thành tình huống thực tế của bạn
4. **Cắt giảm theo nhu cầu**: Nếu một số trường không áp dụng, có thể xóa đi

## Chỉ mục theo ngữ cảnh: Tôi muốn làm gì → Dùng mẫu nào

| Bạn muốn làm gì | Mẫu đề xuất | Chương tương ứng |
|-----------|---------|---------|
| Làm một ứng dụng web từ con số 0 | Mẫu tạo ứng dụng web | A.1 |
| Dùng Python phân tích một bộ dữ liệu | Mẫu dự án phân tích dữ liệu | A.1 |
| Viết một script tự động hóa xử lý file | Mẫu script tự động hóa | A.1 |
| Thêm chức năng mới trên code hiện có | Mẫu mở rộng chức năng | A.2 |
| Tối ưu hiệu năng hoặc cấu trúc code | Mẫu tái cấu trúc code | A.2 |
| Code báo lỗi, cần sửa chữa | Mẫu rà soát lỗi thời gian chạy | A.3 |
| Code chạy được nhưng kết quả sai | Mẫu phân tích lỗi logic | A.3 |
| Không biết nên dùng công nghệ/thư viện nào | Mẫu tư vấn lựa chọn kỹ thuật | A.3 |
| Thêm chú thích cho code | Mẫu tạo chú thích code | A.4 |
| Viết tài liệu mô tả dự án | Mẫu tạo README | A.4 |

## Danh sách kiểm tra trước khi dùng mẫu

Trước khi gửi Prompt, kiểm tra nhanh:

- [ ] **Thông tin bối cảnh đầy đủ chưa?** Loại dự án, stack kỹ thuật, tiến độ hiện tại
- [ ] **Mô tả nhiệm vụ rõ ràng chưa?** Cụ thể phải làm gì, đầu vào đầu ra là gì
- [ ] **Điều kiện ràng buộc viết chưa?** Hạn chế bắt buộc tuân thủ, không được làm gì
- [ ] **Placeholder đã thay thế hết chưa?** Không còn sót lại nội dung `[ngoặc vuông]`
- [ ] **Định dạng kỳ vọng đã nói chưa?** Cần code hoàn chỉnh hay giải thích

## Cấu trúc phụ lục này

```
A.1 Mẫu tạo dự án     → Dựng dự án từ con số 0
A.2 Mẫu sửa đổi code  → Sửa đổi, mở rộng, tái cấu trúc code hiện có
A.3 Mẫu giải quyết vấn đề → Rà soát lỗi, lựa chọn kỹ thuật, giải thích khái niệm
A.4 Mẫu tạo tài liệu   → Chú thích, README, tài liệu API
```

## Mối quan hệ với chính văn

Phụ lục này là **hộp công cụ thực dụng** cho các phần nội dung của Chương 3:

| Chương chính văn | Tương ứng phụ lục |
|---------|---------|
| 3.2 Khung cấu trúc | Mẫu phụ lục được thiết kế dựa trên khung S.C.A.F.F. |
| 3.3 Kỹ thuật nâng cao | Một số mẫu tích hợp kỹ thuật Few-shot, CoT |
| 3.4 Mẫu PRD | A.1 Mẫu tạo dự án bổ sung cho PRD |
| 3.6 Xử lý vấn đề | A.3 Mẫu giải quyết vấn đề cung cấp định dạng chuẩn hóa |
| 3.7 Danh sách kiểm tra nhanh | Phụ lục cung cấp bản mẫu đầy đủ chi tiết hơn |

Bây giờ, chúng ta hãy đi vào thư viện mẫu cụ thể.
