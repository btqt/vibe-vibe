---
title: "Chương 7: Biến môi trường và cơ chế bảo mật"
---

# Chương 7: Biến môi trường và cơ chế bảo mật

## Lời tựa

Trước khi bắt đầu xử lý dữ liệu, sư phụ nghiêm mặt ngăn bạn lại. Ông phát hiện bạn đang định viết thẳng API Key của nền tảng AI và mật khẩu database vào trong code. Ông bảo, đây là điều đại kỵ trong giới lập trình. Mạng Internet bây giờ đầy rẫy crawler đi tuần tra 24/7, chuyên quét các kho code công khai trên GitHub. Nếu code của bạn chứa khóa bí mật dạng văn bản rõ (plaintext), thường chỉ vài giây sau khi commit, hạn mức API của bạn sẽ bị trộm sạch, thậm chí gánh khoản nợ khổng lồ, nghe mà toát mồ hôi hột.

### Biến môi trường .env

Bạn đã biết sơ qua về việc dùng file `.env` để chuyên chứa những thông tin nhạy cảm này. Bạn hiểu thế nào là biến môi trường —— chỉ chương trình đang chạy mới biết, chứ không bị viết toạc ra trên mặt code.

### Danh sách chặn .gitignore

Nhưng chỉ tạo file `.env` thôi chưa đủ, vì nếu bạn lỡ tay gõ `git add .`, file này vẫn sẽ bị đóng gói upload lên GitHub. Sư phụ chỉ vào cái file bắt đầu bằng dấu chấm **`.gitignore`** ở thư mục gốc dự án, bảo đây mới là phòng tuyến cuối cùng ngăn bạn phá sản. Bạn có thể hiểu nó là **danh sách chặn** của Git. Phàm là những cái tên được viết trong file này, Git sẽ **bỏ qua** khi quét các thay đổi của dự án.

Sư phụ bảo bạn nhất định phải kiểm tra xem trong đó có chứa mấy loại file phổ biến này không:

- **Cấu hình nhạy cảm**: Như `.env`, đây là "chìa khóa thật" tuyệt đối không được upload.
- **Gói dependency**: Như `node_modules/`, cái thư mục khổng lồ chứa hàng vạn gói dependency bên thứ 3 này, đồng đội chỉ cần chạy lệnh cài đặt là tải lại được, không cần upload.
- **Sản phẩm build**: Như `.next/` hoặc `dist/`, đây là file tạm sinh ra sau khi biên dịch code, không cần lưu trữ.
- **Rác hệ thống**: Như `.DS_Store` (file cache của Mac) hoặc `Thumbs.db` (cache hình thu nhỏ của Windows), upload lên chỉ tổ làm bạn trông thiếu chuyên nghiệp.
- **Log lỗi**: Như `npm-debug.log`, đây là ghi chép hiện trường khi báo lỗi, thường cũng không cần chia sẻ.

Nếu bạn thực sự lỡ tay, chưa cấu hình `.gitignore` mà đã commit file nhạy cảm lên rồi, thì chỉ xóa file rồi commit lại là vô dụng, vì trong lịch sử Git vẫn tra ra được. Lúc này, bạn có thể cầu cứu AI: **"Tôi lỡ tay commit mật khẩu vào lịch sử Git rồi, xin hãy giúp tôi viết lệnh xóa sạch nó đi."** AI sẽ hướng dẫn bạn dùng các lệnh phức tạp để sửa chữa sai lầm. Tất nhiên, để an toàn tuyệt đối, sau khi rửa sạch lịch sử, tốt nhất vẫn là lên trang chủ **đổi Key mới (Reset Key)**.

### Bản mẫu .env.example

Đã chặn `.env` rồi, thì sau này đồng đội kéo code về sao biết cần cấu hình những biến nào? Lúc này cần dùng đến **`.env.example`**. Nếu nói `.env` là két sắt chứa chìa khóa thật, thì `.env.example` là cái khuôn đúc chìa khóa rỗng. Bạn chỉ liệt kê tên biến vào đó (ví dụ `DATABASE_URL=`), nhưng không điền giá trị cụ thể. File này cần commit lên GitHub, đồng đội kéo code về, chỉ cần copy một bản đổi tên thành `.env`, rồi điền Key của họ vào là dự án chạy được.

