---
title: "Chương 14: Vận hành Cloud Server và Deploy dự án"
---

# Chương 14: Vận hành Cloud Server và Deploy dự án

## Lời tựa

Giả sử ví tiền của bạn rủng rỉnh, bạn thực sự đi mua một con server; hoặc bạn phát hiện chương trình khuyến mãi của nhà cung cấp cloud nào đó, cho dùng thử miễn phí.

Khi chọn khu vực cho server, sư phụ khuyên tốt nhất nên chọn **Hồng Kông (Trung Quốc)** hoặc các node ở nước ngoài. Lý do rất đơn giản: server ở node trong nước (Trung Quốc đại lục/Việt Nam) nếu gắn tên miền thì bắt buộc phải xin giấy phép/bắc án, còn node Hồng Kông hay quốc tế thường **miễn thủ tục này**, giúp bạn bớt được vài tuần chờ đợi, mua xong dùng ngay.

Tóm lại, bạn có được một địa chỉ IP công khai, tên đăng nhập (thường là `root`) và mật khẩu. Bạn phát hiện server không có Remote Desktop như Windows, chỉ có thể thao tác qua **Terminal**. Bạn học được cách dùng lệnh SSH để kết nối server: `ssh root@1.2.3.4`

### SSH

Quản lý server từ xa cần **kết nối SSH**. SSH là phương thức an toàn để đăng nhập server từ xa. Ở **【Chương 10】**, bạn đã được giảng giải chi tiết về nguyên lý và cấu hình SSH.
Lấy được server rồi, sư phụ không bảo bạn bắt đầu gõ code ngay, mà dạy bạn vài **thiết luật (quy tắc sắt) khi khởi tạo server** (như cập nhật hệ thống, cài đặt tường lửa...).

### 1Panel Dashboard

Để giảm độ khó vận hành, sư phụ khuyên bạn cài đặt **1Panel**. Đây là một phần mềm quản lý vận hành trực quan hóa hiện đại dành cho server Linux.

Điều này cũng thể hiện triết lý "mở rộng năng lực thông qua cấu hình thay vì code". Giống như trước đây chúng ta dùng **MCP** để AI kết nối công cụ bên ngoài, **Hooks** để AI tự động thực thi tác vụ, **Skills** để AI nắm bắt năng lực chuyên môn. Tất cả đều là hệ thống điều khiển bằng cấu hình.

Bạn làm theo hướng dẫn chính thức, gõ một dòng lệnh là cài xong, tiện tay cài luôn **Docker**, và thuận tiện cấu hình **tăng tốc Mirror** (cái này cực kỳ quan trọng trong môi trường mạng nội địa).

### Docker Container

**Docker là gì?** Cốt lõi của 1Panel thực ra chính là Docker. Nghe thì lại là thuật ngữ mới, nhưng bạn cứ coi nó là cái thùng container.

- **Tính cách ly**: Mỗi ứng dụng (website, database của bạn) đều được đóng gói chạy trong một cái thùng container độc lập, không quấy rầy nhau, cũng không làm bẩn hệ thống server của bạn.
- **Tính nhất quán**: Mỗi lần bạn bấm cài đặt ứng dụng trong 1Panel, bản chất là đang kéo (pull) và chạy các thùng container Docker này.

Cơ chế cách ly này giúp bạn hiểu ra một thiết luật: **Tuyệt đối không sửa code hay sửa file trực tiếp trên server**. Server là **Môi trường sản xuất (Production)** dùng để "chạy" code, còn việc viết code, debug lỗi phải luôn hoàn thành ở **Môi trường phát triển (Development)** trên máy tính cá nhân của bạn, sau đó đồng bộ lên thông qua Git.

### Security Group (Nhóm an ninh)

Khi bạn hào hứng nhập `http://IP:Port` mà 1Panel cung cấp để truy cập bảng điều khiển, trình duyệt lại quay đều cho đến khi timeout. Bạn tưởng cấu hình sai, nhưng sư phụ bảo, Cloud Server thường có **cánh cửa bảo mật đầu tiên —— Security Group của nhà cung cấp**.

