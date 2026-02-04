---
title: "Chương 5: 3 trạng thái vận hành của code và nguyên lý build"
---

# Chương 5: 3 trạng thái vận hành của code và nguyên lý build

## Lời tựa

Bạn nghe thực tập sinh công ty bên cạnh kể một câu chuyện. Cậu ta ngày đầu đi làm, leader bảo chuẩn bị một bản demo chạy local. Cậu ta hăm hở chạy `pnpm dev`, mọi thứ bình thường.

Nhưng khi leader hỏi: "Bản demo local này tôi có xem được không?", cậu thực tập sinh mới phát hiện —— **trên máy leader không có cấu hình database của cậu, mà chế độ Dev cũng không thích hợp để demo**.

Leader bảo: "Phát triển local dùng chế độ Dev, tiện cho cậu debug. Nhưng cái để cho người dùng xem thì phải `pnpm build` ra bản production, rồi deploy lên server."

Cậu thực tập sinh mới vỡ lẽ, hóa ra code có **môi trường chạy khác nhau**: Local dev dùng Dev, cho người dùng xem là bản Build xong deploy lên server. Bạn nghe chuyện này xong, cảm thấy chương này phải học cho kỹ.

### 3 trạng thái

Để tránh bị nhầm lẫn khi đi sâu vào phát triển, sư phụ đặc biệt phổ cập cho bạn về **3 trạng thái vòng đời** của code.

Đầu tiên là **Dev (Chế độ phát triển)**, chính là `pnpm dev` bạn hay dùng. Nó giống như **làm nháp**. Ở chế độ này, khi bạn sửa code và lưu, trình duyệt **không cần** refresh toàn trang, mà chỉ thay thế một mảnh component nhỏ vừa sửa. Có nghĩa là nếu bạn đang điền một cái form dài dằng dặc, sửa lại style xong, nội dung đã điền trong form **không bị mất**. Nhưng cái giá phải trả là tốc độ chạy khá chậm, và chứa một đống thông tin debug dùng để báo lỗi.

Thứ hai là **Build (Chế độ xây dựng)**, khi bạn chuẩn bị online, cần chạy `pnpm build`. Quá trình này giống như **đem bản nháp đi dàn trang in thành sách**. Nó sẽ nén, tối ưu, phiên dịch tất cả code TypeScript, React bạn viết, cuối cùng sinh ra một thư mục `.next` (hoặc `dist`) trong dự án. Code trong này dung lượng cực nhỏ, chạy cực nhanh, là bản chính thức chuyên dành cho người dùng.

Cuối cùng là **Production (Chế độ sản xuất)**, chạy `pnpm start` (hoặc `next start`). Đây là **mô phỏng môi trường online chính thức** ngay trên local, dùng để chạy cái "bản chính thức" vừa sinh ra từ bước `build`. Thông thường trước khi online, bạn sẽ dùng chế độ này để kiểm tra lần cuối xem có Bug không.

### Lưu là có hiệu lực

Có thể bạn tò mò: Tại sao ở chế độ Dev cứ lưu file là trình duyệt tự refresh? Cái này gọi là **Hot Reload (Tải lại nóng)**.

Công cụ phát triển sẽ nghe ngóng sự thay đổi của file ở hậu đài. Một khi phát hiện có sửa đổi, nó sẽ tự động refresh trình duyệt hoặc chỉ cập nhật phần thay đổi. Việc này giúp bạn không cần mỗi lần đều phải F5 thủ công, hiệu suất phát triển tăng vọt.

Còn ở chế độ Build hoặc Production, code đã được đóng gói tối ưu, không có cơ chế nghe ngóng này, nên sửa xong cần build lại. Hiểu được sự khác biệt này, bạn sẽ biết tại sao thỉnh thoảng sửa code mà không thấy có tác dụng —— có thể là đang chạy sai chế độ.

### package.json

Lúc này, có thể bạn sẽ thắc mắc: **Tại sao gõ `pnpm dev` là chạy được dự án?** Sư phụ bảo bạn mở file **`package.json`** ở thư mục gốc ra. Ông bảo, đây là **file cấu hình cốt lõi** của dự án Node.js, quản lý metadata, script và dependency của dự án.

- **Quản lý Script (Scripts)**: Trong trường `scripts`, định nghĩa các lệnh chạy thường dùng của dự án. Khi bạn gõ `pnpm dev` trong terminal, trình quản lý gói sẽ tra bảng, thấy nó tương ứng với lệnh `next dev` và thực thi lệnh đó. Đây là lý do tại sao các lệnh tầng dưới phức tạp có thể được đơn giản hóa thành `dev` hay `build` ngắn gọn. **Sư phụ tiện mồm nhắc luôn, đây cũng là chỗ để tùy chỉnh "số phòng".** Còn nhớ cái lỗi chiếm dụng cổng phiền phức ở chương 1 không? Bạn hoàn toàn có thể sửa lệnh ở đây thành `next dev -p 4000`. Như vậy, lần sau chạy `pnpm dev`, ứng dụng sẽ khởi động luôn ở cổng 4000, tránh xa cổng 3000 đông đúc.