### Cấu hình chưa hiệu lực

Cấu hình xong .gitignore, chìa khóa của bạn đã an toàn. Nhưng sư phụ nhắc nhở, nếu bạn dùng MCP Server, thông tin kết nối của chúng cũng chứa chứng thực nhạy cảm, cũng cần quản lý qua biến môi trường, chứ không được viết chết trong file cấu hình. Cấu hình bảo mật cho MCP chúng ta sẽ nói kỹ ở các chương sau.

Cấu hình xong xuôi, bạn dẫm ngay phải một cái hố to: Bạn đã cấu hình Key trong `.env`, code cũng viết logic gọi rồi, nhưng chương trình vẫn báo lỗi `undefined` hoặc hiện tượng lạ. Bạn kiểm tra chính tả, kiểm tra đường dẫn file, thậm chí bắt đầu hoài nghi nhân sinh. Cuối cùng sư phụ thốt ra một câu xanh rờn: "**Sửa file cấu hình thì phải khởi động lại terminal service.**" Bạn ngậm ngùi tắt tiến trình terminal (Ctrl+C) rồi chạy lại `pnpm dev`, mọi thứ bình thường. Bạn hiểu sâu sắc cái sự "hiệu lực trễ" của cấu hình biến môi trường —— vì biến môi trường được nạp vào bộ nhớ ngay khoảnh khắc chương trình khởi động, đang chạy mà sửa file thì giá trị cũ trong bộ nhớ sẽ không tự cập nhật.

### Server và Client

Theo đà phát triển Next.js, bạn lại gặp một hiện tượng quỷ dị: Bạn định nghĩa `API_KEY` trong `.env`, ở phía server (API Route) thì đọc được, nhưng ở component Frontend (React Component) in ra lại là `undefined`. Sư phụ bảo, đây là **cơ chế bảo mật** Next.js thiết kế để phòng ngừa bạn làm điều ngốc nghếch, tiện thể bổ túc cho bạn khái niệm **Server (Phía chủ)** và **Client (Phía khách)**.

- **Server (Phía chủ)**: Thường chỉ **máy chủ deploy trên cloud** (hoặc tiến trình Node.js chạy ngầm ở local của bạn). Nơi này chạy code Backend, kết nối trực tiếp database. Vì người dùng không thể tiếp xúc trực tiếp với nội bộ cái máy này, nên đọc khóa riêng (Private Key, API Key) ở đây là rất an toàn. Mặc định, biến trong `.env` **chỉ khả dụng ở phía Server**.
- **Client (Phía khách)**: Chỉ **thiết bị của người dùng**, ví dụ trình duyệt trên máy tính người dùng, App trên điện thoại. Code Frontend cuối cùng là chạy trong máy tính hoặc điện thoại của người dùng. Bất cứ dữ liệu nào gửi xuống Client, người dùng đều có thể dùng biện pháp kỹ thuật (ví dụ F12 Developer Tools của trình duyệt) để xem được. Nếu để lộ API Key ở Client, thì cũng ngang với dán mật mã két sắt lên cổng lớn.

Cho nên, nếu bạn thực sự cần dùng thông tin không nhạy cảm ở Frontend (ví dụ tiêu đề website, địa chỉ API công khai), bạn bắt buộc phải thêm tiền tố **`NEXT_PUBLIC_`** vào trước tên biến (ví dụ `NEXT_PUBLIC_ANALYTICS_ID`). Chỉ những biến có tiền tố này, công cụ Build mới cho phép nó được gửi từ phía Server an toàn xuống thiết bị của người dùng.

### Cross-Origin (Xuyên miền) —— Cơ chế bảo mật của trình duyệt

Có lúc bạn sẽ gặp một lỗi lạ: Rõ ràng địa chỉ API đúng, nhưng lại báo lỗi "Request xuyên miền bị chặn" (CORS policy).

Sư phụ giải thích: **Đây là cơ chế bảo mật của trình duyệt**. Giả sử website hiện tại là `a.com`, nó gửi request lấy dữ liệu từ `b.com`, trình duyệt sẽ chặn lại. Vì nếu không chặn, trang web độc hại có thể mạo danh bạn gửi request đến trang web khác, ví dụ trang ngân hàng, thế thì nguy hiểm quá.

