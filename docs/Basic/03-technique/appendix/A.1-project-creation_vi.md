---
title: "A.1 Mẫu tạo dự án"
---


![03-technique_appendix_A.1-project-creation.png](../../../public/images/Basic/03-technique_appendix_A.1-project-creation.png)
# A.1 Mẫu tạo dự án

Phần này cung cấp các mẫu Prompt để tạo dự án từ con số 0, bao phủ các tình huống phổ biến như ứng dụng web, phân tích dữ liệu, script tự động hóa.

## Mẫu 1: Dựng ứng dụng web từ con số 0

Thích hợp cho: Công cụ cá nhân, nguyên mẫu sản phẩm, trang web nhỏ

```markdown
## Bối cảnh dự án

Tôi muốn tạo một [Loại dự án].

**Người dùng mục tiêu**: [Ai sẽ sử dụng ứng dụng này]
**Nhu cầu cốt lõi**: [Mô tả bằng một câu ứng dụng này giải quyết vấn đề gì]

## Yêu cầu kỹ thuật

**Ưu tiên Stack kỹ thuật**:
- Frontend: [React/Vue/HTML+CSS+JS thuần/Không giới hạn]
- Style: [Tailwind CSS/CSS thuần/Không giới hạn]
- Có cần backend không: [Có/Không]
- Lưu trữ dữ liệu: [localStorage/Không cần lưu trữ/Cần cơ sở dữ liệu]

**Trình độ kỹ thuật của tôi**: [Số 0/Có chút nền tảng/Thành thạo frontend]

## Nhu cầu chức năng

**Bắt buộc phải có (P0)**:
- [ ] [Chức năng 1]
- [ ] [Chức năng 2]
- [ ] [Chức năng 3]

**Tạm thời chưa cần**:
- [Chức năng A] (Nguyên nhân: [Tại sao chưa cần])
- [Chức năng B] (Nguyên nhân: [Tại sao chưa cần])

## Yêu cầu giao diện

**Phong cách**: [Tối giản/Hiện đại/Dễ thương/Chuyên nghiệp/Tham khảo trang web nào đó]
**Phối màu**: [Màu chủ đạo ưu tiên, ví dụ "Trắng xanh"/"Chủ đề tối"]
**Responsive**: [Cần thích ứng mobile/Chỉ cần desktop]

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Mô tả cấu trúc file của dự án
2. File code hoàn chỉnh
3. Hướng dẫn cách chạy trên máy local
```

### Ví dụ điền mẫu: Sổ thu chi cá nhân

```markdown
## Bối cảnh dự án

Tôi muốn tạo một ứng dụng web ghi chép thu chi tối giản.

**Người dùng mục tiêu**: Chính tôi (Muốn rèn thói quen ghi chép nhưng ngại các App khác quá phức tạp)
**Nhu cầu cốt lõi**: Ghi nhanh mỗi khoản chi, cuối tháng thấy được tổng chi tiêu

## Yêu cầu kỹ thuật

**Ưu tiên Stack kỹ thuật**:
- Frontend: HTML+CSS+JS thuần (Tôi là người mới, muốn bắt đầu từ cái đơn giản)
- Style: CSS thuần
- Có cần backend không: Không
- Lưu trữ dữ liệu: localStorage

**Trình độ kỹ thuật của tôi**: Số 0, vừa học xong Hello World

## Nhu cầu chức năng

**Bắt buộc phải có (P0)**:
- [ ] Ghi chép chi tiêu: Số tiền + Ghi chú đơn giản
- [ ] Hiển thị danh sách chi tiêu hôm nay
- [ ] Hiển thị tổng chi tiêu tháng này
- [ ] Xóa bản ghi sai

**Tạm thời chưa cần**:
- Ghi thu nhập (Nguyên nhân: Tôi chỉ muốn quản lý chi tiêu)
- Thống kê theo phân loại (Nguyên nhân: Chạy được đã, sau này thêm sau)
- Biểu đồ trực quan hóa (Nguyên nhân: Con số đủ rồi, không cần màu mè)

## Yêu cầu giao diện

**Phong cách**: Tối giản, cảm giác sạch sẽ giống Ghi chú iOS
**Phối màu**: Nền trắng, chữ xám đậm, màu nhấn xanh lá
**Responsive**: Cần thích ứng mobile (Tôi chủ yếu dùng trên điện thoại)

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Mô tả cấu trúc file của dự án
2. File code hoàn chỉnh
3. Hướng dẫn cách chạy trên máy local
```

