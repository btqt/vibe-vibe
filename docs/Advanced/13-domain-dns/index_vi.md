---
title: "Chương 13: Nguyên lý phân giải tên miền và Kết nối mạng"
---

# Chương 13: Tên miền, DNS và HTTPS

## Lời tựa

Bạn chuẩn bị deploy dự án của mình lên mạng công cộng. Nếu bạn dùng nền tảng nước ngoài (như Vercel), link nhận được có thể truy cập trực tiếp, nhưng bạn bè ở trong nước mở sẽ rất chậm. Nếu bạn dùng nền tảng trong nước (như Tencent Cloud EdgeOne Pages hay Aliyun ESA Functions & Pages), tình hình sẽ phức tạp hơn một chút.

Sư phụ bảo bạn, các nền tảng trong nước vì yêu cầu tuân thủ nội dung, nên có hạn chế đối với việc truy cập tên miền mặc định. Lấy EdgeOne Pages làm ví dụ, nó cung cấp 3 vùng tăng tốc tùy chọn:

- **Vùng khả dụng Trung Quốc đại lục**: Tốc độ nhanh nhất, nhưng thêm tên miền tùy chỉnh **bắt buộc phải hoàn thành ICP Filing (Bắc án/Cấp phép)**, nếu không chỉ dùng được link xem trước có hiệu lực 3 tiếng.
- **Vùng khả dụng toàn cầu (gồm thềm lục địa TQ)**: Cũng cần Bắc án, link xem trước cũng chỉ có hiệu lực 3 tiếng.
- **Vùng khả dụng toàn cầu (không gồm thềm lục địa TQ)**: **Không cần Bắc án**, mạng ngoài Trung Quốc đại lục có thể truy cập trực tiếp, nhưng truy cập từ trong nước sẽ bị hạn chế.

Bạn chọn **Vùng khả dụng toàn cầu (không gồm thềm lục địa TQ)**, như vậy không cần đợi Bắc án là có thể online ngay. Sư phụ nhắc bạn: Tuy tên miền mặc định của vùng này có hạn chế truy cập, nhưng **sau khi liên kết tên miền tùy chỉnh là có thể truy cập bình thường**, hơn nữa không cần Bắc án.

Khi bạn gửi tên miền mặc định do nền tảng cấp cho bạn bè, họ lại chụp màn hình báo: **403** hoặc không mở được. Bạn hoảng, tưởng mình deploy thất bại. Sư phụ nhân cơ hội phổ cập nhanh cho bạn kiến thức thường thức về **Mã trạng thái HTTP** (HTTP Status Code) —— gặp lỗi đừng hoảng, **chỉ cần nhìn chữ số đầu tiên**, là phán đoán được lỗi của ai:

- **2xx (như 200 OK)**: **Thành công**. Mọi thứ bình thường, cả hai bên đều vui vẻ.
- **3xx (như 301 Moved)**: **Chuyển hướng**. Chuyển nhà rồi, sang địa chỉ mới tìm nhé.
- **4xx (như 404/403)**: **Lỗi Client (Lỗi của bạn)**.
  - `404`: Số điện thoại bạn gọi là số không đúng (nhập sai địa chỉ).
  - `403`: Gọi thông rồi nhưng bị dập máy (không có quyền truy cập).
- **5xx (như 500/502)**: **Lỗi Server (Lỗi của nó)**. Code bị nổ, hoặc server sập rồi.

Hóa ra, lỗi 403 lần này là do tên miền mặc định của nền tảng trong nước mặc định bật bảo vệ xác thực để **tuân thủ nội dung**. Bạn hiểu ra: **Muốn cho người khác xem ổn định, bắt buộc phải liên kết một tên miền tùy chỉnh thuộc về chính mình.**

### Tên miền tùy chỉnh

Bạn nghe nói trên mạng có tên miền cấp 2 cho nhận miễn phí, nghĩ bụng tiết kiệm được bao nhiêu hay bấy nhiêu. Sư phụ nghiêm túc ngăn bạn lại: **"Làm sản phẩm, tên miền chính là mặt tiền."** Những tên miền miễn phí này thường cực kỳ không ổn định, có thể bị thu hồi bất cứ lúc nào, hơn nữa dễ bị trình duyệt đánh dấu là trang web không an toàn. Thế là bạn quyết định đi mua một tên miền cấp cao (TLD) đàng hoàng (như `.com`).

