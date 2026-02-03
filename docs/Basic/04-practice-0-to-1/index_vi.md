---
title: "Chương 4: Thực chiến —— Phát triển công cụ cá nhân từ 0 đến 1"
---


![04-practice-0-to-1_index.png](../../public/images/Basic/04-practice-0-to-1_index.png)
# Chương 4: Thực chiến —— Phát triển công cụ cá nhân từ 0 đến 1

> **Định vị chương**: Chương này là chương thực hành cốt lõi của Vibe Coding, đưa tư duy và kỹ thuật đã học ở ba chương trước vào thực tế, cầm tay chỉ việc dẫn dắt bạn hoàn thành dự án lập trình AI hoàn chỉnh đầu tiên.

## Từ "Bàn việc trên giấy" đến "Múa đao múa thương"

Ở ba chương trước, chúng ta đã hoàn thành công tác chuẩn bị quan trọng:

| Chương | Bạn học được gì | Ẩn dụ |
|------|-------------|------|
| Chương 1 Thức tỉnh | Hiểu Vibe Coding là gì | Nhận biết thế giới mới |
| Chương 2 Tâm pháp | Dùng tư duy giám đốc sản phẩm nghĩ cho rõ cần làm gì | Viết kịch bản hay |
| Chương 3 Kỹ thuật | Dùng phương pháp cấu trúc hóa để giao tiếp hiệu quả với AI | Học ngôn ngữ đạo diễn |
| **Chương 4 Thực chiến** | **Thực sự bắt tay làm ra một sản phẩm** | **Diễn!** |

Chương này, chúng ta sẽ dùng hết tất cả những gì đã học ở trước đó —— **làm ra một thứ thực sự dùng được**.

Không phải nhìn người khác làm, không phải tưởng tượng đang làm, mà là chính tay bạn làm ra.

## Tại sao chọn "Danh sách việc cần làm" làm dự án đầu tiên

Bạn có thể sẽ hỏi: Sao không làm cái gì đó ngầu hơn? Ví dụ như AI chatbot, trình tạo ảnh?

Chúng tôi chọn "Danh sách việc cần làm cá nhân", có ba lý do quan trọng:

### 1. Bao hàm trọn vẹn thao tác CRUD

| Thao tác | Tiếng Anh | Thể hiện trong danh sách việc cần làm |
|------|------|-------------------|
| Tạo | Create | Thêm nhiệm vụ mới |
| Đọc | Read | Hiển thị danh sách nhiệm vụ |
| Cập nhật | Update | Đánh dấu nhiệm vụ hoàn thành |
| Xóa | Delete | Xóa nhiệm vụ |

Bốn thao tác này là nền tảng của hầu hết mọi ứng dụng. Học được cái này, làm dự án khác chỉ là thay đổi lớp vỏ thôi.

### 2. Kết nối liền mạch với ví dụ chương 2

Còn nhớ Tiểu Lý ở chương 2 không? Cậu ấy muốn làm một danh sách việc cần làm để quản lý nhiệm vụ của mình. Ở chương 2 chúng ta đã giúp cậu ấy làm:
- Phân tích 3 câu hỏi linh hồn
- Chân dung người dùng
- Định nghĩa chức năng MVP
- PRD đơn giản

Bây giờ, chúng ta sẽ **biến ý tưởng của Tiểu Lý thành hiện thực**.

### 3. Làm xong dùng được thật

Đây không phải là một "dự án luyện tập" —— sau khi làm xong, bạn thực sự có thể dùng nó để quản lý các công việc cần làm của mình. Làm mới trang dữ liệu vẫn còn, mở trên điện thoại cũng được. Cảm giác thành tựu kiểu "thứ mình làm ra dùng được thật" này là động lực lớn nhất để học lập trình.

## Chương này tích hợp nội dung các chương trước như thế nào

| Đến từ chương | Bạn sẽ dùng | Dùng ở đâu |
|---------|---------|---------|
| Chương 2 Tâm pháp | PRD của Tiểu Lý, 3 câu hỏi linh hồn, Định nghĩa MVP | 4.1 Xác định rõ cần làm gì |
| Chương 3 Kỹ thuật | Khung S.C.A.F.F., kỹ năng đối thoại lặp lại | 4.2-4.4 Viết Prompt, điều chỉnh tối ưu |

Chương này là "sân diễn tập thực chiến" của hai chương trước —— Chương 2 dạy bạn nghĩ cho kỹ, chương 3 dạy bạn nói cho rõ, chương này để bạn thực sự làm ra sản phẩm.

## Mục tiêu học tập chương này

Sau khi hoàn thành chương này, bạn sẽ:

- ✅ Độc lập hoàn thành một ứng dụng web hoàn chỉnh bao gồm chức năng thêm xóa sửa tra cứu
- ✅ Nắm vững quy trình làm việc trọn vẹn từ ý tưởng đến sản phẩm
- ✅ Học cách sử dụng AI IDE để phát triển
- ✅ Có khả năng debug và sửa chữa khi mã AI bị lỗi
- ✅ Hiểu khái niệm cơ bản về lưu trữ dữ liệu (localStorage)
- ✅ Sở hữu một tác phẩm thực tế có thể khoe với bạn bè

## Xem trước cấu trúc chương này

```
4.1 Bắt đầu trước đó → Tích hợp công tác chuẩn bị, chọn công cụ
4.2 Vòng 1: Dựng trang → Làm cái "mặt tiền" trước
4.3 Vòng 2: Thực hiện chức năng → Để nó phản hồi thao tác
4.4 Vòng 3: Lưu trữ dữ liệu → Để nó nhớ dữ liệu của bạn
4.5 Thực chiến Debug → Khi mã AI báo lỗi thì làm thế nào
4.6 Kết thúc và ôn tập → Trưng bày dự án hoàn chỉnh và tổng kết kinh nghiệm
```

## Thời gian dự kiến

| Tiết | Thời gian dự kiến | Độ khó |
|------|---------|------|
| 4.1 Bắt đầu trước đó | 15 phút | ⭐ |
| 4.2 Dựng trang | 20 phút | ⭐ |
| 4.3 Thực hiện chức năng | 30 phút | ⭐⭐ |
| 4.4 Lưu trữ dữ liệu | 20 phút | ⭐⭐ |
| 4.5 Thực chiến Debug | 20 phút | ⭐⭐ |
| 4.6 Kết thúc ôn tập | 15 phút | ⭐ |
| **Tổng cộng** | **Khoảng 2 tiếng** | |

::: tip 💡 Gợi ý
Có thể làm một mạch cho xong, cũng có thể chia thành 2-3 lần. Mỗi khi hoàn thành một vòng đều có thành quả giai đoạn, có thể tạm dừng bất cứ lúc nào.
:::

## Sẵn sàng chưa?

Hãy cùng bắt tay vào làm!

→ [4.1 Bắt đầu trước đó](./4.1-before-start/)
