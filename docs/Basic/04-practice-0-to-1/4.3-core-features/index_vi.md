---
title: "4.3 Vòng 2: Thực hiện chức năng cốt lõi"
order: 1
---


![04-practice-0-to-1_4.3-core-features_index.png](../../../public/images/Basic/04-practice-0-to-1_4.3-core-features_index.png)
# 4.3 Vòng 2: Thực hiện chức năng cốt lõi

> **Mục tiêu vòng này**: Để trang web phản hồi thao tác người dùng - nhấp nút thực sự có phản ứng

Ở vòng trước (4.2), bạn đã làm ra một cái "vỏ rỗng đẹp mắt": có tiêu đề, ô nhập liệu, nút bấm, khu vực danh sách. Nhưng nếu bây giờ bạn nhấp nút "Thêm", sẽ chẳng có chuyện gì xảy ra cả.

Điều này giống như làm ra một chiếc xe hơi đẹp đẽ, nhưng chưa lắp động cơ.

**Vòng này, chúng ta sẽ lắp "động cơ" cho nó** - để mỗi nút bấm đều thực sự hoạt động.

## Từ "Tĩnh" sang "Động"

Ở phần 4.2, chúng ta dùng HTML và CSS dựng trang. Bây giờ cần thêm JavaScript, để trang có thể "phản hồi" thao tác của người dùng.

| Khái niệm | So sánh | Biểu hiện trong danh sách việc cần làm |
|------|------|-------------------|
| HTML | Khung xương ngôi nhà | Cấu trúc ô nhập liệu, nút bấm, danh sách |
| CSS | Trang trí ngôi nhà | Màu sắc, phông chữ, bố cục |
| JavaScript | Mạch điện và công tắc | Logic phản hồi sau khi nhấp nút |

Bạn không cần "học thuộc" JavaScript. Bạn chỉ cần nói cho AI biết bạn muốn hiệu quả gì, AI sẽ giúp bạn viết mã.

## Ba chức năng cần thực hiện trong vòng này

Còn nhớ chức năng P0 đã định nghĩa ở chương 2 không? Vòng này chúng ta sẽ thực hiện 3 chức năng cốt lõi nhất:

| Chức năng | Thao tác người dùng | Kết quả mong đợi |
|------|---------|---------|
| Thêm nhiệm vụ | Nhập nội dung, nhấp nút "Thêm" | Nhiệm vụ mới xuất hiện trong danh sách |
| Xóa nhiệm vụ | Nhấp nút "Xóa" bên cạnh nhiệm vụ | Nhiệm vụ đó biến mất khỏi danh sách |
| Đánh dấu hoàn thành | Nhấp nút "Hoàn thành" của nhiệm vụ | Nhiệm vụ hiển thị trạng thái hoàn thành (có gạch ngang) |

Ba chức năng này bao gồm các thao tác "Thêm, Xóa, Sửa", là mô hình cơ bản của hầu hết các ứng dụng.

## Xử lý sự kiện: Để trang web "nghe hiểu" thao tác của bạn

Trước khi bắt đầu, hãy hiểu một khái niệm cốt lõi: **Xử lý sự kiện**.

Tưởng tượng bạn gọi món trong nhà hàng:

1. Bạn nhấn nút gọi nhân viên phục vụ (**Kích hoạt sự kiện**)
2. Nhân viên nghe thấy tiếng chuông (**Lắng nghe sự kiện**)
3. Nhân viên đi tới phục vụ bạn (**Thực hiện phản hồi**)

Logic xử lý sự kiện của JavaScript cũng vậy:

```
Người dùng nhấp nút → Chú trình lắng nghe thấy cú nhấp → Thực thi mã tương ứng
```

Bạn không cần tự viết những đoạn mã này. Chỉ cần nói với AI: "Khi người dùng nhấp nút thêm, hãy thêm nội dung đã nhập vào danh sách", AI sẽ giúp bạn thực hiện.

## Quy trình làm việc vòng này

```
4.3.1 Thêm nhiệm vụ → Để nút "Thêm" dùng được
       ↓
4.3.2 Xóa nhiệm vụ → Để nút "Xóa" dùng được
       ↓
4.3.3 Đánh dấu hoàn thành → Để nút "Hoàn thành" dùng được
       ↓
4.3.4 Tối ưu hóa lặp lại → Điều chỉnh những chỗ chưa hài lòng
       ↓
4.3.5 Kiểm tra giai đoạn → Xác nhận mọi chức năng bình thường
```

Mỗi khi hoàn thành một chức năng, đều phải kiểm tra xác nhận có thể sử dụng bình thường, rồi mới vào bước tiếp theo.

## Điều hướng chương

| Tiểu tiết | Chủ đề | Thời gian dự kiến |
|------|------|---------|
| [4.3.1](./4.3.1-add-task_vi.md) | Chức năng 1: Thêm nhiệm vụ | 10 phút |
| [4.3.2](./4.3.2-delete-task_vi.md) | Chức năng 2: Xóa nhiệm vụ | 8 phút |
| [4.3.3](./4.3.3-complete-task_vi.md) | Chức năng 3: Đánh dấu hoàn thành | 8 phút |
| [4.3.4](./4.3.4-iterate_vi.md) | Nghệ thuật tối ưu hóa lặp lại | 7 phút |
| [4.3.5](./4.3.5-checkpoint_vi.md) | Kiểm tra kết quả giai đoạn | 2 phút |

**Tổng thời gian dự kiến: Khoảng 35 phút**

::: tip 💡 Nhắc nhở ấm áp
Nếu chức năng nào đó thực hiện xong mà chưa đúng lắm, đừng vội. Phần 4.3.4 sẽ chuyên nói về cách truy vấn và điều chỉnh. Cứ làm theo trước đã, gặp vấn đề thì ghi lại.
:::

## Đã chuẩn bị xong chưa?

Đảm bảo bạn đã hoàn thành phần 4.2, có một trang tĩnh hiển thị bình thường.

Hãy bắt đầu "lắp động cơ" cho nó nào!

→ [4.3.1 Chức năng 1: Thêm nhiệm vụ](./4.3.1-add-task_vi.md)
