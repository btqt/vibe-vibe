---
title: "Chương 8: Bền vững hóa dữ liệu và Cơ sở dữ liệu"
---

# Chương 8: Bền vững hóa dữ liệu và Cơ sở dữ liệu

## Lời tựa

Giao diện dựng lên trông cũng ra dáng rồi đấy, nhưng bạn phát hiện một vấn đề khó xử: Mỗi lần refresh trang web, mấy cái form vừa điền, mấy đoạn hội thoại vừa sinh ra đều biến mất sạch.

Sư phụ bảo bạn, đó là vì dữ liệu trong trình duyệt mặc định chỉ lưu trữ trong **bộ nhớ (RAM)** tạm thời. Muốn dữ liệu vẫn còn sau khi tắt hoặc refresh trang, bạn cần **Bền vững hóa dữ liệu (Data Persistence)**.

Ông nghiêm túc nhắc nhở bạn: **Dữ liệu là nền tảng của mọi nghiệp vụ**. Code Frontend mất thì có thể viết lại, UI xấu thì có thể thay da đổi thịt, nhưng nếu dữ liệu người dùng trong database mà mất, mà loạn, thì sản phẩm của bạn coi như toi đời. Đây là lý do tại sao phát triển Backend thường chú trọng tính chặt chẽ hơn Frontend —— vì thứ bạn đang canh giữ là linh hồn của sản phẩm.

### Lưu trữ file JSON

Bền vững hóa không nhất thiết cứ phải cài phần mềm phức tạp. Cách đơn giản nhất, thực ra là tận dụng định dạng **JSON** mà bạn học được trong file cấu hình, lưu dữ liệu thành file `.json`. Mỗi dòng lịch sử chat hay thông tin người dùng, bản chất chính là một đoạn văn bản. Lưu nó vào file trong ổ cứng, lần sau đọc file ra là khôi phục được. Cách này giúp bạn hiểu ngay bản chất của "Cơ sở dữ liệu" —— **chẳng qua là đọc ghi hiệu quả các file trên ổ cứng.**

### Cơ sở dữ liệu quan hệ (Relational DB)

Tuy file JSON đơn giản, nhưng khi dữ liệu nhiều lên, muốn tìm "tất cả người dùng sống ở Hà Nội và trên 20 tuổi", thì phải duyệt qua toàn bộ file, hiệu suất cực thấp. Thế là bạn tiếp xúc với **Relational Databases (Cơ sở dữ liệu quan hệ)**. Sư phụ bảo bạn cứ tưởng tượng nó là một cái **Siêu Excel**, muốn hiểu nó chỉ cần nắm vài điểm then chốt:

- **Table (Bảng)**: Chính là một Excel Sheet (Trang tính), ví dụ bảng `Users`.
- **Row (Hàng)**: Một hàng trong bảng, đại diện cho một dữ liệu cụ thể (ví dụ người dùng Nguyễn Văn A).
- **Column (Cột)**: Tiêu đề của bảng, định nghĩa dữ liệu có những thuộc tính nào (tên, tuổi, email).
- **Primary Key (Khóa chính)**: Số chứng minh thư duy nhất của mỗi hàng dữ liệu (thường là `id`), tuyệt đối không được trùng lặp.
- **Foreign Key (Khóa ngoại)**: Manh mối dùng để liên kết các bảng khác. Ví dụ trong bảng `Orders` (đơn hàng) ghi lại một `user_id`, là có thể lần ra đơn hàng này thuộc về người dùng nào.

**Làm sao phán đoán thiết kế bảng của AI là tốt hay xấu?** Người mới thường khó nhìn ra ngay Schema thiết kế có hợp lý không. Sư phụ truyền cho bạn một chiêu **"AI phản biện chéo"** (dân dã gọi là "luyện cổ"): Bạn bảo **AI số 1** giúp bạn thiết kế cấu trúc bảng, rồi đem code sinh ra gửi cho **AI số 2** hoặc **AI số 3**, hỏi nó: "**Với tư cách là một kiến trúc sư cơ sở dữ liệu thâm niên, dựa trên PRD và ngữ cảnh nghiệp vụ thực tế của tôi, thiết kế này có hợp lý không, có ẩn họa hiệu năng hay lỗ hổng logic tiềm tàng nào không?**" Thường qua hai vòng "song đấu" như vậy, bạn sẽ có được một mô hình database cực kỳ vững chắc.