Security Group tương đương với **tường lửa** mà nhà cung cấp Cloud dựng ngay trước cửa phòng máy. Mặc định, ngoại trừ cổng SSH (22) và vài cổng ít ỏi khác, tất cả các cổng còn lại đều bị bịt kín. Bạn phải vào bảng điều khiển (Console) của nhà cung cấp Cloud, thủ công **mở quy tắc Security Group** (cho phép cổng của 1Panel), thì request từ bên ngoài mới chạm được đến mép server của bạn.

### Tự dựng Database

Nếu không dùng Database Supabase trên cloud, giờ có server rồi, chúng ta hoàn toàn có thể tự dựng một cái. Bạn mở "App Store" của 1Panel, bấm một nút cài đặt **PostgreSQL**. Trong quá trình cài, bạn thiết lập **Cổng database**, **Tài khoản admin** (thường là `postgres`) và **Mật khẩu**.

Cài xong, bạn vào trang "Database" của 1Panel tạo một **Cơ sở dữ liệu cụ thể** (ví dụ `my_app_db`). Ở đây sư phụ phổ cập cho bạn một kiến thức thường thức: **Phần mềm quản trị CSDL (DBMS) vs Cơ sở dữ liệu (Database)**.

- **DBMS (PostgreSQL)**: Giống như bản thân phần mềm Excel.
- **Database**: Giống như từng file `.xlsx` được Excel mở ra. Cài một phần mềm PostgreSQL, có thể tạo vô số file database độc lập cho các dự án khác nhau sử dụng.

Trong phần "Thông tin kết nối" của database, bạn nhìn thấy hai cái tên host. Sư phụ bảo, cái này quyết định bạn điền `DATABASE_URL` trong `.env` thế nào:

### Mạng Docker (Container Network)

Khi cấu hình chuỗi kết nối trong môi trường Docker, rất dễ nhầm lẫn giữa `localhost` và tên container. Sư phụ nhấn mạnh, chìa khóa để hiểu mạng container là: **`localhost` = bản thân môi trường hiện tại, Tên container = hàng xóm cùng mạng Docker, `127.0.0.1` = localhost của máy chủ (host)**.

- **Kịch bản 1: Dự án Node chạy bằng tính năng "Runtime" của 1Panel (Khuyên dùng)** Lúc này dự án của bạn chạy trong container, database cũng trong container. Chúng là hàng xóm của nhau. Bạn nên điền **Tên container Docker** (ví dụ `postgresql` hoặc `1panel-postgres-x`), chứ không phải `localhost`. Việc này giống như gọi tên hàng xóm trong mạng nội bộ.
- **Kịch bản 2: Debug thủ công trong terminal server** Nếu bạn SSH vào server, chạy script bằng dòng lệnh. Lúc này bạn đang đứng trên máy chủ (Host) để truy cập container. Bạn nên điền **`127.0.0.1` hoặc `localhost`**. Vì cổng của container database đã được ánh xạ (map) ra localhost của máy chủ. Điền sai chuỗi kết nối sẽ dẫn đến kết nối thất bại, mà lỗi này rất khó tra cứu, vì cấu hình trông có vẻ không sai.

### Ánh xạ cổng (Port Mapping)

Sư phụ bảo, có thể dùng tính năng Runtime của 1Panel để deploy nhanh dự án Node.js. Bạn phát hiện bài điền vào chỗ trống ở đây —— chọn phiên bản node, lệnh build, biến môi trường... —— y hệt như những gì đã làm trên Vercel. Khác biệt duy nhất là: Server cần kéo code từ GitHub về trước, sau đó bạn phải cấu hình ánh xạ cổng và cho phép truy cập cổng từ bên ngoài.

Trước đây bạn rất thắc mắc, tại sao server chỉ có 1 IP công khai, mà lại chạy được cùng lúc mấy dự án đều lắng nghe cổng 3000 ở bên trong? Hóa ra, Docker cung cấp **môi trường mạng cách ly** cho từng container.

- Ứng dụng A của bạn lắng nghe cổng 3000 trong container.
- Ứng dụng B của bạn lắng nghe cổng 3000 trong container. Chúng không xung đột nhau.

Khi deploy, thông qua kỹ thuật **Ánh xạ cổng**:

- Ánh xạ cổng **3001** của server -> vào cổng 3000 của Ứng dụng A.
- Ánh xạ cổng **3002** của server -> vào cổng 3000 của Ứng dụng B.

