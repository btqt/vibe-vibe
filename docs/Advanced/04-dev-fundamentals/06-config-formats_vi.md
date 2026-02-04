---
title: "4.6 Định dạng file cấu hình"
description: "Hiểu định dạng cấu hình JSON và YAML"
chapter: "Chương 4"
priority: "🟢"
---

# 4.6 Định dạng file cấu hình 🟢

> **Đọc xong phần này, bạn sẽ thu hoạch được:**
>
> - Hiểu cú pháp và công dụng của JSON và YAML
> - Nắm vững phương pháp đọc viết hai định dạng này
> - Biết kịch bản áp dụng của chúng trong phát triển
> - Hiểu giá trị của dữ liệu cấu trúc hóa đối với AI

> JSON và YAML là "tiếng phổ thông" của thời đại kỹ thuật số —— ngôn ngữ chung để giao tiếp giữa các hệ thống khác nhau.

---

## Dữ liệu cấu trúc hóa là gì

Dữ liệu cấu trúc hóa là cách biểu diễn dữ liệu được tổ chức theo quy tắc nghiêm ngặt. Chúng giúp máy tính có thể phân tích và hiểu dữ liệu một cách chính xác.

So với ngôn ngữ tự nhiên, định dạng dạng cấu trúc có các đặc điểm:

- Định dạng thống nhất, không gây hiểu lầm
- Dễ dàng cho chương trình phân tích (parse) và tạo mới (generate)
- Dùng chung được trên nhiều ngôn ngữ, nền tảng
- AI có thể hiểu chính xác

Hiểu giá trị của dữ liệu cấu trúc hóa có thể nhìn từ góc độ tiến hóa của ngôn ngữ lập trình. Các ngôn ngữ đời đầu khá gần với mã máy, lập trình viên phải xử lý trực tiếp địa chỉ bộ nhớ và dữ liệu nhị phân. Khi ngôn ngữ bậc cao xuất hiện, dữ liệu được trừu tượng hóa thành các khái niệm biến, đối tượng, mảng, lập trình viên có thể mô tả dữ liệu theo cách tự nhiên hơn. JSON và YAML đại diện cho tầng trừu tượng cao nhất của sự phát triển này —— chúng không phải cú pháp của một ngôn ngữ cụ thể nào, mà là "ngôn ngữ chung" mà mọi ngôn ngữ hiện đại đều hiểu. Dù bạn dùng Dictionary của Python, Object của JavaScript, hay Struct của Go, cuối cùng đều có thể chuyển đổi không sứt mẻ sang định dạng JSON để ngôn ngữ khác đọc hiểu. Tính phổ quát này là nền tảng để hệ sinh thái phần mềm hiện đại có thể kết nối với nhau.

::: tip Sở thích đọc của AI

So với ngôn ngữ tự nhiên tản mạn, định dạng cấu trúc rõ ràng là loại "hướng dẫn sử dụng" mà AI thích đọc nhất. Khi bạn viết nhu cầu hoặc cấu hình bằng JSON/YAML, độ chính xác trong cách hiểu của AI sẽ tăng vọt.

:::

---

## Định dạng JSON

**JSON (JavaScript Object Notation)** là định dạng trao đổi dữ liệu phổ biến nhất.

### Quy tắc cú pháp

```json
{
  "name": "Trương Tam",
  "age": 25,
  "email": "zhang@example.com",
  "address": {
    "city": "Bắc Kinh",
    "district": "Triều Dương"
  },
  "hobbies": ["Đọc sách", "Bơi lội", "Lập trình"]
}
```

**Giải thích quy tắc**:

- Dùng ngoặc nhọn `{}` biểu thị đối tượng (Object)
- Dùng ngoặc vuông `[]` biểu thị mảng (Array)
- Dữ liệu tổ chức theo cặp "Khóa: Giá trị" (Key: Value)
- Khóa bắt buộc phải bao quanh bởi dấu ngoặc kép
- Các cặp khóa-giá trị phân cách bằng dấu phẩy

### Kiểu dữ liệu

| Kiểu               | Ví dụ              | Giải thích                  |
| ------------------ | ------------------ | --------------------------- |
| Chuỗi (String)     | `"hello"`          | Bao quanh bởi dấu ngoặc kép |
| Số (Number)        | `123`, `3.14`      | Số nguyên hoặc số thực      |
| Boolean            | `true`, `false`    | Đúng/Sai                    |
| Mảng (Array)       | `[1, 2, 3]`        | Danh sách dữ liệu có thứ tự |
| Đối tượng (Object) | `{"key": "value"}` | Tập hợp các cặp Key-Value   |
| Null               | `null`             | Giá trị rỗng                |

### Lợi thế của JSON

