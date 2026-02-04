---
title: "Chương 4: Kiến thức chung về phát triển và Tech Stack"
---

# Chương 4: Kiến thức chung về phát triển và Tech Stack

## Lời tựa

Trước khi bắt tay vào viết code, sư phụ dặn bạn rằng có một số kiến thức phát triển cốt lõi cần phải nắm được. Những kiến thức này sẽ không trực tiếp dạy bạn viết code, nhưng sẽ giúp bạn hiểu code vận hành thế nào trên mạng Internet.

### Lựa chọn Tech Stack

Việc chọn Tech Stack nên được thực hiện sau khi đã chốt PRD. Sư phụ nói: "Phải làm rõ muốn làm cái gì trước, rồi mới quyết định dùng cái gì để làm."

Đối diện với bao nhiêu lựa chọn công nghệ, người mới dễ bị hoang mang. Thực ra có một khung quyết định đơn giản: Fullstack Next.js (thân thiện AI, hệ sinh thái chín muồi, deploy tiện lợi), trừ khi dự án của bạn thuần túy là Frontend thì mới cân nhắc Vite; Database thì dùng PostgreSQL (Quan hệ + JSONB + pgvector, khả năng mở rộng mạnh).

**Hai cách托管 (hosting) PostgreSQL**: Supabase và Neon đều là dịch vụ cloud hosting PostgreSQL, nhưng định vị khác nhau. **Supabase** cung cấp trọn bộ tính năng Backend (Authentication, Storage, Realtime), phù hợp để phát triển nhanh; **Neon** tập trung vào bản thân Database, nhẹ nhàng và hỗ trợ kiến trúc Serverless, phù hợp với ngữ cảnh có nhu cầu tùy biến Backend cao. Nếu bạn chỉ muốn tập trung vào logic nghiệp vụ, chọn Supabase; nếu bạn cần kiểm soát linh hoạt, chọn Neon.

Tư duy cốt lõi là "Làm rõ nhu cầu → Đánh giá độ phức tạp → Chọn phương án khả thi tối thiểu", chừa đường lui để mở rộng nhưng không thiết kế thừa thãi (over-design). Trong kỷ nguyên AI, Tech Stack càng thống nhất, khả năng hiểu ngữ cảnh của AI càng chuẩn, hiệu suất phát triển càng cao.

> 4.1 Khung quyết định Tech Stack (./01-tech-stack-decision.md) 🟡 - Hệ thống hóa việc lựa chọn Tech Stack phù hợp

### Mối quan hệ giữa PRD và Tài liệu kỹ thuật

Sau khi PRD lặp đến bản 5, phương án sản phẩm cơ bản đã chốt, sư phụ nhắc nhở bạn: Ngoài việc chải chuốt logic nghiệp vụ, bạn còn cần ghi lại phương án thực hiện kỹ thuật cụ thể, đó chính là **Tài liệu kỹ thuật**.

Nhiều người dễ nhầm lẫn PRD và tài liệu kỹ thuật, thực ra phân công của chúng rất rõ ràng:

**PRD (Tài liệu nhu cầu sản phẩm)** trả lời câu hỏi "Làm cái gì":

- Người dùng mục tiêu là ai?
- Chức năng cốt lõi là gì?
- Người dùng tương tác thế nào?
- Trường hợp biên xử lý sao?

**Tài liệu kỹ thuật** trả lời câu hỏi "Làm thế nào":

- Dùng Tech Stack gì? (Next.js + PostgreSQL)
- Cấu trúc bảng Database thiết kế sao? (Bảng User, Bảng Post, Bảng Comment)
- Interface API định nghĩa thế nào? (/api/auth, /api/posts)
- Dịch vụ bên thứ 3 tích hợp ra sao? (OpenAI API, Map Service)
- Phương án deploy là gì? (Edgeone, Vercel, Cloud Server)

Sư phụ nói: "Với cậu hiện tại, không cần câu nệ hình thức, hoàn toàn có thể gộp Tài liệu kỹ thuật và PRD làm một, gọi chung là **Tài liệu dự án**, như thế tra cứu tiện hơn. Nhưng phải phân biệt rõ đâu là tư duy tầng sản phẩm, đâu là quyết định tầng kỹ thuật."

> 4.2 Mối quan hệ giữa PRD và Tài liệu kỹ thuật (./02-prd-and-tech-docs.md) 🟢 - Hiểu sự phân công giữa tài liệu sản phẩm và tài liệu kỹ thuật

### Các cấu kiện cơ bản của lập trình

Sư phụ bảo, trước khi viết code, cậu phải hiểu code được cấu thành từ cái gì đã. Giống như viết văn phải biết mặt chữ, lập trình cũng có "chữ cái" của nó.