### Drizzle Schema

Ngôn ngữ tiêu chuẩn để thao tác database là SQL, trong hướng dẫn này chúng ta dùng **Drizzle ORM**. Drizzle sử dụng TypeScript để định nghĩa Schema, AI sẽ dựa vào tài liệu PRD để tự động sinh ra.

Ví dụ PRD viết rõ "một người dùng có thể đăng nhiều bài viết", AI sẽ tự động thêm trường `posts` vào bảng `User`, và thêm khóa ngoại `authorId` vào bảng `Post`. **Công việc của bạn là rà soát xem code AI sinh ra có đúng không.**

Sư phụ nói: "Mấu chốt của thiết kế database là hiểu quan hệ nghiệp vụ. AI xử lý được việc hiện thực hóa kỹ thuật, nhưng 'người dùng và đơn hàng có quan hệ gì' thì cần bạn hiểu nghiệp vụ."

Để có thể xem hiểu bài tập AI nộp, sư phụ chỉ vào một đoạn code, dạy bạn hiểu từng dòng:

```typescript
// src/db/schema.ts
import { pgTable, serial, text, timestamp, integer } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: serial("id").primaryKey(), // Khóa chính tự tăng
  email: text("email").notNull().unique(), // Bắt buộc điền và duy nhất
  name: text("name"), // Trường tùy chọn (không thêm .notNull())
  createdAt: timestamp("created_at").defaultNow(),
});

// Ví dụ bảng liên kết
export const posts = pgTable("posts", {
  id: serial("id").primaryKey(),
  title: text("title").notNull(),
  authorId: integer("author_id").references(() => users.id), // Liên kết khóa ngoại
});
```

- **`pgTable`**: Định nghĩa cấu trúc bảng PostgreSQL
- **Kiểu dữ liệu**: `serial` (số nguyên tự tăng), `text` (văn bản), `boolean` (đúng sai), `timestamp` (thời gian), `integer` (số nguyên)
- **Trường tùy chọn**: Trường không thêm `.notNull()` mặc định là tùy chọn (có thể null)
- **`.unique()`**: Giá trị trường là duy nhất
- **`.references()`**: Định nghĩa liên kết khóa ngoại giữa các bảng

### Thao tác Cơ sở dữ liệu

Nắm vững thao tác database, bạn chỉ cần hiểu 3 khái niệm cốt lõi.

**Thao tác CRUD**: Tuy không cần viết SQL, nhưng bạn bắt buộc phải khắc cốt ghi tâm **CRUD** (Create Tạo, Read Đọc, Update Sửa, Delete Xóa). Đây là nền tảng của mọi thao tác database, cũng là thuật ngữ chung cốt lõi để bạn chỉ huy AI thao tác dữ liệu.

**Transaction (Giao dịch) —— Đảm bảo tính toàn vẹn dữ liệu**: Sư phụ bổ sung một khái niệm then chốt: "Có những thao tác liên quan đến nhiều thay đổi database, bắt buộc phải 'đóng gói' thực hiện. Ví dụ chuyển tiền —— trừ tiền tài khoản A, cộng tiền tài khoản B. Nếu trừ tiền thành công mà cộng tiền thất bại, dữ liệu sẽ bị loạn." **Transaction** chính là đóng gói nhiều thao tác thành một thao tác nguyên tử "hoặc là thành công tất cả, hoặc là thất bại tất cả". Cái này cực kỳ cần thiết khi xử lý các nghiệp vụ quan trọng như tài chính, đơn hàng.

**Index (Chỉ mục) —— Tăng tốc truy vấn**: Sư phụ bổ sung: "Cậu có thể sẽ gặp vấn đề này —— sau khi dữ liệu nhiều lên, truy vấn càng ngày càng chậm. Ví dụ tìm một email nào đó trong hàng triệu người dùng, nếu không có Index, database phải quét từng dòng một." **Index** giống như mục lục của cuốn sách. Không có Index, database phải quét toàn bảng (Full Table Scan); có Index, định vị ngay vị trí mục tiêu, tốc độ nhanh hơn mấy chục lần. Nhưng Index không phải càng nhiều càng tốt. Nó chiếm thêm không gian, hơn nữa khi thêm xóa dữ liệu phải cập nhật Index, ngược lại còn ảnh hưởng hiệu năng ghi. Cho nên thường chỉ tạo Index trên "các trường thường xuyên truy vấn", ví dụ `email`, `created_at`.