## Mẫu 2: Dự án phân tích dữ liệu

Thích hợp cho: Xử lý dữ liệu Excel, phân tích bán hàng, thống kê bảng hỏi, báo cáo trực quan hóa

```markdown
## Bối cảnh phân tích

Tôi cần phân tích một bộ dữ liệu [Loại dữ liệu].

**Nguồn dữ liệu**: [Excel/CSV/Cơ sở dữ liệu/API]
**Quy mô dữ liệu**: Khoảng [Số dòng] dòng, [Số cột] cột
**Mục đích phân tích**: [Trả lời câu hỏi nghiệp vụ gì/Hỗ trợ quyết định gì]

## Mô tả dữ liệu

**Các trường chính**:
| Tên trường | Ý nghĩa | Loại dữ liệu | Giá trị mẫu |
|-------|------|---------|-------|
| [Trường 1] | [Giải thích] | [Văn bản/Số/Ngày tháng] | [Ví dụ] |
| [Trường 2] | [Giải thích] | [Văn bản/Số/Ngày tháng] | [Ví dụ] |

**Vấn đề chất lượng dữ liệu** (nếu có):
- [Vấn đề 1, ví dụ "Một số định dạng ngày tháng không thống nhất"]
- [Vấn đề 2, ví dụ "Một số dòng thiếu dữ liệu số tiền"]

## Nhu cầu phân tích

**Câu hỏi muốn trả lời**:
1. [Câu hỏi 1]
2. [Câu hỏi 2]
3. [Câu hỏi 3]

**Hình thức đầu ra**:
- [ ] Bảng dữ liệu sau khi làm sạch
- [ ] Con số thống kê (như tổng, trung bình, tỷ trọng)
- [ ] Biểu đồ trực quan hóa (Cột/Đường/Tròn)
- [ ] Văn bản giải thích kết luận phân tích

## Yêu cầu kỹ thuật

**Công cụ sử dụng**: [Python + Pandas / Công thức Excel / SQL]
**Môi trường chạy**: [Python local / Jupyter Notebook / Google Colab]
**Trình độ của tôi**: [Số 0/Biết Python cơ bản/Thành thạo phân tích dữ liệu]

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Code hoàn chỉnh (kèm chú thích giải thích từng bước đang làm gì)
2. Ví dụ kết quả mong đợi sau khi chạy code
3. Cách sửa code để thích ứng với dữ liệu thực tế của tôi
```

### Ví dụ điền mẫu: Phân tích doanh số bán hàng hàng tháng