Như vậy, khi người dùng bên ngoài truy cập `IP:3001` và `IP:3002`, lưu lượng sẽ được chuyển tiếp chính xác đến container tương ứng. Việc này giải quyết vấn đề xung đột cổng, giúp một server chạy được nhiều ứng dụng.

Bạn truy cập thành công ứng dụng trên server qua `http://IP:Port`, nhưng sau khi liên kết tên miền trong 1Panel thì lại không mở được. Hóa ra là chưa làm **Phân giải DNS**. Bạn thành thục vào nhà cung cấp tên miền thêm một **bản ghi A**, trỏ về IP công khai của server.

Truy cập được rồi, nhưng trình duyệt hiện cảnh báo đỏ lòm "Không an toàn".

### Chứng chỉ SSL

Sư phụ bảo cần xin cấp chứng chỉ SSL. Thế là bạn vào cài đặt Website - Chứng chỉ trong 1Panel, **bấm một nút xin cấp chứng chỉ miễn phí**, và bật **HTTPS**. Nhìn cái ổ khóa xanh trên thanh địa chỉ, cuối cùng bạn cũng hoàn thành một lần deploy độc lập fullstack thực thụ.

### Ý thức nhập môn SRE

Nhìn ứng dụng chạy ổn định trên server, sư phụ nói: "Giờ cậu đã là một nửa kỹ sư vận hành (Ops) rồi đấy."

Ông giới thiệu cho bạn triết lý **SRE (Site Reliability Engineering - Kỹ thuật độ tin cậy trang web)**: **Dùng tư duy kỹ thuật phần mềm để giải quyết vấn đề vận hành**.

Vận hành truyền thống dựa vào sức người thức đêm sửa lỗi, SRE dựa vào hệ thống tự động để duy trì sự ổn định. Bạn hiện đã nắm được cơ bản:

- **Giám sát**: Hiểu trạng thái hệ thống qua log và công cụ thống kê
- **Tự động hóa**: Deploy một nút bấm qua Docker, Rollback một nút bấm qua Git
- **Dung sai (Disaster Recovery)**: Bảo vệ dữ liệu qua chiến lược sao lưu và khôi phục

Sư phụ nói: "SRE không phải đặc quyền của công ty lớn, mà là ý thức mọi sản phẩm đều nên có. Sản phẩm của cậu dù chỉ có 1 người dùng, cũng nên đáng tin cậy."

Điều này làm bạn nhận ra, kỹ thuật không chỉ là kiến tạo, mà còn là bảo vệ. Deploy online không phải là kết thúc, mà là sự bắt đầu của trách nhiệm lâu dài.

### Nhật ký (Log)

Deploy xong vài ngày, có bạn phản ánh không mở được trang. Bạn vội vàng tự truy cập, thấy mọi thứ bình thường. Bạn bắt đầu nghi ngờ có phải tại máy của bạn kia, hay mạng chập chờn.

Sư phụ bảo, đừng đoán mò, hãy xem **Log**.

Log là cuốn sổ nhật ký tự động ghi lại quá trình chạy của chương trình. Nó ghi lại chuyện gì xảy ra vào lúc nào, có báo lỗi không, người dùng đã thao tác gì. Giống như hộp đen máy bay, xảy ra sự cố có thể lôi ra xem đã xảy ra chuyện gì.

**Xem ở đâu**

Nếu bạn dùng nền tảng Deploy Serverless, họ sẽ cung cấp giao diện xem log trên web. Mỗi lần deploy, mỗi request người dùng, mỗi lần báo lỗi đều được ghi lại. Bạn có thể lọc theo thời gian, tìm kiếm theo từ khóa, rất nhanh sẽ tìm ra vấn đề.

Nếu dùng server riêng, có thể xem log thời gian thực qua 1Panel. Log sẽ cuộn liên tục, hiển thị trạng thái chạy mới nhất.

**Xem cái gì**

Người mới nhìn log có thể thấy hoa mắt, toàn chữ là chữ. Sư phụ bảo, thực ra chỉ cần quan tâm vài từ khóa:

Thứ nhất là từ **Error (Lỗi)**. Nếu trong log xuất hiện từ này, đằng sau thường kèm theo thông tin báo lỗi cụ thể, cho biết hỏng ở đâu.

