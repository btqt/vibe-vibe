---
title: "4.3 Cách đọc hiểu code AI sinh ra"
description: "Hiểu 4 khái niệm cốt lõi của code"
chapter: "Chương 4"
priority: "🟢"
---

# 4.3 Cách đọc hiểu code AI sinh ra 🟢

> **Đọc xong phần này, bạn sẽ thu hoạch được:**
>
> - Hiểu 4 khái niệm cốt lõi: biến, hàm, điều kiện, vòng lặp
> - Có khả năng đọc code AI sinh ra và hiểu logic của nó
> - Học cách dùng mã giả (pseudocode) để mô tả nhu cầu cho AI
> - Hiểu rằng cùng một chức năng có thể có nhiều cách hiện thực hóa

> Mọi ngôn ngữ lập trình, dù cú pháp khác nhau thế nào, đều dựa trên vài khái niệm cốt lõi.

---

## Dẫn nhập

Tài liệu kỹ thuật mô tả hệ thống làm gì, nhưng hiện thực hóa cuối cùng phải dựa vào code. Bạn không cần tự tay viết từng dòng code, nhưng cần hiểu logic cơ bản của code —— có thế mới đọc hiểu code AI sinh ra, biết nó đang làm gì, và có năng lực tra soát khi gặp vấn đề.

Ngôn ngữ lập trình có hàng trăm loại, cú pháp mỗi loại một khác, nhưng chúng đều dựa trên vài khái niệm cốt lõi chung. Hiểu những khái niệm này giống như học được "bảng chữ cái" để đọc code vậy.

---

## 4 cấu kiện cơ bản của code

Khi bạn bảo AI sinh code, bản chất là nó đang tổ hợp 4 nguyên tố cơ bản này. Hiểu chúng sẽ giúp bạn đọc code và biết nó đang làm gì.

### Biến (Variable): Vật chứa dữ liệu

**Biến** là vật chứa để lưu trữ dữ liệu. Bạn có thể tưởng tượng nó như cái hộp có dán nhãn —— trong hộp chứa dữ liệu, nhãn là tên biến.

Ví dụ `let username = "Trương Tam"` chính là tạo một cái hộp tên là `username`, bên trong chứa "Trương Tam". Sau đó bạn có thể lấy giá trị này ra dùng bất cứ lúc nào, hoặc đổi nội dung trong hộp thành cái khác.

Biến giúp code có thể "ghi nhớ" thông tin. Trạng thái đăng nhập của người dùng, sản phẩm trong giỏ hàng, tiêu đề bài viết —— tất cả đều là dữ liệu được lưu trong biến.

### Hàm (Function): Khối lệnh tái sử dụng

**Hàm** là khối lệnh có thể tái sử dụng. Khi bạn phát hiện mình đang viết đi viết lại những đoạn code giống nhau, đó là lúc nên đóng gói nó thành hàm.

Hàm nhận đầu vào (tham số), thực hiện xử lý, rồi trả về đầu ra. Ví dụ một hàm tính tổng giá tiền sản phẩm:

- Đầu vào: Đơn giá, Số lượng
- Xử lý: Đơn giá × Số lượng
- Đầu ra: Tổng giá

Sau khi định nghĩa hàm, mỗi lần cần tính tổng giá, chỉ cần gọi hàm này và truyền tham số khác nhau vào, không cần viết lại logic tính toán nữa.

### Điều kiện (Condition): Ngã rẽ

**Phán đoán điều kiện** giúp chương trình có thể thực hiện hành động khác nhau tùy theo tình huống.

```
if (Người dùng đã đăng nhập) {
  Hiển thị thông tin chào mừng
} else {
  Hiển thị nút đăng nhập
}
```

Đây chính là phán đoán điều kiện —— chương trình dựa vào điều kiện "người dùng có đăng nhập hay không" để quyết định chạy đoạn code nào. Nó giống như một ngã rẽ, chương trình chọn đường đi dựa trên điều kiện.

### Vòng lặp (Loop): Sức mạnh của sự lặp lại

**Vòng lặp** giúp chương trình thực hiện lặp đi lặp lại một thao tác nào đó.

Ví dụ bạn muốn gửi email cho 1000 người dùng, không cần viết 1000 lần code gửi mail, chỉ cần viết một vòng lặp: "Với mỗi người dùng trong danh sách, gửi email cho họ".

Bản chất của vòng lặp là: **Dùng mô tả ngắn gọn để hoàn thành lượng lớn công việc lặp lại**.

---

## Tính đầy đủ Turing (Turing Completeness): Sức mạnh của 4 cấu kiện