Mọi ngôn ngữ lập trình, dù cú pháp khác nhau thế nào, đều dựa trên 4 khái niệm cốt lõi: **Biến**, **Hàm**, **Điều kiện** và **Vòng lặp**.

**Biến** là vật chứa để lưu trữ dữ liệu. Cậu cứ tưởng tượng nó như cái hộp có dán nhãn —— trong hộp chứa dữ liệu, nhãn là tên biến.

**Hàm** là khối lệnh có thể tái sử dụng. Khi cậu thấy mình đang viết đi viết lại những đoạn code giống nhau, đó là lúc nên đóng gói nó thành hàm. Hàm nhận đầu vào (tham số), thực hiện xử lý, rồi trả về đầu ra.

**Phán đoán điều kiện** giúp chương trình có thể thực hiện hành động khác nhau tùy theo tình huống. `if (Người dùng đã đăng nhập) { Hiển thị lời chào } else { Hiển thị nút đăng nhập }` —— chương trình dựa vào điều kiện để quyết định chạy đoạn code nào.

**Vòng lặp** giúp chương trình thực hiện lặp đi lặp lại một thao tác nào đó. Ví dụ cậu muốn gửi email cho 1000 người dùng, không cần viết 1000 lần code gửi mail, chỉ cần viết một vòng lặp: "Với mỗi người dùng trong danh sách, gửi email cho họ".

Bốn khái niệm này là nền tảng của **tính đầy đủ Turing**. Điều này có nghĩa là bất kỳ vấn đề nào có thể tính toán được, đều có thể giải quyết bằng sự tổ hợp của 4 cấu kiện này.

> 4.3 Cách đọc hiểu code AI sinh ra (./03-programming-basics.md) 🟢 - Hiểu 4 khái niệm cốt lõi của code

### Cơ bản về API và HTTP

Sư phụ thấy bạn tò mò, liền giảng giải về nguyên lý tầng đáy của **tương tác Frontend-Backend**. Ông nói, **HTTP** thực ra giống như một hệ thống chỉ lệnh làm việc từ xa. Khi cậu truy cập một trang web trên trình duyệt, bản chất là trình duyệt của cậu (Client) gửi một chỉ lệnh đã được chuẩn hóa tới server từ xa, server nhận lệnh, xử lý việc xong xuôi, rồi trả kết quả về cho cậu theo đúng quy chuẩn đó.

Sư phụ giải thích tiếp, mỗi chỉ lệnh HTTP đều chứa 4 phần cốt lõi:

**Phần 1 là Phương thức (Method)**, bảo cho server biết cậu muốn làm loại việc gì. 4 phương thức phổ biến nhất là:

- **GET** dùng để đọc dữ liệu, ví dụ xem danh sách bài viết
- **POST** dùng để tạo dữ liệu mới, ví dụ submit form đăng ký
- **PUT** hoặc **PATCH** dùng để sửa dữ liệu cũ, ví dụ cập nhật hồ sơ cá nhân
- **DELETE** dùng để xóa dữ liệu, ví dụ hủy tài khoản

**Phần 2 là URL**, chính là địa chỉ cụ thể của tài nguyên cậu muốn thao tác. Ví dụ `https://api.example.com/users/123`, nghĩa là "Truy cập người dùng số 123 trên server example.com".

**Phần 3 là Headers (Thông tin đầu mục)**, dùng để mang theo một số siêu dữ liệu (metadata). Ví dụ token xác thực danh tính của cậu (chứng minh cậu là ai), định dạng dữ liệu cậu mong muốn nhận được (JSON hay XML).

**Phần 4 là Body (Thân nội dung)**, chính là nội dung dữ liệu thực tế cậu muốn gửi đi, ví dụ thông tin điền trong form hoặc một đoạn tham số định dạng JSON.

Tuy AI sẽ giúp cậu xử lý mấy chi tiết này, nhưng hiểu 4 phần này sẽ giúp cậu định vị vấn đề nhanh hơn. Ví dụ API trả về `401 Unauthorized`, cậu biết ngay là Token trong Headers có vấn đề; trả về `404 Not Found`, cậu biết ngay là đường dẫn URL viết sai rồi.

> 4.4 Cơ bản về API và HTTP (./04-api-and-http.md) 🟢 - Nắm vững nguyên lý hoạt động của API và giao thức HTTP

### Khái niệm tách biệt Frontend-Backend

Trong quá trình học về giao tiếp HTTP, sư phụ giải thích trước cho bạn về khái niệm **Frontend** và **Backend**.

**Frontend (Phía khách)** là giao diện người dùng nhìn thấy và thao tác —— code chạy trong trình duyệt. Nút bấm, ô nhập liệu, hình ảnh, văn bản cậu thấy trên web đều là do Frontend render ra. Khi cậu click nút hoặc nhập chữ, code Frontend sẽ phản hồi.