Thứ hai là **Warning (Cảnh báo)**. Tuy không phải lỗi, nhưng có nghĩa là chỗ nào đó có thể có vấn đề, khuyên bạn nên kiểm tra.

Thứ ba là log do chính bạn viết. Lúc phát triển, bạn có thể thêm vài dòng chú thích ở vị trí then chốt, ví dụ "Người dùng bắt đầu đăng ký", "Kết nối DB thành công". Như vậy khi có sự cố, bạn biết chương trình đã chạy đến bước nào.

**Mẫu vấn đề thường gặp**

Sư phụ tổng kết vài mẫu log thường gặp:

Nếu thấy "Module not found", nghĩa là gói dependency nào đó chưa cài xong, cần cài lại.

Nếu thấy "Connection refused", thường là kết nối database thất bại, có thể sai địa chỉ, hoặc database chưa bật.

Nếu thấy "Timeout", nghĩa là thao tác nào đó quá chậm, có thể do mạng, hoặc logic code có vấn đề.

Gặp mấy cái này, không cần tự mình vò đầu bứt tai phân tích, cứ copy thông tin then chốt trong log, quăng cho AI nhờ nó chẩn đoán.

Log không lưu mãi mãi. Nền tảng thường giữ vài ngày đến một tháng, sau đó tự xóa. Nên nếu gặp vấn đề quan trọng, nhớ lưu lại nội dung log kịp thời. Ngoài ra, log có thể chứa thông tin nhạy cảm, khi phân tích log phải cẩn thận, đừng chụp màn hình đăng lên chỗ công cộng.

---

## Mục lục chương này

```
1. **14.1 Khái niệm VPS (./01-vps-concepts.md)** 🟢
   Hiểu khái niệm và sự khác biệt giữa VPS, Cloud Server, Máy ảo. Học cách chọn cấu hình server phù hợp.

2. **14.2 Mua và Cấu hình Server (./02-server-setup.md)** 🔴
   Cách mua và khởi tạo cấu hình Cloud Server, bao gồm chọn cấu hình, cấu hình Security Group và tối ưu hệ thống.

3. **14.3 Cấu hình kết nối SSH (./03-ssh-config.md)** 🔴
   Nắm vững các cách kết nối SSH server từ xa, bao gồm chứng thực khóa, file cấu hình và các kỹ thuật nâng cao.

4. **14.4 Cài đặt Panel 1Panel (./04-1panel-install.md)** 🟡
   Cài đặt và sử dụng bảng quản trị trực quan 1Panel, giảm ngưỡng vận hành, nâng cao hiệu suất.

5. **14.5 Chi tiết Docker Container (./05-docker-details.md)** 🟡
   Hiểu khái niệm và cách dùng cơ bản của Docker Container, nắm vững Image, Container, Repository và Docker Compose.

6. **14.6 Mạng Docker Container (./06-docker-network.md)** 🔴 **[Tiểu tiết cốt lõi]**
   Hiểu sâu nguyên lý và cấu hình mạng Docker. Nắm vững khái niệm cốt lõi về localhost, tên container, ánh xạ cổng; hiểu cơ chế giao tiếp giữa các container và cách ly mạng.

7. **14.7 Cấu hình Security Group (./07-security-group.md)** 🔴
   Hiểu và cấu hình Security Group cho Cloud Server, bảo vệ an toàn server. Đây là phòng tuyến đầu tiên của Cloud Server.

8. **14.8 Tự dựng Database (./08-self-hosted-db.md)** 🟡
   Sử dụng Docker và 1Panel tự dựng database PostgreSQL, hiểu sự khác biệt giữa DBMS và Database.

9. **14.9 Thực chiến cấu hình chứng chỉ SSL (./09-ssl-config.md)** 🟡
   Cấu hình chứng chỉ SSL trên server, bật HTTPS. Bao gồm xin cấp và tự động gia hạn chứng chỉ miễn phí Let's Encrypt.

10. **14.10 Thực chiến Ánh xạ cổng (./10-port-mapping.md)** 🔴
    Hiểu và cấu hình ánh xạ cổng Docker, thực hiện deploy đa ứng dụng. Nắm vững cách chạy đồng thời nhiều ứng dụng trên một server.
```