### Tên miền và Tài sản thương hiệu

Sư phụ bổ sung: "**Ba điều kiện của tên miền tốt**: Ngắn, dễ nhớ, dễ đánh vần. Ví dụ `zoom.com`, `dropbox.com` đều là các case kinh điển. **Chiến lược đầu tư tên miền**: Khi đăng ký tên miền phải cân nhắc chi phí gia hạn, một số tên miền cấp cao (như `.io`) phí gia hạn rất đắt. Ngoài ra, để bảo vệ nhãn hiệu, nên đăng ký nhiều biến thể như `.com`, `.net`, `.vn`... để tránh bị đầu cơ.

Tên miền là số nhà trong thời đại số, tên miền tốt là tài nguyên khan hiếm.

### Giới thiệu nhà cung cấp dịch vụ Cloud

Sư phụ tiện thể phổ cập cho bạn về các nhà cung cấp dịch vụ Cloud chủ lưu. Có thể bạn đã nghe qua những cái tên này: **Aliyun (Alibaba Cloud), Tencent Cloud, AWS (Amazon Web Services), Huawei Cloud**, v.v.

Họ là những ông lớn về hạ tầng đám mây, cung cấp dải sản phẩm cloud một trạm (one-stop):

- **Tính toán**: Máy chủ ảo (ECS/CVM)
- **Lưu trữ**: Lưu trữ đối tượng (OSS/COS)
- **Cơ sở dữ liệu**: Database trên mây (RDS)
- **Mạng**: Tăng tốc CDN, Cân bằng tải (Load Balancing)
- **An ninh**: Tường lửa, Chống DDoS

So với các nền tảng Deploy mới nổi (EdgeOne Pages, ESA Functions & Pages, Vercel...), nhà cung cấp Cloud truyền thống có chức năng toàn diện hơn, nhưng cấu hình cũng phức tạp hơn. Chúng phù hợp cho dự án cấp doanh nghiệp hoặc kịch bản cần tổ hợp nhiều dịch vụ cloud. Đối với cá nhân phát triển hoặc kiểm chứng MVP, sư phụ khuyên nên dùng nền tảng Deploy đơn giản trước, đợi sản phẩm lớn mạnh rồi hãy tính chuyện di dời sang Cloud truyền thống.

### Phân giải DNS

Trong quá trình cấu hình, cuối cùng bạn cũng hiểu **Phân giải DNS** là gì. Bạn hiểu ra DNS giống như **danh bạ điện thoại** của Internet, tác dụng của nó là dịch cái tên miền dễ nhớ (tên người) của bạn thành địa chỉ IP mà máy móc hiểu được (số điện thoại).

Sư phụ dạy bạn cấu hình 2 loại bản ghi phổ biến nhất:

- **Bản ghi A**: Trỏ trực tiếp đến một **địa chỉ IP** cụ thể.
  - _Ngữ cảnh_: Ví dụ sau này bạn mua một con Cloud Server, có một IP công khai cố định là `1.2.3.4`, bạn dùng bản ghi A để trỏ tên miền vào đó.
- **Bản ghi CNAME**: Trỏ đến **một tên miền khác** (biệt danh).
  - _Ngữ cảnh_: EdgeOne cấp cho bạn địa chỉ truy cập là một chuỗi dài `your-project.pages.eo`. Bạn dùng CNAME để trỏ `www.example.com` của bạn vào đó. Việc này cũng giống như bạn cài đặt chuyển cuộc gọi, người khác gọi vào tên miền của bạn, tự động chuyển tiếp đến máy chủ của EdgeOne.

Trang web của bạn cuối cùng cũng có thân phận hợp pháp trên Internet.

### Chứng chỉ HTTPS

