---
title: "A.4 Mẫu tạo tài liệu"
---


![03-technique_appendix_A.4-document-generation.png](../../../public/images/Basic/03-technique_appendix_A.4-document-generation.png)
# A.4 Mẫu tạo tài liệu

Phần này cung cấp các mẫu Prompt để tạo các loại tài liệu, bao gồm chú thích code, README, tài liệu API và hướng dẫn sử dụng.

## Mẫu 1: Tạo chú thích code

Thích hợp cho: Thêm chú thích cho code hiện có

```markdown
## Nhu cầu chú thích

Vui lòng thêm chú thích bằng tiếng Việt cho đoạn code sau:

```[Ngôn ngữ]
[Dán code]
```

## Yêu cầu chú thích

**Loại chú thích**:
- [ ] Chú thích đầu file (giải thích công dụng file)
- [ ] Chú thích hàm (giải thích tham số, giá trị trả về, chức năng)
- [ ] Chú thích logic then chốt (giải thích logic phức tạp)
- [ ] Chú thích TODO (đánh dấu chỗ cần hoàn thiện)

**Phong cách chú thích**:
- Ngôn ngữ: Tiếng Việt
- Định dạng: [Phong cách JSDoc / Chú thích thường / Quy chuẩn của bạn]
- Độ chi tiết: [Ngắn gọn/Vừa phải/Chi tiết]

**Lưu ý đặc biệt**:
- [Yêu cầu khác, ví dụ "không cần chú thích biến đơn giản"]

## Yêu cầu đầu ra

Vui lòng xuất code hoàn chỉnh sau khi thêm chú thích, giữ nguyên logic code ban đầu.
```

### Ví dụ điền mẫu

```markdown
## Nhu cầu chú thích

Vui lòng thêm chú thích bằng tiếng Việt cho đoạn code sau:

```typescript
interface Task {
  id: string;
  title: string;
  completed: boolean;
  createdAt: Date;
}

