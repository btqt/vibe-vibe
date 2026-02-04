---
title: "C.2 Liên quan đến Phát triển"
---

![99-appendix_c-2-content.png](../../public/images/Basic/99-appendix_c-2-content.png)

# C.2 Liên quan đến Phát triển

Đây là các thuật ngữ thường dùng trong phát triển phần mềm. Không cần hiểu sâu, chỉ cần biết đại khái ý nghĩa là được.

## MVP

**Viết tắt của**: Minimum Viable Product (Sản phẩm khả thi tối thiểu)

**Giải thích một câu**: Phiên bản đơn giản nhất dùng được, chỉ bao gồm các chức năng cốt lõi nhất.

**Ví dụ tương tự**: Làm một chiếc xe đạp chạy được trước, chứ không phải vừa vào đã muốn chế tạo xe Tesla.

**Tại sao quan trọng**:

- Nhanh chóng xác minh ý tưởng có khả thi không
- Sớm phát hiện vấn đề
- Tránh lãng phí thời gian vào các chức năng không ai cần

## PRD

**Viết tắt của**: Product Requirement Document (Tài liệu yêu cầu sản phẩm)

**Giải thích một câu**: Tài liệu mô tả sản phẩm "làm cái gì".

**Thường bao gồm**:

- Mục tiêu sản phẩm
- Người dùng là ai
- Chức năng cốt lõi
- Không bao gồm cái gì

**Giá trị đối với lập trình AI**:
Có PRD, AI có thể hiểu chính xác hơn nhu cầu của bạn, code sinh ra càng phù hợp với mong đợi.

## Debug

**Giải thích một câu**: Tìm và sửa lỗi trong code.

**Ví dụ tương tự**: Giống như tìm nguyên nhân tại sao đèn không sáng — do bóng hỏng? Hay chưa bật công tắc? Hay mất điện?

**Phương pháp Debug thường gặp**:

- Xem thông báo lỗi
- Thêm `console.log` để in giá trị biến
- Kiểm tra code từng dòng một
- Hỏi AI

## Deploy (Triển khai)

**Giải thích một câu**: Đưa thứ bạn làm lên mạng, để người khác truy cập được.

**Ví dụ tương tự**: Giống như biến bản thảo sách thành sách in được bày bán trên kệ.

**Nền tảng triển khai thường dùng**:

- Vercel
- Netlify
- GitHub Pages

## Git

**Giải thích một câu**: Công cụ quản lý phiên bản code, có thể ghi lại mỗi lần sửa đổi, quay lại bất cứ lúc nào.

**Ví dụ tương tự**: Giống như chức năng lưu game save. Chơi sai có thể load lại save quay về trạng thái trước đó.

**Khái niệm cốt lõi**:
| Khái niệm | Giải thích |
|------|------|
| Repository (Kho) | Nơi chứa dự án |
| Commit (Gửi) | Lưu lại một bản ghi sửa đổi |
| Branch (Nhánh) | Phiên bản song song của code |
| Push (Đẩy) | Tải code từ máy lên đám mây |
| Pull (Kéo) | Tải code từ đám mây về máy |

## GitHub

**Giải thích một câu**: Nền tảng lưu trữ code lớn nhất, dựa trên Git.

**Ví dụ tương tự**: Giống như "Google Drive của giới code", code của bạn được lưu trên mây, truy cập mọi lúc mọi nơi.

**Công dụng thường gặp**:

- Lưu trữ và sao lưu code
- Cộng tác phát triển với người khác
- Trưng bày dự án của bạn
- Tìm dự án mã nguồn mở để học tập

## API

**Viết tắt của**: Application Programming Interface (Giao diện lập trình ứng dụng)

**Giải thích một câu**: "Ám hiệu" để các chương trình giao tiếp với nhau.

**Ví dụ tương tự**: Giống như thực đơn nhà hàng. Bạn gọi món theo thực đơn (gửi yêu cầu), nhà bếp làm cho bạn (trả về kết quả). Bạn không cần biết nhà bếp làm như thế nào.

**Ví dụ**:

- API Thời tiết: Bạn gửi yêu cầu "Thời tiết Hà Nội", nó trả về "Nắng, 30°C"
- API Bản đồ: Bạn gửi yêu cầu "Từ A đến B", nó trả về lộ trình

## Framework (Khung sườn)

**Giải thích một câu**: Bộ khung code người khác viết sẵn, bạn chỉ cần điền nội dung vào là được.

**Ví dụ tương tự**: Giống như xếp hình. Framework cung cấp cấu trúc cơ bản, bạn chỉ cần bỏ nội dung vào bên trong.

**Framework thường gặp**:
| Framework | Công dụng |
|------|------|
| React / Vue | Làm giao diện web |
| Next.js | Làm website hoàn chỉnh |
| Express | Làm dịch vụ backend |

## Frontend vs Backend

|                | Frontend                           | Backend                         |
| -------------- | ---------------------------------- | ------------------------------- |
| Là gì          | Phần người dùng nhìn thấy          | Phần người dùng không nhìn thấy |
| Ví dụ tương tự | Trang trí và thực đơn của nhà hàng | Nhà bếp và kho hàng             |
| Phụ trách      | Giao diện, tương tác, hiệu ứng     | Xử lý dữ liệu, lưu trữ, logic   |
| Công nghệ      | HTML/CSS/JS                        | Node.js/Python/Database         |

## Fullstack

**Giải thích một câu**: Biết cả Frontend và Backend.

**Ví dụ tương tự**: Vừa biết thiết kế trang trí nhà hàng, vừa biết nấu ăn trong bếp.

**Trong kỷ nguyên AI**:
Nhờ có AI, người bình thường cũng có thể làm ứng dụng "Fullstack" — bởi vì AI có thể giúp bạn xử lý những phần bạn không sở trường.