AI biết lúc nào cần dùng Transaction, trường nào cần tạo Index. Bạn nắm vững những khái niệm cốt lõi này, sẽ giao tiếp nhu cầu với AI tốt hơn.

### Tính toàn vẹn và Kiểm tra dữ liệu (Validation)

"Dữ liệu lưu vào rồi," sư phụ hỏi, "nhưng lưu có đúng không?"

Ông lấy vài ví dụ: Người dùng điền email thành `hello` (sai định dạng), tuổi điền thành `-5` (sai phạm vi), đơn hàng tham chiếu đến một ID người dùng không tồn tại (toàn vẹn tham chiếu). **Kiểm tra dữ liệu chính là để ngăn chặn tình huống này xảy ra**.

Sư phụ bảo, kiểm tra có **3 phòng tuyến**:

**Phòng tuyến 1: Ràng buộc Database**. Lúc định nghĩa Schema dùng `.notNull()`, `.unique()`, `.references()` chính là ràng buộc tầng database. Mấy cái này là "thiết luật", cho dù code có bug, database cũng sẽ từ chối dữ liệu vi phạm.

**Phòng tuyến 2: Kiểm tra Backend API**. Khi xử lý request người dùng, AI sẽ tự động thêm logic kiểm tra. Ví dụ định dạng email, độ dài mật khẩu, phạm vi giá trị enum... Việc này giúp chặn lỗi ngay trước khi dữ liệu đến được database.

**Phòng tuyến 3: Xác thực Frontend Form**. Trước khi người dùng submit, browser kiểm tra trước một lượt. Ví dụ `<input type="email">` sẽ tự động kiểm tra định dạng email, các thuộc tính `required`, `min`, `max` của HTML5 cũng làm được kiểm tra cơ bản.

Sư phụ nhắc nhở: **3 phòng tuyến mỗi cái một tác dụng**. Ràng buộc database là bảo hiểm cuối cùng, kiểm tra Backend là phòng tuyến chính, kiểm tra Frontend là vì trải nghiệm người dùng (phản hồi nhanh, không cần đợi request mạng). Đừng vì có Frontend check rồi mà bỏ qua bảo vệ tầng Backend và Database —— người dùng có thể gọi trực tiếp API, vòng qua Frontend.

AI biết nên thêm kiểm tra gì ở mỗi tầng. Bạn nhớ kỹ nguyên tắc "phòng tuyến không chỉ có một", khi cộng tác với AI sẽ có định hướng hơn.

### Sao lưu dữ liệu

"Trước khi giảng bất kỳ kỹ thuật nào," sư phụ nghiêm túc nói, "phải giảng **ý thức sao lưu dữ liệu** trước. Dữ liệu là linh hồn của sản phẩm, sao lưu là giới hạn cuối cùng của phát triển. Rất nhiều người coi thường điểm này, cho đến một ngày database sập, mới phát hiện toàn bộ dữ liệu người dùng mất sạch, đây là hậu quả mang tính thảm họa.

**Sao lưu tự động không phải là tùy chọn, mà là môn bắt buộc**. Chiến lược sao lưu phải bao gồm: Sao lưu tự động (hàng ngày), sao lưu đa điểm (cloud + local), diễn tập khôi phục định kỳ (xác minh sao lưu dùng được). Quá nhiều người làm sao lưu nhưng chưa bao giờ test thử, đợi đến lúc cần khôi phục mới phát hiện file sao lưu bị hỏng.

Tầm quan trọng của diễn tập khôi phục thảm họa không kém gì bản thân việc sao lưu. Nếu chưa diễn tập bao giờ, cậu căn bản không biết bản sao lưu có thực sự dùng được hay không."

### Lựa chọn Cơ sở dữ liệu

Để thực chiến, bạn tiếp xúc với **SQLite**, nó là một database dạng file gọn nhẹ, không cần cài đặt, rất hợp để dev test. Nhưng vì khả năng mở rộng trong tương lai, sư phụ khuyên bạn dùng **PostgreSQL**.

**Cách thức Hosting PostgreSQL**: Supabase và Neon là hai dịch vụ cloud hosting PostgreSQL phổ biến, nhưng định vị khác nhau.