```markdown
## Bối cảnh phân tích

Tôi cần phân tích một bộ dữ liệu bán hàng thương mại điện tử.

**Nguồn dữ liệu**: File Excel (Xuất từ backend)
**Quy mô dữ liệu**: Khoảng 5000 dòng, 8 cột
**Mục đích phân tích**: Tìm hiểu tình hình bán hàng tháng này, tìm ra sản phẩm bán chạy và sản phẩm có vấn đề

## Mô tả dữ liệu

**Các trường chính**:
| Tên trường | Ý nghĩa | Loại dữ liệu | Giá trị mẫu |
|-------|------|---------|-------|
| Mã đơn hàng | Định danh duy nhất | Văn bản | ORD20241201001 |
| Tên sản phẩm | Tên sản phẩm | Văn bản | Tai nghe bluetooth không dây |
| Phân loại | Loại sản phẩm | Văn bản | Phụ kiện số |
| Số tiền | Số tiền đơn hàng | Số | 299 |
| Thời gian đặt | Thời gian đặt hàng | Ngày tháng | 2024-12-01 14:30 |

**Vấn đề chất lượng dữ liệu**:
- Một số đơn hàng có số tiền là 0 (có thể là đơn hoàn tiền)
- Định dạng thời gian đặt hàng có hai kiểu: Có cái kèm giờ phút, có cái chỉ có ngày tháng

## Nhu cầu phân tích

**Câu hỏi muốn trả lời**:
1. Tổng doanh số tháng này là bao nhiêu? Doanh số trung bình ngày?
2. Loại sản phẩm nào bán chạy nhất? Chiếm tỷ trọng bao nhiêu?
3. Những sản phẩm nào nằm trong Top 10 bán chạy?
4. Xu hướng doanh số hàng ngày như thế nào?

**Hình thức đầu ra**:
- [x] Con số thống kê (Tổng, trung bình ngày, tỷ trọng phân loại)
- [x] Biểu đồ trực quan hóa (Biểu đồ tròn phân loại, biểu đồ đường xu hướng ngày, biểu đồ cột Top 10)
- [x] Văn bản giải thích kết luận phân tích

## Yêu cầu kỹ thuật

**Công cụ sử dụng**: Python + Pandas + Matplotlib
**Môi trường chạy**: Jupyter Notebook local
**Trình độ của tôi**: Biết Python cơ bản, Pandas dùng chưa thạo

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Code hoàn chỉnh (kèm chú thích giải thích từng bước đang làm gì)
2. Ví dụ kết quả mong đợi sau khi chạy code
3. Cách sửa code để thích ứng với dữ liệu thực tế của tôi
```

## Mẫu 3: Script tự động hóa

Thích hợp cho: Xử lý file hàng loạt, tổng hợp Excel, tác vụ định giờ, cào dữ liệu

```markdown
## Nhu cầu tự động hóa

Tôi muốn tự động hoàn thành [Mô tả nhiệm vụ].

**Nỗi đau hiện tại**:
[Mô tả hiện tại làm thủ công phiền phức thế nào]

**Hiệu quả kỳ vọng**:
[Sau khi chạy script, chuyện gì sẽ xảy ra]

## Đầu vào Đầu ra

**Đầu vào**:
- Nguồn: [Thư mục/File đơn lẻ/Trang web/...]
- Định dạng: [Excel/CSV/TXT/Ảnh/...]
- Vị trí: [Đường dẫn cụ thể hoặc mô tả]
- Ví dụ: [Cho một ví dụ cụ thể]

**Đầu ra**:
- Định dạng: [Excel/CSV/File mới/...]
- Vị trí: [Lưu vào đâu]
- Quy tắc đặt tên: [Ví dụ "Tên_gốc_processed.xlsx"]

## Logic xử lý

Vui lòng xử lý theo các bước sau:
1. [Bước 1: Làm gì]
2. [Bước 2: Làm gì]
3. [Bước 3: Làm gì]

**Xử lý trường hợp đặc biệt**:
- Nếu gặp [Trường hợp A], thì [Cách xử lý]
- Nếu gặp [Trường hợp B], thì [Cách xử lý]

## Yêu cầu kỹ thuật

**Ngôn ngữ**: [Python/Script batch/PowerShell]
**Môi trường chạy**: [Windows/Mac/Linux]
**Hạn chế phụ thuộc**: [Hạn chế dùng thư viện bên thứ ba/Có thể dùng thư viện phổ biến]
**Trình độ của tôi**: [Biết chạy script là được/Muốn học hiểu code]

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Code script hoàn chỉnh có thể chạy được
2. Các thư viện phụ thuộc cần cài đặt (như pip install xxx)
3. Hướng dẫn sử dụng (cách chạy, cách sửa tham số)
4. Vấn đề thường gặp và cách giải quyết
```

### Ví dụ điền mẫu: Đổi tên ảnh hàng loạt