| Lợi thế           | Giải thích                                    |
| ----------------- | --------------------------------------------- |
| **Tính phổ quát** | Mọi ngôn ngữ lập trình đều hỗ trợ             |
| **Tính dễ đọc**   | Con người có thể đọc hiểu dễ dàng             |
| **Gọn nhẹ**       | Định dạng súc tích, không lãng phí dung lượng |
| **Chuẩn Web**     | Định dạng chuẩn của API HTTP                  |

::: tip JSON là tiếng phổ thông thời kỹ thuật số

Dù bạn dùng Python viết Backend, dùng JavaScript viết Frontend, hay nhờ AI viết code, thì mọi người đều dùng JSON để truyền tải dữ liệu. Nếu không dùng JSON, mỗi ngôn ngữ có thể sẽ dùng định dạng "phương ngữ" của riêng mình, giống như thời xưa mỗi vùng nói một tiếng vậy, giao tiếp rất khó khăn.

:::

---

## Định dạng YAML

**YAML (YAML Ain't Markup Language)** là một định dạng cấu hình nhân tính hóa hơn.

### Quy tắc cú pháp

```yaml
# Thông tin người dùng
name: Trương Tam
age: 25
email: zhang@example.com

# Thông tin địa chỉ
address:
  city: Bắc Kinh
  district: Triều Dương

# Danh sách sở thích
hobbies:
  - Đọc sách
  - Bơi lội
  - Lập trình
```

**Giải thích quy tắc**:

- Dùng thụt đầu dòng (indent) để biểu thị cấp bậc (dùng dấu cách, không dùng Tab)
- Cặp Key-Value phân cách bằng dấu hai chấm
- Phần tử mảng biểu thị bằng dấu gạch ngang `-`
- Dấu `#` mở đầu cho chú thích (comment)

### Lợi thế của YAML

| Lợi thế              | Giải thích                                |
| -------------------- | ----------------------------------------- |
| **Dễ đọc hơn**       | Tự nhiên như viết danh sách liệt kê       |
| **Hỗ trợ chú thích** | Có thể thêm text giải thích               |
| **Súc tích**         | Không cần ngoặc nhọn, ngoặc kép, dấu phẩy |
| **Hợp làm cấu hình** | Thường dùng cho file cấu hình hệ thống    |

::: tip YAML vs JSON

YAML giống "danh sách liệt kê", JSON giống "bảng biểu". Viết cấu hình dùng YAML thoải mái hơn, truyền dữ liệu dùng JSON chuẩn mực hơn.

:::

---

## CSV: Định dạng file phẳng

Khi bàn về dữ liệu cấu trúc hóa, **CSV (Comma-Separated Values)** là định dạng đơn giản nhất. Nó dùng văn bản thuần túy để lưu trữ dữ liệu dạng bảng, mỗi dòng là một bản ghi, các trường phân cách bằng dấu phẩy.

**Ví dụ CSV**:

```csv
name,email,age
Trương Tam,zhang@example.com,25
Lý Tứ,li@example.com,30
```

**Đặc điểm của CSV**:

- **Đơn giản**: Trình soạn thảo văn bản nào cũng mở được
- **Tương thích tốt**: Excel, Google Sheets đều import trực tiếp được
- **Dung lượng nhỏ**: Không có các ký tự đánh dấu định dạng dư thừa

**Hạn chế của CSV**:

- Chỉ biểu diễn được bảng 2 chiều (hàng và cột)
- Không hỗ trợ cấu trúc lồng nhau (nested)
- Không có kiểu dữ liệu (tất cả đều là chuỗi)
- Xử lý các mối quan hệ phức tạp rất yếu

**CSV vs JSON/YAML**:

| Đặc tính          | CSV                                       | JSON/YAML                                     |
| ----------------- | ----------------------------------------- | --------------------------------------------- |
| Cấu trúc          | Bảng 2 chiều                              | Lồng nhau tùy ý                               |
| Kiểu dữ liệu      | Không                                     | Chuỗi, Số, Boolean...                         |
| Biểu diễn quan hệ | Yếu                                       | Mạnh                                          |
| Ngữ cảnh sử dụng  | Xuất dữ liệu đơn giản, trao đổi bảng biểu | File cấu hình, dữ liệu API, cấu trúc phức tạp |

Khi bạn cần xuất dữ liệu từ bảng tính, hoặc trao đổi dữ liệu đơn giản với đồng nghiệp dùng Excel, CSV rất phù hợp. Nhưng để phát triển Web App, JSON và YAML là lựa chọn tốt hơn vì chúng biểu diễn được cấu trúc dữ liệu phức tạp hơn.

---

## So sánh hai định dạng

| Đặc tính         | JSON                               | YAML                          |
| ---------------- | ---------------------------------- | ----------------------------- |
| Cú pháp          | Nghiêm ngặt, cần ngoặc và dấu phẩy | Thoáng, dựa vào thụt đầu dòng |
| Chú thích        | Không hỗ trợ                       | Hỗ trợ `#`                    |
| Tính dễ đọc      | Khá                                | Tốt hơn                       |
| Ngữ cảnh sử dụng | Truyền dữ liệu, API                | File cấu hình                 |
| Tốc độ phân tích | Nhanh hơn                          | Chậm hơn chút                 |

---

## Ví dụ ứng dụng thực tế

### JSON: Dữ liệu người dùng

```json
{
  "id": "user_123",
  "name": "Trương Tam",
  "email": "zhang@example.com",
  "avatar": "https://example.com/avatar.jpg",
  "location": {
    "country": "Trung Quốc",
    "province": "Bắc Kinh",
    "city": "Bắc Kinh"
  },
  "birthday": "1990-01-15",
  "phone": "+86 138 0000 0000"
}
```

### YAML: Cấu hình ứng dụng

```yaml
# Cấu hình ứng dụng
app:
  name: "Blog Của Tôi"
  version: "1.0.0"
  port: 3000

# Cấu hình Database
database:
  host: "localhost"
  port: 5432
  name: "blog_db"
  user: "admin"
  password: "${DB_PASSWORD}" # Tham chiếu biến môi trường

# Công tắc tính năng
features:
  enable_comments: true
  enable_analytics: false
```

### JSON: Phản hồi API

```json
{
  "success": true,
  "data": {
    "posts": [
      {
        "id": "1",
        "title": "Bài viết đầu tiên",
        "author": "Trương Tam"
      },
      {
        "id": "2",
        "title": "Bài viết thứ hai",
        "author": "Lý Tứ"
      }
    ],
    "total": 2,
    "page": 1
  }
}
```

### YAML: Cấu hình CI/CD

```yaml
# Cấu hình GitHub Actions
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Cài đặt dependency
        run: pnpm install
      - name: Build
        run: pnpm build
      - name: Deploy
        run: pnpm deploy
```

---

## Sử dụng trong phát triển

### package.json (JSON)

File cấu hình của dự án Node.js, định nghĩa dependency và script của dự án:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.0.0"
  }
}
```

### tsconfig.json (JSON)

File cấu hình TypeScript:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "jsx": "preserve",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

---

## Câu hỏi thường gặp

### Q1: Muốn viết chú thích trong JSON thì làm thế nào?

Chuẩn JSON không hỗ trợ chú thích. Nếu cần chú thích, có thể dùng JSONC (JSON with Comments) hoặc chuyển sang dùng YAML.

### Q2: Thụt đầu dòng trong YAML dùng dấu cách (Space) hay Tab?

Bắt buộc dùng dấu cách, không được dùng Tab. Thường dùng 2 dấu cách cho một cấp thụt đầu dòng.

### Q3: Chọn JSON hay YAML khi nào?

- Truyền dữ liệu, phản hồi API: Dùng JSON
- File cấu hình: Ưu tiên YAML
- Cần viết chú thích: Dùng YAML
- Web API: Dùng JSON

### Q4: Viết sai định dạng thì sao?

Đa số trình soạn thảo code đều có chức năng kiểm tra cú pháp. Nhờ AI sửa giúp cũng là một cách hay, nó sẽ chỉ ra lỗi cụ thể và đưa ra định dạng đúng.

---

## Trọng điểm cốt lõi

- ✅ JSON và YAML là định dạng chuẩn của dữ liệu cấu trúc hóa
- ✅ JSON là định dạng dữ liệu chung cho Web API
- ✅ YAML thích hợp hơn để viết file cấu hình
- ✅ Định dạng cấu trúc hóa giúp AI hiểu nhu cầu chính xác hơn
- ✅ JSON dùng ngoặc và dấu phẩy, YAML dùng thụt đầu dòng
- ✅ Chọn định dạng tùy thuộc vào ngữ cảnh sử dụng

Hiểu các định dạng cấu hình rồi, tiếp theo sẽ học cách áp dụng những kiến thức này vào thực tế —— tích hợp API bên ngoài.

---

## Nội dung liên quan

- Trước đó: [4.2 Mối quan hệ giữa PRD và Tài liệu kỹ thuật](./02-prd-and-tech-docs_vi.md)
- Trước đó: [4.5 Khái niệm tách biệt Frontend-Backend](./05-frontend-backend-separation_vi.md)
- Chi tiết: [4.7 Thực chiến tích hợp API](./07-api-integration_vi.md)
- Chi tiết: [4.8 Cấu trúc bản hướng dẫn dự án](./08-readme-structure_vi.md)