**Supabase** là một BaaS (Backend as a Service) hoàn chỉnh, ngoài database PostgreSQL, còn cung cấp Auth (xác thực), Storage (lưu trữ), Realtime (đăng ký thời gian thực), Edge Functions... Nếu bạn muốn kiểm chứng MVP nhanh chóng, không muốn bận tâm chi tiết Backend, Supabase là lựa chọn rất tốt.

**Neon** thì tập trung vào bản thân database, cung cấp PostgreSQL kiến trúc Serverless, có thể tự động co giãn (scale) theo nhu cầu, phù hợp với ngữ cảnh có nhu cầu tùy chỉnh Backend.

Nhưng sư phụ nhắc bạn, hướng dẫn này khuyên dùng PostgreSQL tiêu chuẩn, chứ không bị trói buộc bởi bất kỳ BaaS nào. PostgreSQL tiêu chuẩn giúp bạn hiểu sâu hơn các khái niệm cốt lõi của database, chi phí di dời thấp hơn, tương lai có thể tùy theo nhu cầu mà chọn bất kỳ nền tảng hosting nào hoặc tự dựng (self-host). Supabase, Neon, Railway... đều chỉ là các cách hosting khác nhau của PostgreSQL, thứ bạn nắm vững là bản thân database, chứ không phải một nền tảng dịch vụ cụ thể nào đó. Tư duy "không bị trói buộc" này, trong thời đại AI đặc biệt quan trọng.

Tại sao là PostgreSQL? Lấy một ví dụ thuyết phục nhất: **Backend của ChatGPT (OpenAI) dùng chính là PostgreSQL**. Họ dùng một DB PostgreSQL chủ (Master) để gánh 800 triệu người dùng, xử lý hàng triệu truy vấn mỗi giây. Nếu PostgreSQL gánh được quy mô của ChatGPT, thì với bạn chắc chắn là dư dùng.

Bạn có thể tò mò "DB chủ" là gì. Nói đơn giản về khái niệm **Chủ tớ (Master-Slave) và Tính sẵn sàng cao (High Availability)**: Môi trường production thường sẽ có một **DB chủ** (phụ trách ghi dữ liệu) và nhiều **DB tớ** (phụ trách đọc dữ liệu), dữ liệu từ DB chủ sẽ tự động đồng bộ sang DB tớ. Như vậy vừa phân tán áp lực đọc, vừa đảm bảo khi DB chủ gặp sự cố thì DB tớ có thể lên thay —— đây là tư duy cơ bản của **HA (High Availability)**. Có điều mấy cái này là việc của tầng vận hành (Ops), giai đoạn phát triển bạn chỉ cần 1 database là đủ, các nền tảng hosting sẽ giúp bạn xử lý mấy việc này.

Ngoài việc được các công ty AI hàng đầu bảo chứng, PostgreSQL còn có 2 đặc tính khiến developer AI không thể chối từ:

1. **Hỗ trợ JSONB**: Tuy là database quan hệ, nhưng nó có thể lưu trực tiếp dữ liệu JSON giống như NoSQL. Điều này có nghĩa là bạn có thể ném trực tiếp những dữ liệu cấu trúc không xác định phức tạp do AI sinh ra vào đó, vừa có quy tắc (SQL) vừa có sự linh hoạt (NoSQL).
2. **pgvector (Truy vấn vector)**: Đây là đòn sát thủ trong thời đại AI. Nó có thể lưu trữ và truy vấn "dữ liệu vector", đây là kỹ thuật cốt lõi để hiện thực hóa **Trí nhớ dài hạn cho AI** (RAG). Chọn PostgreSQL, đồng nghĩa với việc trải sẵn con đường tương lai cho ứng dụng AI của bạn.

### Tránh hố thực chiến

**Database Phát triển vs Database Sản xuất**. Sư phụ bảo, trong team chuyên nghiệp, thường sẽ có 2 bộ database: Môi trường Development dùng để test và debug, môi trường Production cho người dùng thật sử dụng. Tuy Best Practice s là tách biệt môi trường, nhưng ở giai đoạn học tập, **dùng một bộ database để làm quen nhanh là chấp nhận được** —— phát triển trực tiếp trên database cloud, như vậy khi deploy không cần di dời dữ liệu, bớt đi rất nhiều phiền phức. **Khi ứng dụng của bạn có người dùng thật, cực lực khuyên tách biệt môi trường Dev và Prod**, để tránh ô nhiễm dữ liệu và rủi ro bảo mật.