- **Quản lý Dependency (Dependencies)**: Danh sách `dependencies` ghi lại rõ ràng các thư viện bên thứ 3 (như React, Next.js, Drizzle) và phiên bản cụ thể mà dự án bắt buộc phải cài để chạy được. Việc này đảm bảo người khác (hoặc server) khi lấy code về, có thể thông qua `pnpm install` để cài đặt các thư viện y hệt, khôi phục hoàn hảo môi trường phát triển của bạn.

### Sản phẩm Build (Build Artifcats)

Build xong, bạn định tìm file `index.html` trong thư mục để click đúp mở ra, giống như hồi chương 1. Sư phụ bảo sản phẩm build nằm trong thư mục `.next` (hoặc `dist`), nhưng bạn lục tung thư mục `.next` lên cũng chỉ thấy một đống file `.js` và `.json` lằng nhằng như "ma trận". Sư phụ bảo, **Next.js Fullstack Framework dùng trong hướng dẫn này, bản chất là một "chương trình" chạy trên Node.js, chứ không phải "file" đơn giản**. Nó cần kết nối database, xử lý API request, render trang web từ phía server, mấy cái này đều không thể tách rời sự hỗ trợ của **môi trường server**.

Tất nhiên, có một số ngữ cảnh bạn có thể phát triển **dự án tĩnh thuần túy** (ví dụ dùng Vite + Vue/React), dự án kiểu này đóng gói xong đúng là sẽ sinh ra một file `index.html` trong thư mục `dist`. Nhưng để dẫn dắt bạn đi hết quy trình Fullstack trọn vẹn gồm database, auth..., chúng ta chọn Next.js. Có điều phải nhớ, kể cả là file tĩnh thuần túy do Vite đóng gói, thường cũng không thể click đúp mở trực tiếp. Vì ứng dụng hiện đại sử dụng **đường dẫn tuyệt đối** (như `/assets/app.js`) để dẫn tài nguyên, mà mở click đúp thì lại dùng **giao thức file** (`file:///`), dẫn đến việc trình duyệt không tìm thấy tài nguyên.

Vì thế, xin hãy nhớ kỹ: **Đừng bao giờ click đúp mở trực tiếp file code sau khi build, hãy luôn truy cập ứng dụng thông qua Web Server (như `pnpm start` của Next.js hoặc `pnpm preview` của dự án Vite).**

### Cache (Bộ nhớ đệm)

Như đã nói, chế độ Dev có Hot Reload, sửa code lưu cái là trình duyệt tự cập nhật, thường không bị vấn đề cache.

Nhưng ở **chế độ Production** (chạy `pnpm start`) hoặc **khi truy cập trang web đã deploy**, bạn có thể gặp chuyện lạ do **trình duyệt cache**. Ví dụ bạn đổi nút bấm từ xanh sang đỏ, `pnpm build` lại rồi truy cập, nút bấm vẫn trơ ra màu xanh. Bạn suy sụp, tưởng mình lọt vào vũ trụ song song.

Hóa ra, để tải nhanh hơn, trình duyệt đã lưu các file CSS/JS cũ vào local. Bạn học được 3 tuyệt chiêu: Một là **bắt buộc refresh** (giữ `Ctrl` + `Shift` + `R`); Hai là mở chế độ ẩn danh; Ba là mở F12 Developer Tools, trong tab Network tích vào **"Disable cache"**.

Nếu bắt buộc refresh mà vẫn không được, có thể là vấn đề **cache build**, cần xóa thư mục `.next` đi rồi `pnpm run build` lại.

Còn một cái hố hay bị bỏ quên: Sửa file `.env` xong bắt buộc phải khởi động lại service (Ctrl+C rồi npm run dev), biến môi trường mới có hiệu lực. **【Xem chi tiết Chương 6】** sẽ giải thích kỹ tại sao biến môi trường được load khi khởi động tiến trình, nên lúc chạy mà sửa file thì nó không tự cập nhật.

---

## Điều hướng chương

```
- 5.1 Rà soát bẫy Cache (./01-cache-traps.md) 🔴
- 5.2 Ba chế độ vận hành (./02-runtime-modes.md) 🟢
- 5.3 Hướng dẫn thực dụng package.json (./03-package-json-guide.md) 🟢
- 5.4 Sản phẩm Build và Web Server (./04-build-artifacts-server.md) 🟢
```