**Backend (Phía chủ)** là code xử lý dữ liệu và logic trên server. Người dùng không thấy nó, nhưng nó chịu trách nhiệm xử lý các yêu cầu từ Frontend gửi tới —— ví dụ truy vấn database, xác thực danh tính, gọi dịch vụ khác. Xử lý xong, Backend trả kết quả về cho Frontend, Frontend lại hiển thị cho người dùng xem.

Trước đây, Frontend và Backend thường là hai dự án độc lập, viết bằng ngôn ngữ khác nhau, do các team khác nhau bảo trì. Giờ đây có **Fullstack Framework như Next.js**, code Frontend và Backend nằm chung một dự án, viết cùng một ngôn ngữ (JavaScript/TypeScript), nhưng trách nhiệm của chúng thì không đổi: Frontend phụ trách "hiển thị", Backend phụ trách "xử lý".

Khi quy hoạch tính năng, cậu gặp phải hai vấn đề bắt buộc phải tính đến từ sớm: Cậu muốn làm hệ thống người dùng, cái này liên quan đến xác thực (Auth). Cậu muốn làm tính năng bản đồ, cái này liên quan đến API bên ngoài. Sư phụ nhắc cậu, đừng nhét tất cả code vào một file, phải học cách chia nhỏ chức năng thành các module khác nhau, ví dụ `auth` (xác thực), `api` (giao diện), `components` (thành phần). **Tư duy module hóa** này là chìa khóa để dự án có thể bảo trì lâu dài.

> 4.5 Khái niệm tách biệt Frontend-Backend (./05-frontend-backend-separation.md) 🟢 - Hiểu kiến trúc phân tách và tương tác giữa Frontend và Backend

### Định dạng file cấu hình

Trong quá trình viết tài liệu kỹ thuật và cấu hình dự án, cậu tiện thể tìm hiểu luôn về **JSON** và **YAML** - mấy định dạng cấu hình trông lạ lạ này.

**JSON** giống như một cách biểu diễn dữ liệu được định dạng nghiêm ngặt. Nó dùng ngoặc nhọn `{}` biểu thị đối tượng, ngoặc vuông `[]` biểu thị mảng, dữ liệu tổ chức theo kiểu "Key: Value". Cậu có thể hiểu JSON là **tiếng phổ thông của thời đại số** —— ngôn ngữ chung để giao tiếp giữa các ngôn ngữ lập trình và hệ thống khác nhau.

**YAML** thì là định dạng cấu hình nhân tính hóa hơn, nó không dùng ngoặc, mà dùng thụt đầu dòng để biểu thị cấp bậc, viết trông gọn gàng hơn. Nhiều file cấu hình (như cấu hình CI/CD) hay dùng định dạng YAML.

Hóa ra, đối với AI mà nói, so với ngôn ngữ tự nhiên tản mạn, những định dạng cấu trúc rõ ràng này mới là "hướng dẫn sử dụng" mà chúng thích đọc nhất.

> 4.6 Định dạng file cấu hình (./06-config-formats.md) 🟢 - Hiểu định dạng cấu hình JSON và YAML

### Thực chiến tích hợp API

Cậu muốn kết nối năng lực AI, hoặc dịch vụ bản đồ... Sư phụ bảo, mấy API bên ngoài này thường thu phí, nhưng rất thân thiện với developer, thường có hạn mức miễn phí cho cậu test. Việc cậu cần làm là:

1. **Lấy chứng thực (Credentials)**: Tìm đến tài liệu developer của nền tảng chính chủ, tìm tính năng cậu cần, đăng ký tài khoản sinh **API Key** (đây là chứng minh thư nhạy cảm của cậu, tuyệt đối không được lộ). Sư phụ dặn kỹ, **nhất định phải lưu Key vào biến môi trường trong file `.env`**, chứ đừng viết chết vào code. Biến môi trường giống như "tường lửa" giữa code và khóa bí mật, chỉ cần cấu hình một lần, chương trình chạy sẽ tự động đọc, vừa đảm bảo tính năng hoạt động, vừa tránh việc cậu upload nhầm khóa lên GitHub bị người ta trộm mất.

2. **Xác định lộ trình kỹ thuật (SDK vs HTTP)**: Sư phụ ngăn cản ý định để AI viết tay HTTP request thô sơ của cậu. Ông giới thiệu khái niệm **SDK (Software Development Kit)** —— chính chủ thường đã đóng gói sẵn các tương tác mạng phức tạp, xử lý lỗi và logic xác thực rồi, chỉ cần cài đặt, tìm tài liệu chính chủ là dùng được ngay. **Quan trọng hơn, SDK chính chủ thường đi kèm định nghĩa kiểu TypeScript hoàn chỉnh**. Điều này tương đương với việc cung cấp hướng dẫn code cho AI, nó biết chính xác có những chức năng nào dùng được, tham số điền sao, cái này đáng tin cậy hơn nhiều so với để nó đoán mò dựa trên HTTP request trắng trơn.