```markdown
## Nhu cầu tự động hóa

Tôi muốn tự động đổi tên hàng loạt ảnh trong thư mục.

**Nỗi đau hiện tại**:
Ảnh xuất từ máy ảnh có tên kiểu IMG_0001.jpg, rất khó tìm ảnh của ngày cụ thể.
Đổi tên thủ công mấy trăm cái ảnh tốn thời gian quá.

**Hiệu quả kỳ vọng**:
Sau khi chạy script, tất cả ảnh được đổi tên theo định dạng 2024-12-01_001.jpg dựa trên ngày chụp.

## Đầu vào Đầu ra

**Đầu vào**:
- Nguồn: Thư mục chỉ định
- Định dạng: Ảnh jpg, png
- Vị trí: Người dùng chỉ định (nhập khi chạy)
- Ví dụ: IMG_0001.jpg, IMG_0002.jpg...

**Đầu ra**:
- Định dạng: Ảnh gốc (chỉ đổi tên, không sửa nội dung)
- Vị trí: Đổi tên tại chỗ
- Quy tắc đặt tên: Ngày_chụp_Số_thứ_tự.phần_mở_rộng (ví dụ 2024-12-01_001.jpg)

## Logic xử lý

Vui lòng xử lý theo các bước sau:
1. Đọc tất cả ảnh trong thư mục
2. Trích xuất ngày chụp từ thông tin EXIF của ảnh
3. Sắp xếp theo ngày, ảnh cùng ngày đánh số theo thời gian
4. Đổi tên file

**Xử lý trường hợp đặc biệt**:
- Nếu ảnh không có thông tin EXIF, dùng thời gian sửa đổi file
- Nếu tên file đích đã tồn tại, thêm hậu tố _dup

## Yêu cầu kỹ thuật

**Ngôn ngữ**: Python
**Môi trường chạy**: Windows 11
**Hạn chế phụ thuộc**: Có thể dùng thư viện Pillow để đọc EXIF
**Trình độ của tôi**: Biết chạy script là được, code không cần chú thích quá chi tiết

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Code script hoàn chỉnh có thể chạy được
2. Các thư viện phụ thuộc cần cài đặt
3. Hướng dẫn sử dụng (cách chạy)
```

## Mẫu 4: Công cụ dòng lệnh CLI (Bản rút gọn)

Thích hợp cho: Công cụ cho developer, script hiệu suất, quản trị hệ thống

```markdown
## Nhu cầu công cụ

Tôi muốn tạo một công cụ dòng lệnh, dùng để [Công dụng].

**Ví dụ cách dùng**:
```bash
[Tên lệnh] [Ví dụ tham số]
# Ví dụ: mytool --input data.csv --output result.json
```

**Chức năng chính**:
1. [Chức năng 1]
2. [Chức năng 2]

**Mô tả tham số**:
| Tham số | Bắt buộc | Giải thích | Giá trị mặc định |
|-----|-----|------|-------|
| [Tham số 1] | Có/Không | [Giải thích] | [Giá trị mặc định] |

**Stack kỹ thuật**: [Python argparse / Node.js commander / Go cobra]

Vui lòng cung cấp code hoàn chỉnh và ví dụ sử dụng.
```

## Sai lầm thường gặp khi điền

| Sai lầm | Vấn đề | Cách làm đúng |
|-----|------|---------|
| Không ghi trình độ kỹ thuật | Code AI đưa quá phức tạp hoặc quá đơn giản | Nói rõ trình độ của mình |
| Nhu cầu chức năng quá mơ hồ | "Làm một công cụ dễ dùng" | Liệt kê các điểm chức năng cụ thể |
| Quên viết "không cần" | AI tự ý thêm rất nhiều chức năng | Xác định ranh giới, viết rõ không làm gì |
| Mô tả dữ liệu không rõ | AI không thể viết logic xử lý đúng | Đưa ra giải thích trường dữ liệu và dữ liệu mẫu |

## Điểm cốt yếu phần này

- ✅ **Mẫu ứng dụng web**: Stack kỹ thuật + Nhu cầu chức năng + Yêu cầu giao diện + Định dạng đầu ra
- ✅ **Mẫu phân tích dữ liệu**: Mô tả dữ liệu + Vấn đề phân tích + Hình thức đầu ra
- ✅ **Mẫu script tự động hóa**: Đầu vào đầu ra + Logic xử lý + Xử lý bất thường
- ✅ **Kỹ thuật then chốt**: Nói rõ trình độ kỹ thuật, AI sẽ điều chỉnh độ phức tạp của code