function useTasks() {
  const [tasks, setTasks] = useState<Task[]>([]);
  
  const addTask = useCallback((title: string) => {
    const newTask: Task = {
      id: crypto.randomUUID(),
      title,
      completed: false,
      createdAt: new Date(),
    };
    setTasks(prev => [...prev, newTask]);
  }, []);
  
  const toggleTask = useCallback((id: string) => {
    setTasks(prev => 
      prev.map(task => 
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  }, []);
  
  return { tasks, addTask, toggleTask };
}
```

## Yêu cầu chú thích

**Loại chú thích**:
- [x] Chú thích đầu file
- [x] Chú thích hàm (định dạng JSDoc)
- [x] Chú thích logic then chốt

**Phong cách chú thích**:
- Ngôn ngữ: Tiếng Việt
- Định dạng: Phong cách JSDoc
- Độ chi tiết: Vừa phải

**Lưu ý đặc biệt**:
- Mỗi trường trong interface cần có chú thích
- useCallback cần giải thích tại sao dùng nó

## Yêu cầu đầu ra

Vui lòng xuất code hoàn chỉnh sau khi thêm chú thích.
```

## Mẫu 2: Tạo README

Thích hợp cho: Tạo tài liệu hướng dẫn cho dự án

```markdown
## Thông tin dự án

**Tên dự án**: [Tên]
**Mô tả một câu**: [Tóm tắt dự án làm gì]

**Stack kỹ thuật**:
- Frontend: [Công nghệ]
- Backend: [Công nghệ, nếu không có thì ghi "Không"]
- Cơ sở dữ liệu: [Công nghệ, nếu không có thì ghi "Không"]

**Người dùng mục tiêu**: [Ai sẽ dùng dự án này]

## Chức năng dự án

**Chức năng cốt lõi**:
1. [Chức năng 1]
2. [Chức năng 2]
3. [Chức năng 3]

**Ảnh chụp màn hình chức năng** (Tùy chọn):
[Nếu có ảnh chụp màn hình, mô tả nội dung ảnh]

## Chi tiết kỹ thuật

**Cấu trúc dự án**:
```
[Dán cấu trúc thư mục dự án]
```

**Yêu cầu môi trường**:
- Phiên bản Node.js: [Phiên bản]
- Phụ thuộc khác: [Liệt kê]

**Các bước cài đặt**:
[Nếu bạn biết các bước cài đặt, có thể viết ra trước]

## Yêu cầu README

**Nội dung bao gồm**:
- [ ] Giới thiệu dự án
- [ ] Đặc điểm tính năng
- [ ] Bắt đầu nhanh (Cài đặt và chạy)
- [ ] Giải thích cấu trúc dự án
- [ ] Giải thích Stack kỹ thuật
- [ ] Hướng dẫn đóng góp
- [ ] License

**Yêu cầu phong cách**:
- Ngôn ngữ: Tiếng Việt
- Phong cách: [Ngắn gọn chuyên nghiệp/Thân thiện gần gũi/Đậm chất kỹ thuật]

## Yêu cầu đầu ra

Vui lòng tạo nội dung file README.md hoàn chỉnh.
```

### Ví dụ điền mẫu

```markdown
## Thông tin dự án

**Tên dự án**: Minimal Todo
**Mô tả một câu**: Một danh sách việc cần làm cực giản, mở trình duyệt là dùng ngay

**Stack kỹ thuật**:
- Frontend: React + TypeScript + Tailwind CSS
- Backend: Không
- Cơ sở dữ liệu: localStorage trình duyệt

**Người dùng mục tiêu**: Người dùng cá nhân muốn ghi lại việc cần làm hàng ngày một cách đơn giản

## Chức năng dự án

**Chức năng cốt lõi**:
1. Thêm việc cần làm
2. Đánh dấu hoàn thành
3. Xóa việc cần làm
4. Bền vững hóa dữ liệu cục bộ

## Chi tiết kỹ thuật

**Cấu trúc dự án**:
```
src/
├── components/
│   ├── AddTask.tsx
│   ├── TaskList.tsx
│   └── TaskItem.tsx
├── hooks/
│   └── useTasks.ts
├── types/
│   └── index.ts
├── App.tsx
└── main.tsx
```

**Yêu cầu môi trường**:
- Phiên bản Node.js: 18+
- Trình quản lý gói: npm hoặc pnpm

## Yêu cầu README

**Nội dung bao gồm**:
- [x] Giới thiệu dự án
- [x] Đặc điểm tính năng
- [x] Bắt đầu nhanh
- [x] Giải thích cấu trúc dự án
- [ ] Hướng dẫn đóng góp (Không cần)
- [ ] License (Không cần)

**Yêu cầu phong cách**:
- Ngôn ngữ: Tiếng Việt
- Phong cách: Ngắn gọn chuyên nghiệp

## Yêu cầu đầu ra

Vui lòng tạo nội dung file README.md hoàn chỉnh.
```

## Mẫu 3: Tạo tài liệu API

Thích hợp cho: Tạo tài liệu cho interface backend

```markdown
## Thông tin cơ bản API

**Tên API**: [Tên interface]
**Đường dẫn request**: [Ví dụ /api/users]
**Phương thức request**: [GET/POST/PUT/DELETE]
**Mô tả chức năng**: [Interface này làm gì]

## Code interface

```[Ngôn ngữ]
[Dán code cài đặt interface]
```

## Yêu cầu tài liệu

**Định dạng tài liệu**: [Markdown / OpenAPI YAML / Khác]

**Nội dung bao gồm**:
- [ ] Mô tả interface
- [ ] Giải thích tham số request
- [ ] Ví dụ body request
- [ ] Giải thích định dạng phản hồi
- [ ] Ví dụ phản hồi
- [ ] Giải thích mã lỗi
- [ ] Ví dụ gọi (curl/JavaScript)

## Yêu cầu đầu ra

Vui lòng tạo tài liệu API hoàn chỉnh.
```

### Ví dụ điền mẫu

```markdown
## Thông tin cơ bản API

**Tên API**: Tạo nhiệm vụ
**Đường dẫn request**: /api/tasks
**Phương thức request**: POST
**Mô tả chức năng**: Tạo một nhiệm vụ cần làm mới

## Code interface

```typescript
// POST /api/tasks
export async function POST(request: Request) {
  const body = await request.json();
  const { title, priority } = body;
  
  if (!title || title.trim() === '') {
    return Response.json(
      { error: 'Title is required' },
      { status: 400 }
    );
  }
  
  const task = {
    id: crypto.randomUUID(),
    title: title.trim(),
    priority: priority || 'medium',
    completed: false,
    createdAt: new Date().toISOString(),
  };
  
  // Lưu vào database...
  await db.tasks.create(task);
  
  return Response.json(task, { status: 201 });
}
```

## Yêu cầu tài liệu

**Định dạng tài liệu**: Markdown

**Nội dung bao gồm**:
- [x] Mô tả interface
- [x] Giải thích tham số request
- [x] Ví dụ body request
- [x] Giải thích định dạng phản hồi
- [x] Ví dụ phản hồi
- [x] Giải thích mã lỗi
- [x] Ví dụ gọi (curl)

## Yêu cầu đầu ra

Vui lòng tạo tài liệu API hoàn chỉnh.
```

## Mẫu 4: Tạo hướng dẫn sử dụng

Thích hợp cho: Viết hướng dẫn sử dụng cho người dùng không chuyên kỹ thuật

```markdown
## Thông tin sản phẩm

**Tên sản phẩm**: [Tên]
**Loại sản phẩm**: [Trang web/App/Phần mềm desktop/Script]
**Người dùng mục tiêu**: [Ai dùng, trình độ kỹ thuật thế nào]

## Chức năng cốt lõi

Vui lòng viết hướng dẫn sử dụng cho các chức năng sau:

1. **[Chức năng 1]**
   - Mô tả chức năng: [Làm gì]
   - Vị trí truy cập: [Tìm chức năng này ở đâu]
   
2. **[Chức năng 2]**
   - Mô tả chức năng: [Làm gì]
   - Vị trí truy cập: [Tìm chức năng này ở đâu]

## Yêu cầu hướng dẫn

**Phong cách ngôn ngữ**:
- Giọng điệu: [Trang trọng/Thân thiện/Ngắn gọn]
- Thuật ngữ kỹ thuật: [Tránh sử dụng/Giải thích đơn giản rồi dùng]

**Cấu trúc nội dung**:
- [ ] Giới thiệu chức năng
- [ ] Các bước thao tác (giải thích từng bước)
- [ ] Lưu ý
- [ ] Vấn đề thường gặp

**Giải thích phối ảnh** (Tùy chọn):
[Mô tả cần phối ảnh gì, hoặc ghi chú "Không cần phối ảnh"]

## Yêu cầu đầu ra

Vui lòng tạo tài liệu hướng dẫn sử dụng thân thiện với người dùng.
```

## Mẫu 5: Tổng hợp ghi chép học tập

Thích hợp cho: Tổng hợp nội dung học tập kỹ thuật

```markdown
## Chủ đề học tập

Tôi đã học về [Chủ đề], vui lòng giúp tôi tổng hợp ghi chép.

## Nội dung học tập

Sau đây là những ghi chép rời rạc tôi ghi lại trong quá trình học:

```
[Dán ghi chép học tập, đoạn code, từ khóa... của bạn]
```

## Yêu cầu tổng hợp

**Cấu trúc ghi chép**:
- [ ] Định nghĩa khái niệm
- [ ] Điểm cốt lõi (3-5 điểm)
- [ ] Ví dụ code
- [ ] Tình huống sử dụng
- [ ] Hiểu lầm thường gặp
- [ ] Link khái niệm liên quan

**Sở thích định dạng**:
- Sử dụng Markdown
- Khối code có highlight cú pháp
- Điểm trọng tâm in đậm

## Yêu cầu đầu ra

Vui lòng xuất ghi chép học tập có cấu trúc, thuận tiện cho việc ôn tập sau này.
```

### Ví dụ điền mẫu

```markdown
## Chủ đề học tập

Tôi đã học về useEffect trong React Hooks, vui lòng giúp tôi tổng hợp ghi chép.

## Nội dung học tập

Sau đây là những ghi chép rời rạc tôi ghi lại trong quá trình học:

```
useEffect tác dụng phụ
- Lấy dữ liệu
- Đăng ký sự kiện
- Sửa DOM

Mảng dependency
[] mảng rỗng - chỉ thực thi một lần khi mount
Không viết - thực thi mỗi lần render
[dep1, dep2] - thực thi khi dependency thay đổi

Hàm cleanup return () => {}
Gọi khi component unmount
Tránh rò rỉ bộ nhớ

Lỗi thường gặp:
Vòng lặp vô hạn - mảng dependency viết sai
Rò rỉ bộ nhớ - quên dọn dẹp đăng ký
```

## Yêu cầu tổng hợp

**Cấu trúc ghi chép**:
- [x] Định nghĩa khái niệm
- [x] Điểm cốt lõi
- [x] Ví dụ code
- [x] Tình huống sử dụng
- [x] Hiểu lầm thường gặp

**Sở thích định dạng**:
- Sử dụng Markdown
- Khối code có highlight cú pháp
- Điểm trọng tâm in đậm

## Yêu cầu đầu ra

Vui lòng xuất ghi chép học tập có cấu trúc.
```

## Bản rút gọn: Tạo tài liệu nhanh

Khi nhu cầu đơn giản, có thể dùng bản rút gọn này:

```markdown
Vui lòng tạo [Chú thích/Tài liệu/Giải thích] cho code sau:

```[Ngôn ngữ]
[Code]
```

Yêu cầu:
- Ngôn ngữ: Tiếng Việt
- Định dạng: [Markdown/JSDoc/Khác]
- [Yêu cầu khác]
```

## Kỹ năng tạo tài liệu

### Kỹ năng 1: Cung cấp đủ ngữ cảnh

AI cần hiểu công dụng của code mới viết được tài liệu tốt. Giải thích đơn giản đoạn code này "làm gì" sẽ giúp tài liệu chính xác hơn.

### Kỹ năng 2: Chỉ định độc giả mục tiêu

Tài liệu cho developer xem và hướng dẫn cho người dùng phổ thông xem có cách viết hoàn toàn khác nhau. Xác định rõ người đọc là ai.

### Kỹ năng 3: Đưa ra ví dụ định dạng

Nếu bạn có yêu cầu định dạng tài liệu cụ thể, đưa ra một ví dụ sẽ hiệu quả hơn là dùng lời mô tả.

## Sai lầm thường gặp khi điền

| Sai lầm | Vấn đề | Cách làm đúng |
|-----|------|---------|
| Không giải thích công dụng | AI không hiểu code làm gì | Giải thích tóm tắt chức năng và tình huống |
| Không chỉ định định dạng | Định dạng đầu ra ngẫu nhiên | Xác định rõ cần Markdown/JSDoc... |
| Không chỉ định ngôn ngữ | Có thể xuất ra tiếng Anh | Yêu cầu rõ tiếng Việt |
| Yêu cầu quá chung chung | "Viết cái tài liệu" | Nói cụ thể bao gồm những nội dung gì |

## Điểm cốt yếu phần này

- ✅ **Chú thích code**: Chỉ định loại chú thích + Phong cách + Độ chi tiết
- ✅ **README**: Cung cấp thông tin dự án + Danh sách chức năng + Chi tiết kỹ thuật
- ✅ **Tài liệu API**: Cung cấp code interface + Chỉ định định dạng tài liệu
- ✅ **Hướng dẫn sử dụng**: Xác định người dùng mục tiêu + Chỉ định phong cách ngôn ngữ
- ✅ **Kỹ thuật then chốt**: Cung cấp ngữ cảnh + Chỉ định độc giả mục tiêu + Đưa ra ví dụ định dạng