**Đánh dấu dữ liệu**: Đã dùng chung 1 database cho Dev và Prod, thì làm sao phân biệt dữ liệu test và dữ liệu thật? Sư phụ dạy bạn 2 cách: Một là trước khi online thì xóa thủ công dữ liệu test; Hai là lúc thiết kế bảng thêm một trường `isTest` hoặc `isDev`, dữ liệu ghi vào lúc dev đều đánh dấu là `true`, sau khi online lúc truy vấn thì lọc bỏ những dữ liệu này. Cách này vừa tiết kiệm tiền vừa an toàn.

**Dọn dẹp dữ liệu test**: Khi bạn cần xóa dữ liệu test, bảo AI "xóa hết dữ liệu test đi", nó sẽ sinh code kiểu `DELETE FROM users WHERE isTest = true`. Bạn xem là hiểu dòng code này —— chỉ xóa dữ liệu được đánh dấu là test. **Đây chính là tác dụng của trường `isTest`**, nó giống như một cái van an toàn, đảm bảo chỉ xóa dữ liệu test, không lỡ tay xóa nhầm người dùng thật.

**Connection URL (Chuỗi kết nối)**: Bạn thường thấy báo lỗi `Error: Invalid URL`. Sư phụ bảo, kết nối database giống như gửi thư, định dạng bắt buộc phải tuân thủ nghiêm ngặt: `postgresql://username:password@host:port/database_name`. Sai bất kỳ dấu chấm dấu phẩy nào, hoặc trong mật khẩu có chứa ký tự đặc biệt (cần escape), đều sẽ dẫn đến kết nối thất bại.

#### Mục lục chương này

```
#### 8.1 Sự tiến hóa của lưu trữ dữ liệu (./01-data-storage-evolution.md)
Con đường tiến hóa từ lưu trữ bộ nhớ đến database, so sánh các phương thức lưu trữ và ngữ cảnh áp dụng.

#### 8.2 Cơ bản về Database quan hệ (./02-rdbms-basics.md)
Các khái niệm cốt lõi: Bảng, Khóa chính, Khóa ngoại, Quan hệ, Ràng buộc, Index...

#### 8.3 Lựa chọn phương án Backend (./03-backend-options.md) 🟡
So sánh và hướng dẫn lựa chọn giữa 3 phương án: BaaS, Serverless, Traditional Backend.

#### 8.4 Lý niệm cốt lõi thiết kế Database (./04-db-design-concepts.md) 🟡
Quy trình trọn vẹn từ PRD đến thiết kế DB, cách nhận diện thực thể, định nghĩa quan hệ, tối ưu cấu trúc.

#### 8.5 Nhập môn Drizzle ORM (./05-drizzle-intro.md)
Cài đặt Drizzle ORM, định nghĩa Schema, quản lý Migration, xây dựng truy vấn.

#### 8.6 Thực chiến di dời Database (Migration) (./06-db-migration.md)
Luồng làm việc Migration, các kịch bản Migration thường gặp, Migration môi trường Production, chiến lược di dời dữ liệu.

#### 8.7 Chi tiết thao tác CRUD (./07-crud-details.md)
Cách dùng đầy đủ của Create, Read, Update, Delete; tối ưu truy vấn; thao tác Transaction.

#### 8.8 Cấu hình và sử dụng Supabase (./08-supabase-config.md) 🟡
Làm quen nhanh nền tảng Supabase, thao tác database, xác thực danh tính, đăng ký thời gian thực, lưu trữ file.

#### 8.9 Quyết định lựa chọn Database (./09-db-selection.md) 🟡
So sánh và gợi ý lựa chọn các database chủ lưu: PostgreSQL, MySQL, MongoDB, SQLite...

#### 8.10 Chiến lược sao lưu Database (./10-db-backup-strategy.md)
Các loại hình sao lưu, lựa chọn chiến lược, sao lưu tự động, diễn tập khôi phục thảm họa.

#### 8.11 Tối ưu hiệu năng Database (./11-db-performance.md)
Tối ưu truy vấn, tối ưu Index, cấu hình Connection Pool, chiến lược Cache, giám sát hiệu năng.

#### 8.12 Case thực chiến tránh hố (./12-real-world-pitfalls.md)
10 sai lầm thường gặp và giải pháp, tổng kết các thực hành tốt nhất (Best Practices).
```