3. **Viết test tối giản**: Cấu hình xong SDK và API Key, sư phụ bảo: "Đừng vội viết chức năng nghiệp vụ, hãy để AI viết cho cậu một đoạn code test đơn giản nhất trước đã." Cái test này chỉ cần làm một việc: Gọi API một lần, xem có nhận được kết quả không.

4. **Xử lý lỗi**: Sư phụ nhắc cậu chú ý mấy vấn đề thường gặp. **Giới hạn tần suất (Rate Limit)** —— API bên ngoài thường không cho gọi vô tội vạ; **Xử lý quá giờ (Timeout)** —— API mà mãi không phản hồi thì chương trình cậu sẽ treo; **Xác thực thất bại** —— Nếu API Key hết hạn hoặc không đúng, sẽ trả về `401 Unauthorized`.

> 4.7 Thực chiến tích hợp API (./07-api-integration.md) 🟢 - Tích hợp API bên ngoài từ con số 0

### Bản hướng dẫn dự án README.md

Code không chỉ để máy chạy, mà còn để người và AI đọc. Cậu đã biết là cần viết **README.md**. Đây không phải thông tin thừa thãi, mà là "hướng dẫn sử dụng" của dự án. Trong đó cậu ghi rõ ràng cách khởi động dự án (`pnpm dev`), cách cấu hình biến môi trường, logic chức năng cốt lõi. Từ đó, bất kể là ai, nhìn tài liệu là bắt tay vào làm được ngay.

README.md giống như "mặt tiền" của dự án, bao gồm:

- **Giới thiệu dự án**: Dự án này làm cái gì?
- **Khởi động nhanh**: Cách cài đặt dependency, chạy dự án
- **Biến môi trường**: Cần cấu hình những khóa và tham số nào
- **Chức năng cốt lõi**: Các module chức năng chính và logic tương tác
- **Tech Stack**: Đã dùng những công nghệ và công cụ gì
- **Hướng dẫn đóng góp**: Làm sao để tham gia phát triển dự án

> 4.8 Cấu trúc bản hướng dẫn dự án (./08-readme-structure.md) 🟢 - Viết tài liệu README.md hoàn chỉnh cho dự án

---

### Điều hướng tiểu tiết

```
- **4.1 Khung quyết định Tech Stack** (./01-tech-stack-decision.md) 🟡 - Hệ thống hóa việc lựa chọn Tech Stack phù hợp
- **4.2 Mối quan hệ giữa PRD và Tài liệu kỹ thuật** (./02-prd-and-tech-docs.md) 🟢 - Hiểu sự phân công giữa tài liệu sản phẩm và tài liệu kỹ thuật
- **4.3 Cách đọc hiểu code AI sinh ra** (./03-programming-basics.md) 🟢 - Hiểu 4 khái niệm cốt lõi của code
- **4.4 Cơ bản về API và HTTP** (./04-api-and-http.md) 🟢 - Nắm vững nguyên lý hoạt động của API và giao thức HTTP
- **4.5 Khái niệm tách biệt Frontend-Backend** (./05-frontend-backend-separation.md) 🟢 - Hiểu kiến trúc phân tách và tương tác giữa Frontend và Backend
- **4.6 Định dạng file cấu hình** (./06-config-formats.md) 🟢 - Hiểu định dạng cấu hình JSON và YAML
- **4.7 Thực chiến tích hợp API** (./07-api-integration.md) 🟢 - Tích hợp API bên ngoài từ con số 0
- **4.8 Cấu trúc bản hướng dẫn dự án** (./08-readme-structure.md) 🟢 - Viết tài liệu README.md hoàn chỉnh cho dự án
```

---

### Mục tiêu học tập

Học xong chương này, bạn sẽ có thể:

- ✅ Hiểu khung quyết định lựa chọn Tech Stack
- ✅ Phân biệt tác dụng của PRD và Tài liệu kỹ thuật
- ✅ Hiểu 4 cấu kiện cơ bản của code (biến, hàm, điều kiện, vòng lặp)
- ✅ Nắm vững nguyên lý cơ bản của giao thức HTTP
- ✅ Hiểu khái niệm tách biệt Frontend-Backend
- ✅ Biết cách tích hợp API bên ngoài
- ✅ Hiểu định dạng cấu hình JSON và YAML
- ✅ Viết được README dự án rõ ràng
- ✅ Hình thành tư duy module hóa

---

**Chương tiếp theo**: Chương 5: 3 trạng thái vận hành của code và nguyên lý build (../05-build-and-runtime-modes/index.md)