Cho nên giới hạn xuyên miền là để bảo vệ an toàn cho người dùng. Giải pháp nằm ở phía Backend: Bảo AI cấu hình CORS (Cross-Origin Resource Sharing), chỉ định rõ cho phép những tên miền nào truy cập API của bạn. Hiểu khái niệm này, gặp báo lỗi sẽ không bị ngơ ngác, biết là vấn đề cấu hình Backend chứ không phải code viết sai.

### Biến môi trường trên Cloud

Cuối cùng, bạn có thể sẽ hỏi: Online rồi thì làm gì có file `.env` nữa? Sư phụ bảo, trên các nền tảng deploy sau này đều có trang cài đặt biến môi trường chuyên biệt. Bạn chỉ cần điền từng nội dung trong `.env` local vào đó là được. Việc này giống như chuyển tiền từ két sắt ở nhà (local `.env`) sang két sắt ngân hàng (cấu hình Cloud), tuy vị trí thay đổi nhưng bản chất không đổi.

### Middleware (Phần mềm trung gian)

Bạn đã học được cách bảo vệ khóa, cũng hiểu sự khác biệt giữa Server và Client. Nhưng một ngày nọ, bạn chợt nhận ra một vấn đề: **Frontend ẩn lối vào chỉ là bịt tai trộm chuông, bảo vệ định tuyến Backend mới là phòng tuyến thực sự.**

Ví dụ, bạn làm một trang quản trị `/admin`, trên giao diện Frontend bạn giấu lối vào rất kỹ, nhưng nhập tay `/admin` trên thanh địa chỉ trình duyệt thì lại vào thẳng trang quản trị! Điều này có nghĩa là bất kỳ ai cũng có thể truy cập trang nhạy cảm của bạn.

Sư phụ bảo, trong Next.js, không cần viết logic phán đoán ở từng trang, chỉ cần đặt một file **`middleware.ts`** ở thư mục gốc dự án. Nó giống như **thủ môn** của website —— mỗi một request (dù là truy cập trang hay gọi API) trước khi đến được server, đều phải qua nó kiểm tra trước.

Bạn bảo AI viết một đoạn logic đơn giản:

> "Chặn tất cả các đường dẫn bắt đầu bằng `/admin`. Nếu người dùng chưa đăng nhập (thiếu Session), hoặc vai trò người dùng không phải admin, đá ngay về trang đăng nhập."

Vài dòng code, bịt kín lỗ hổng truy cập trái phép. Bạn thực sự hiểu ý nghĩa của vòng khép kín Fullstack —— **An toàn không dựa vào may mắn, mà dựa vào logic chặt chẽ.**

### Sự tiến hóa của phương thức xác thực

Sư phụ thuận miệng nhắc một câu: **Website đời đầu dùng Session, ứng dụng hiện đại đa số dùng Token (như JWT)**.

- **Session (Phiên)**: Server ghi lại trạng thái người dùng trong bộ nhớ hoặc database, trình duyệt mang theo một cái ID qua Cookie. Server dựa vào ID tra ra thông tin người dùng. Nhược điểm là Server phải lưu trữ, và khi có nhiều Server thì chia sẻ rất phiền phức.
- **Token (Thẻ bài)**: Server cấp một cái "thẻ bài" đã mã hóa cho trình duyệt, bên trong chứa thông tin người dùng. Trình duyệt mỗi lần gửi request đều mang theo thẻ bài, Server giải mã xác thực là xong. Ưu điểm là không cần lưu trữ, dễ mở rộng.

Tin tốt là, AI biết nên dùng cách nào, Next.js cũng có giải pháp xác thực chín muồi (như NextAuth). Bạn chỉ cần hiểu: Xác thực là quá trình "chứng minh bạn là bạn", chi tiết kỹ thuật cứ giao cho AI.

### An toàn xuyên suốt chu kỳ phát triển

Bạn học được cách cấu hình biến môi trường, học được bảo vệ định tuyến bằng Middleware, cảm thấy dự án đã rất an toàn rồi. Nhưng sư phụ bảo, đây mới chỉ là phần nổi của tảng băng chìm.