Các nền tảng Deploy hiện đại hỗ trợ **Chứng chỉ HTTPS** miễn phí (thường là Let's Encrypt), nó sẽ treo một cái **ổ khóa xanh** trên thanh địa chỉ trình duyệt của bạn, đảm bảo dữ liệu truyền tải giữa người dùng và trang web của bạn được mã hóa, không bị kẻ gian nghe lén.

Tuy nhiên các nền tảng trong nước (như EdgeOne Pages) thường cần bạn **bấm nút xin cấp thủ công** —— tìm mục cấu hình HTTPS trong trang quản lý tên miền, bấm nút "Xin cấp chứng chỉ miễn phí" là được. Sau khi xin cấp thành công sẽ **tự động gia hạn**, bạn không cần lo vấn đề hết hạn.

Nền tảng nước ngoài (như Vercel) thường sẽ tự động xin cấp chứng chỉ sau khi bạn liên kết tên miền tùy chỉnh, đỡ lo hơn một chút.

### Lời kết

Cuối cùng, sư phụ báo cho bạn một tin tốt. Dự án của bạn đã đi hết vòng khép kín hoàn chỉnh của phát triển Fullstack, có thể gửi bài tham dự **Phần thực hành của hướng dẫn này**. Nếu được chọn, người phụ trách liên quan của trang web này sẽ phân bổ cho bạn một **tên miền cấp 2 độc quyền** và cung cấp **hỗ trợ tài nguyên Cloud** nhất định.

Như vậy, bạn có thể tập trung vào code và sáng tạo, không cần phiền não về những việc lặt vặt như mua tên miền, phân giải và vận hành nữa.

---

### Tên miền Việt Nam (.vn)

Nếu bạn phát triển sản phẩm hướng đến người dùng Việt Nam, tên miền quốc gia **.vn** là lựa chọn uy tín nhất.

- **Ưu điểm**: Thương hiệu nhận diện cao tại Việt Nam, được pháp luật Việt Nam bảo vệ, hỗ trợ SEO tốt cho tìm kiếm tại Việt Nam.
- **Lưu ý**: Thủ tục đăng ký cần cung cấp CCCD/CMND (cá nhân) hoặc Giấy phép kinh doanh (tổ chức) và cần thực hiện khai báo sử dụng theo quy định của VNNIC.

---

### Mục lục chương này

```
1. **13.1 Lựa chọn nền tảng Deploy và Truy cập** 🟢
   Hiểu sự khác biệt giữa nền tảng deploy trong và ngoài nước, lựa chọn vùng tăng tốc, và hạn chế truy cập của tên miền mặc định.

2. **13.2 Hướng dẫn mua tên miền** 🟡
   Cách chọn và mua một tên miền tốt, bao gồm chiến lược tên miền, chọn nhà đăng ký và tối ưu chi phí.

3. **13.3 Cấu trúc tên miền** 🟢
   Hiểu cấu trúc phân cấp và thành phần của tên miền, bao gồm tên miền gốc (root), tên miền cấp cao (TLD), tên miền cấp 2 (SLD) và tên miền con (subdomain).

4. **13.4 Thực chiến phân giải DNS** 🔴
   Bắt tay cấu hình phân giải DNS, hiểu ngữ cảnh sử dụng và phương pháp cấu hình bản ghi A và CNAME.

5. **13.5 Thường thức về Mã trạng thái HTTP** 🔴
   Hiểu mã trạng thái HTTP, gặp báo lỗi không hoảng. Học cách định vị nhanh vấn đề thông qua mã trạng thái.

6. **13.6 HTTPS và Giao thức mạng** 🟡
   Hiểu nguyên lý hoạt động của HTTP, HTTPS, SSL/TLS, và tại sao bắt buộc phải bật HTTPS.

7. **13.7 Lựa chọn vùng phục vụ** 🟡
   Cách chọn vùng phục vụ và node mạng phù hợp, hiểu sự khác biệt và chiến lược lựa chọn giữa Cấp phép (Bắc án/ICP) và Miễn cấp phép.

8. **13.8 Thực chiến cấu hình chứng chỉ SSL** 🔴
   Thực thao tác cấu hình chứng chỉ SSL, bật HTTPS, bao gồm xin cấp và tự động gia hạn chứng chỉ miễn phí Let's Encrypt.
```