Bốn khái niệm này —— biến, hàm, điều kiện, vòng lặp —— là nền tảng của **tính đầy đủ Turing**. Điều này có nghĩa là bất kỳ vấn đề nào có thể tính toán được, đều có thể giải quyết bằng sự tổ hợp của 4 cấu kiện này.

Từ cái máy tính bỏ túi đơn giản đến trí tuệ nhân tạo phức tạp, từ biểu mẫu web đến hệ điều hành, tầng đáy đều là sự tổ hợp khác nhau của 4 khái niệm này.

Khi bạn đọc code, hãy thử nhận diện 4 nguyên tố này:

- Dữ liệu ở đâu? → **Biến**
- Thao tác được đóng gói ở đâu? → **Hàm**
- Tình huống nào thì thực hiện cái gì? → **Điều kiện**
- Cái gì đang được thực hiện lặp lại? → **Vòng lặp**

---

## Mã giả (Pseudocode): Cầu nối đối thoại với AI

Hiểu cấu kiện cơ bản của code, bạn sẽ đọc hiểu logic code đơn giản. Nhưng quan trọng hơn, bạn có thể dùng những khái niệm này để mô tả chức năng mong muốn cho AI —— đây chính là tác dụng của mã giả.

**Mã giả** là cách diễn đạt nằm giữa ngôn ngữ tự nhiên và code chính thức. Nó dùng cấu trúc logic của lập trình (điều kiện, vòng lặp...) để mô tả nhu cầu but không cần tuân thủ cú pháp cụ thể.

Ví dụ bạn muốn AI viết giúp chức năng đăng nhập, có thể dùng mã giả mô tả:

```
Khi người dùng bấm nút đăng nhập:
    Lấy email và mật khẩu từ ô nhập liệu
    Kiểm tra định dạng email có đúng không
    Nếu định dạng đúng:
        Gửi request lên server xác thực
        Nếu xác thực thành công:
            Chuyển hướng về trang chủ
        Nếu không:
            Hiển thị "Sai mật khẩu"
    Nếu không:
        Hiển thị "Định dạng email không đúng"
```

Cách mô tả này rõ ràng hơn nhiều so với ngôn ngữ tự nhiên thuần túy, lại không bắt buộc bạn phải nắm vững cú pháp cụ thể. AI có thể hiểu mã giả rất tốt và giúp bạn chuyển đổi nó thành code chính thức.

---

## Tư duy thuật toán: Tại sao cùng một chức năng, code lại khác nhau

Khi dùng mã giả mô tả nhu cầu, AI có thể đưa ra các phương án hiện thực hóa khác nhau. Các phương án này đều hoàn thành chức năng, nhưng các bước thực hiện có thể khác nhau.

Lấy ví dụ: Tìm một email nào đó trong 1000 người dùng.

**Phương án 1**: Kiểm tra từng người một, trường hợp tệ nhất phải kiểm tra 1000 lần.

**Phương án 2**: Nếu người dùng đã được sắp xếp theo email, kiểm tra người ở giữa trước. Nếu email cần tìm nằm ở phía sau, thì chỉ cần kiểm tra nửa sau danh sách, cứ lặp lại như vậy (Tìm kiếm nhị phân). Cách này tối đa chỉ cần kiểm tra 10 lần.

Hai phương án đều hoàn thành nhiệm vụ, nhưng phương án 2 ít bước hơn. Khi bạn bảo AI sinh code, nếu liên quan đến lượng dữ liệu lớn, có thể nhắc nhẹ nó "dữ liệu lớn lắm nhé, dùng phương pháp tìm kiếm hiệu quả vào" —— AI sẽ hiểu ý bạn.

---

## Trọng điểm cốt lõi

- ✅ Biến là vật chứa dữ liệu
- ✅ Hàm là đơn vị tái sử dụng thao tác
- ✅ Phán đoán điều kiện giúp chương trình rẽ nhánh thực thi
- ✅ Vòng lặp giúp chương trình thực thi lặp lại
- ✅ Mã giả là công cụ dùng logic lập trình để mô tả nhu cầu
- ✅ Cùng một chức năng có thể có cách hiện thực hóa khác nhau, AI sẽ chọn phương án phù hợp

Hiểu cấu kiện cơ bản của lập trình rồi, tiếp theo sẽ học kiến thức cơ bản về API và giao tiếp HTTP.

---

## Nội dung liên quan

- Trước đó: [4.2 Mối quan hệ giữa PRD và Tài liệu kỹ thuật](./02-prd-and-tech-docs_vi.md)
- Chi tiết: [4.4 Cơ bản về API và HTTP](./04-api-and-http_vi.md)