Ứng dụng hiện đại đối mặt với mối đe dọa an ninh xa hơn nhiều so với "lộ mật khẩu" hay "truy cập trái phép". Nếu ứng dụng của bạn sử dụng AI Agents, nó có thể bị tấn công **Prompt Injection** —— kẻ tấn công thông qua đầu vào được thiết kế tinh vi, lừa AI thực hiện thao tác bạn không muốn, ví dụ tiết lộ dữ liệu nhạy cảm. Còn một mối đe dọa kín đáo hơn: **Lộ chứng thực (Credentials Leak)**. Nếu bạn lỡ tay commit API Key vào kho Git, dù sau đó bạn xóa đi, nhưng những chứng thực này vẫn lưu trong lịch sử Git, ai truy cập vào kho cũng xem được.

Bảo vệ an toàn không phải chuyện làm một lần là xong, mà phải xuyên suốt cả chu kỳ phát triển. Tin tốt là, mấy cái này đều có thể bảo AI làm hộ —— bạn có thể bảo AI rà soát code, tìm ra vấn đề bảo mật tiềm ẩn. Bạn bắt đầu hình thành tư duy "an toàn trên hết", khi viết code sẽ vô thức nghĩ: "Chỗ này có rủi ro bảo mật không?", "Cái khóa này có nên để vào biến môi trường không?", "Cái route này có cần thêm Middleware bảo vệ không?". Bạn không còn coi an toàn là chuyện "vuốt đuôi", mà hòa nhập nó vào từng khâu của quy trình phát triển.

**Ý thức an toàn có 3 tầng**:

**Tầng 1: An toàn cơ bản** (Trọng điểm chương này). Biến môi trường, .gitignore, bảo vệ định tuyến Middleware. Đây là bài nhập môn bắt buộc, không làm thì coi như "cởi truồng chạy rông".

**Tầng 2: An toàn ứng dụng**. Khi sản phẩm online, bạn phải đối mặt với mối đe dọa phức tạp hơn. Gồm: **Chống SQL Injection** (dùng ORM tự động xử lý, như Drizzle), **Chống tấn công XSS** (React mặc định escape + xác thực đầu vào), **Chống tấn công CSRF** (Next.js tích hợp sẵn xác thực Token), **Mã hóa dữ liệu nhạy cảm** (mã hóa trường trong database), **Quét lỗ hổng dependency** (định kỳ chạy `pnpm audit`). Nghe thì đáng sợ, nhưng chỉ cần chọn đúng Tech Stack (như Next.js + Drizzle), phần lớn đã được tích hợp sẵn.

**Tầng 3: An toàn chuyên sâu**. Quét lỗ hổng, kiểm thử xâm nhập (Penetration Test), kiểm toán an ninh. Đây là nội dung nâng cao, khi sản phẩm của bạn có người dùng thật, cần định kỳ thực hiện.

An toàn không phải cấu hình một lần, mà là ý thức xuyên suốt chu kỳ phát triển. Mỗi khi viết một dòng code, đều phải tự hỏi: Cái này có an toàn không?"

::: danger Cái giá phải trả thực sự của sự cố an ninh

**Các sự cố an ninh nghiêm trọng những năm gần đây:**

1. **Sự cố lộ Key GitHub (2021)**
   - Hàng ngàn kho code để lộ Key AWS/GCP
   - Tổn thất trung bình: khoảng 360,000 NDT / tài khoản (~1.2 tỷ VNĐ)
   - Kẻ tấn công phát hiện và lợi dụng Key bị lộ trong vòng 5 phút

2. **Bài học của một công ty khởi nghiệp**

   ```bash
   # Câu chuyện có thật
   Developer lỡ tay commit .env vào kho công khai
   → 2 tiếng sau phát hiện phí API bất thường
   → OpenAI phát sinh hóa đơn khoảng 86,000 NDT (~300 triệu VNĐ)
   → Tài khoản công ty bị trộm dùng
   → Không gánh nổi chi phí, dự án chấm dứt
   ```

3. **Phản ứng dây chuyền của lộ dữ liệu**
   - Lộ Key → Database bị truy cập
   - Lộ dữ liệu người dùng → Kiện tụng pháp lý
   - Mất uy tín thương hiệu → Mất người dùng
   - Phạt vi phạm quy định → Công ty phá sản
     :::
     ::: tip Quy trình phát triển an toàn

**Hòa nhập an toàn vào từng giai đoạn:**

**Giai đoạn phân tích nhu cầu**

- Nhận diện dữ liệu và chức năng nhạy cảm
- Đánh giá rủi ro an ninh
- Xây dựng yêu cầu bảo mật

**Giai đoạn thiết kế**

- Thiết kế kiến trúc an toàn
- Chọn Tech Stack an toàn
- Quy hoạch kiểm soát truy cập

**Giai đoạn phát triển**

- Dùng biến môi trường quản lý Key
- Thực thi bảo vệ định tuyến Middleware
- Viết code an toàn

**Giai đoạn kiểm thử**

- Test case an ninh
- Kiểm thử xâm nhập
- Quét lỗ hổng dependency

**Giai đoạn triển khai**

- Xác minh cấu hình biến môi trường
- Bật HTTPS
- Cấu hình Header HTTP an toàn

**Giai đoạn bảo trì**

- Kiểm toán an ninh định kỳ
- Luân chuyển Key (Key Rotation)
- Giám sát log an ninh
  :::
  ::: warning Các mục phải kiểm tra ngay lập tức

**Trước khi tiếp tục, hãy kiểm tra ngay:**

```bash
# 1. Kiểm tra xem .env có bị theo dõi không
git ls-files | grep ".env"

# 2. Kiểm tra thông tin nhạy cảm trong lịch sử Git
git log --all --source -- "*env*"
git log --all --source -- "*password*"
git log --all --source -- "*api*key*"

# 3. Kiểm tra file chưa theo dõi ở nhánh hiện tại
git status

# 4. Kiểm tra cấu hình .gitignore
cat .gitignore | grep -E "\.env|node_modules"
```

**Nếu phát hiện bất kỳ vấn đề nào, xử lý ngay:**

1. Dừng công việc hiện tại
2. Đọc nội dung liên quan trong chương này
3. Sửa chữa vấn đề bảo mật
4. Thu hồi Key đã bị lộ (nếu có)
5. Sinh Key mới
6. Xác minh hiệu quả sửa chữa

:::

### Mục lục chương này

```
#### 7.1 Cấu hình file .env (./01-env-config.md)
Quy tắc cơ bản, quy định đặt tên, phương pháp cấu hình biến môi trường, và rà soát lỗi thường gặp.

#### 7.2 Chi tiết Server vs Client (./02-server-vs-client.md)
Sự khác biệt giữa phía chủ và phía khách, quy tắc truy cập biến môi trường, so sánh phương thức render.

#### 7.3 Server-Side Rendering vs Client-Side Rendering (./03-ssr-vs-csr.md)
Sự khác biệt giữa SSR, CSR, SSG, quá trình Hydration, chiến lược tối ưu hiệu năng.

#### 7.4 Thực hành tốt nhất .gitignore (./04-gitignore-best-practices.md)
Tác dụng, cú pháp của .gitignore, danh sách kiểm tra an toàn, và cách xử lý file nhạy cảm.

#### 7.5 Đồng bộ biến môi trường lên Cloud (./05-sync-env-to-cloud.md)
Cách cấu hình biến môi trường trên Vercel, Railway, Docker, quy trình deploy tự động hóa.

#### 7.6 Bảo vệ định tuyến Middleware (./06-middleware-protection.md) 🔴
Sử dụng Next.js Middleware thực hiện bảo vệ định tuyến, xác thực ủy quyền, giới hạn tốc độ...

#### 7.7 Danh sách kiểm tra an toàn (./07-security-checklist.md)
Danh sách kiểm tra an toàn trọn vẹn, bao gồm các phương diện biến môi trường, Git, xác thực, định tuyến, dữ liệu, truyền tải, dependency, log, deploy...

#### 7.8 Bảo vệ an ninh nâng cao (./08-advanced-security.md) 🟡
Phòng chống CSRF, XSS, SQL Injection, giới hạn tốc độ, chính sách an ninh nội dung (CSP), mã hóa dữ liệu nhạy cảm, an ninh ứng dụng AI...
```
