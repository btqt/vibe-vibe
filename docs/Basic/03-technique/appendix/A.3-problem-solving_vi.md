---
title: "A.3 Mẫu giải quyết vấn đề"
---


![03-technique_appendix_A.3-problem-solving.png](../../../public/images/Basic/03-technique_appendix_A.3-problem-solving.png)
# A.3 Mẫu giải quyết vấn đề

Phần này cung cấp các mẫu Prompt để rà soát vấn đề và tìm kiếm sự trợ giúp, bao gồm các tình huống rà soát lỗi, lựa chọn kỹ thuật, giải thích khái niệm.

## Mẫu 1: Rà soát lỗi thời gian chạy (Runtime Error)

Thích hợp cho: Code báo lỗi, chương trình bị crash, console báo đỏ

```markdown
## Thông tin lỗi

Gặp lỗi sau khi chạy:

```
[Dán đầy đủ thông tin lỗi, bao gồm stack trace]
```

## Bối cảnh kích hoạt

**Các bước thao tác**:
1. [Bước 1 đã làm gì]
2. [Bước 2 đã làm gì]
3. [Sau đó thì báo lỗi]

**Tần suất kích hoạt**: [Luôn báo lỗi/Thỉnh thoảng báo lỗi/Báo lỗi trong điều kiện cụ thể]

## Code liên quan

Code mà lỗi trỏ tới:
```[Ngôn ngữ]
Code trong thông tin lỗi, và ngữ cảnh xung quanh]
```

## Thông tin môi trường

- Môi trường chạy: [Phiên bản trình duyệt/Phiên bản Node.js/Phiên bản Python]
- Phiên bản framework: [React 18/Vue 3/...]
- Hệ điều hành: [Windows/Mac/Linux]

## Phương pháp đã thử

1. [Đã thử 1]: Kết quả [Thành công/Thất bại/Giải quyết một phần]
2. [Đã thử 2]: Kết quả [Thành công/Thất bại/Giải quyết một phần]

## Hãy giúp tôi

1. Phân tích nguyên nhân gốc rễ của lỗi
2. Đưa ra phương án sửa chữa
3. Giải thích tại sao lại xuất hiện vấn đề này (để giúp tôi hiểu)
```

### Ví dụ điền mẫu

```markdown
## Thông tin lỗi

Gặp lỗi sau khi chạy:

```
TypeError: Cannot read properties of undefined (reading 'map')
    at TaskList (TaskList.tsx:15:23)
    at renderWithHooks (react-dom.development.js:14985:18)
    at mountIndeterminateComponent (react-dom.development.js:17811:13)
```

## Bối cảnh kích hoạt

**Các bước thao tác**:
1. Mở trang chủ ứng dụng
2. Báo lỗi ngay khi tải trang
3. Danh sách nhiệm vụ không hiển thị

**Tần suất kích hoạt**: Luôn báo lỗi mỗi lần refresh trang

## Code liên quan

Code mà lỗi trỏ tới:
```tsx
// TaskList.tsx
function TaskList({ tasks }) {
  return (
    <ul>
      {tasks.map(task => (          // Dòng 15
        <li key={task.id}>{task.title}</li>
      ))}
    </ul>
  );
}

// Gọi trong App.tsx
function App() {
  const [tasks, setTasks] = useState();  // Chú ý chỗ này
  
  return <TaskList tasks={tasks} />;
}
```

## Thông tin môi trường

- Môi trường chạy: Chrome 120
- Phiên bản framework: React 18.2.0 + TypeScript 5.0
- Hệ điều hành: Mac

## Phương pháp đã thử

1. Kiểm tra dữ liệu tasks: console.log thấy là undefined
2. Refresh trang: Vấn đề vẫn còn

## Hãy giúp tôi

1. Phân tích nguyên nhân gốc rễ của lỗi
2. Đưa ra phương án sửa chữa
3. Giải thích tại sao lại xuất hiện vấn đề này
```

## Mẫu 2: Phân tích lỗi logic

Thích hợp cho: Code chạy được nhưng kết quả sai

```markdown
## Mô tả vấn đề

Code chạy được, nhưng kết quả không như kỳ vọng.

**Hành vi kỳ vọng**: [Kết quả nên là gì]
**Hành vi thực tế**: [Kết quả thực tế là gì]

## Test case

| Đầu vào | Đầu ra kỳ vọng | Đầu ra thực tế | Đúng/Sai |
|-----|---------|---------|---------|
| [Đầu vào 1] | [Kỳ vọng 1] | [Thực tế 1] | ❌ |
| [Đầu vào 2] | [Kỳ vọng 2] | [Thực tế 2] | ❌ |
| [Đầu vào 3] | [Kỳ vọng 3] | [Thực tế 3] | ✅ |

## Code liên quan

```[Ngôn ngữ]
[Dán code liên quan]
```

## Phân tích của tôi

Tôi nghi ngờ vấn đề có thể nằm ở: [Dự đoán của bạn]

## Hãy giúp tôi

1. Tìm ra chỗ sai logic
2. Giải thích tại sao logic hiện tại lại sinh ra kết quả sai
3. Đưa ra code sau khi sửa
```

### Ví dụ điền mẫu

```markdown
## Mô tả vấn đề

Code chạy được, nhưng kết quả không như kỳ vọng.

**Hành vi kỳ vọng**: Khi tính tổng giá giỏ hàng, nếu trên 100 thì giảm 20
**Hành vi thực tế**: Bất kể số tiền bao nhiêu đều giảm 20

## Test case

| Đầu vào (Tổng giá hàng) | Đầu ra kỳ vọng | Đầu ra thực tế | Đúng/Sai |
|---------------|---------|---------|---------|
| 150 | 130 | 130 | ✅ |
| 80 | 80 | 60 | ❌ |
| 100 | 80 | 80 | ✅ |

## Code liên quan

```javascript
function calculateTotal(items) {
  let total = items.reduce((sum, item) => sum + item.price, 0);
  
  // Trên 100 giảm 20
  if (total > 100) {
    total = total - 20;
  } else {
    total = total - 20;  // Có thể vấn đề ở đây?
  }
  
  return total;
}
```

## Phân tích của tôi

Tôi nghi ngờ vấn đề có thể nằm ở: Nhánh else cũng giảm 20, chắc là lỗi copy paste quên xóa

## Hãy giúp tôi

1. Xác nhận phân tích của tôi có đúng không
2. Đưa ra code sau khi sửa
3. Gợi ý cách tránh lỗi copy paste kiểu này
```

## Mẫu 3: Tư vấn lựa chọn kỹ thuật

Thích hợp cho: Không biết chọn thư viện, framework, công cụ nào

```markdown
## Bối cảnh dự án

**Loại dự án**: [Tóm tắt dự án làm gì]
**Stack kỹ thuật**: [Công nghệ đang dùng]
**Tình hình team**: [Dự án cá nhân/Quy mô team/Trình độ kỹ thuật]

## Nhu cầu lựa chọn

Tôi cần chọn một [Loại] để thực hiện [Chức năng].

**Nhu cầu cốt lõi**:
- [Nhu cầu 1]
- [Nhu cầu 2]
- [Nhu cầu 3]

**Yếu tố cân nhắc**:
| Yếu tố | Mức độ quan trọng | Giải thích |
|-----|---------|------|
| Chi phí học tập | Cao/Trung bình/Thấp | [Giải thích] |
| Độ sôi động cộng đồng | Cao/Trung bình/Thấp | [Giải thích] |
| Hiệu năng | Cao/Trung bình/Thấp | [Giải thích] |
| Dung lượng gói | Cao/Trung bình/Thấp | [Giải thích] |
| Bảo trì lâu dài | Cao/Trung bình/Thấp | [Giải thích] |

## Ứng viên đã biết (Tùy chọn)

Tôi hiện biết các lựa chọn sau:
1. [Lựa chọn A]: [Ấn tượng đơn giản]
2. [Lựa chọn B]: [Ấn tượng đơn giản]
3. [Lựa chọn C]: [Ấn tượng đơn giản]

## Hãy giúp tôi

1. Bổ sung phương án ứng viên tôi có thể bỏ sót
2. So sánh ưu nhược điểm các phương án từ nhiều chiều
3. Đưa ra phương án đề xuất và lý do
4. Giải thích trường hợp nào nên chọn phương án khác
```

### Ví dụ điền mẫu

```markdown
## Bối cảnh dự án

**Loại dự án**: Website blog cá nhân
**Stack kỹ thuật**: Next.js + TypeScript
**Tình hình team**: Dự án cá nhân, frontend thạo, backend mới học

## Nhu cầu lựa chọn

Tôi cần chọn một phương án cơ sở dữ liệu để lưu trữ bài viết blog.

**Nhu cầu cốt lõi**:
- Lưu nội dung bài viết (định dạng Markdown)
- Hỗ trợ phân loại và gắn thẻ
- Có thể truy vấn sắp xếp theo thời gian

**Yếu tố cân nhắc**:
| Yếu tố | Mức độ quan trọng | Giải thích |
|-----|---------|------|
| Chi phí học tập | Cao | Backend không thạo, muốn dễ tiếp cận |
| Hạn ngạch miễn phí | Cao | Dự án cá nhân, không muốn tốn tiền |
| Tích hợp với Next.js | Trung bình | Hy vọng có hướng dẫn sẵn |
| Hiệu năng | Thấp | Lượng truy cập blog không lớn |

## Ứng viên đã biết

Tôi hiện biết các lựa chọn sau:
1. Supabase: Nghe nói thay thế được Firebase
2. MongoDB Atlas: Cơ sở dữ liệu NoSQL
3. PlanetScale: Dịch vụ đám mây MySQL

## Hãy giúp tôi

1. Bổ sung phương án ứng viên tôi có thể bỏ sót
2. So sánh ưu nhược điểm các phương án từ nhiều chiều
3. Đưa ra phương án đề xuất và lý do
4. Giải thích trường hợp nào nên chọn phương án khác
```

## Mẫu 4: Giải thích khái niệm

Thích hợp cho: Không hiểu khái niệm kỹ thuật nào đó

```markdown
## Khái niệm muốn tìm hiểu

Tôi muốn hiểu [Tên khái niệm].

## Thắc mắc hiện tại

**Cách hiểu hiện tại của tôi**: [Bạn đang nghĩ nó là gì]
**Chỗ thắc mắc**: [Không hiểu chỗ nào]

## Cách giải thích mong muốn

**Độ sâu kỹ thuật**: [Chỉ cần biết dùng thế nào/Muốn hiểu nguyên lý/Cần đi sâu chi tiết]
**Sở thích loại so sánh**: [Thích so sánh đời sống/Thích so sánh kỹ thuật/Giải thích trực tiếp là được]

## Bối cảnh liên quan

**Nền tảng kỹ thuật của tôi**: [Thạo công nghệ/ngôn ngữ nào]
**Tại sao cần tìm hiểu cái này**: [Ngữ cảnh ứng dụng]

## Hãy giúp tôi

1. Giải thích khái niệm này bằng ngôn ngữ dễ hiểu
2. Đưa ra một ví dụ code đơn giản
3. Giải thích khi nào thì dùng đến nó
4. Chỉ ra các hiểu lầm thường gặp
```

### Ví dụ điền mẫu

```markdown
## Khái niệm muốn tìm hiểu

Tôi muốn hiểu useEffect trong React.

## Thắc mắc hiện tại

**Cách hiểu hiện tại của tôi**: Hình như dùng để xử lý "tác dụng phụ" (side effect), nhưng không biết gì được tính là tác dụng phụ
**Chỗ thắc mắc**:
- Khi nào cần dùng useEffect?
- Mảng dependency dùng làm gì?
- Tại sao thỉnh thoảng lại bị "vòng lặp vô hạn"?

## Cách giải thích mong muốn

**Độ sâu kỹ thuật**: Chỉ cần biết dùng thế nào là được, nguyên lý tính sau
**Sở thích loại so sánh**: Thích so sánh đời sống

## Bối cảnh liên quan

**Nền tảng kỹ thuật của tôi**: Biết JavaScript cơ bản, đang học React
**Tại sao cần tìm hiểu cái này**: Muốn lấy dữ liệu khi component load

## Hãy giúp tôi

1. Giải thích useEffect bằng ngôn ngữ dễ hiểu
2. Đưa ra ví dụ code "lấy dữ liệu"
3. Giải thích tác dụng của mảng dependency
4. Giải thích tại sao lại bị "vòng lặp vô hạn" và cách tránh
```

## Mẫu 5: Review code

Thích hợp cho: Nhờ AI kiểm tra chất lượng code

```markdown
## Mục tiêu review

Hãy giúp tôi review đoạn code sau:

```[Ngôn ngữ]
[Dán code]
```

## Khía cạnh review

Vui lòng kiểm tra theo các khía cạnh sau:

- [ ] **Tính chính xác chức năng**: Logic có đúng không, các trường hợp biên có xử lý không
- [ ] **Bảo mật**: Có lỗ hổng bảo mật nào không (XSS, SQL Injection,...)
- [ ] **Hiệu năng**: Có vấn đề hiệu năng rõ ràng nào không
- [ ] **Khả năng đọc**: Đặt tên có rõ ràng không, cấu trúc có hợp lý không
- [ ] **Khả năng bảo trì**: Có dễ mở rộng và sửa đổi không
- [ ] **Xử lý lỗi**: Các tình huống bất thường có được xử lý thỏa đáng không

## Bối cảnh code

**Tác dụng của đoạn code này**: [Tóm tắt chức năng]
**Ngữ cảnh sử dụng**: [Chạy trong tình huống nào]

## Định dạng đầu ra

Vui lòng xuất theo định dạng sau:

1. **Danh sách vấn đề**: Liệt kê các vấn đề phát hiện, sắp xếp theo mức độ nghiêm trọng
2. **Gợi ý cải tiến**: Đưa ra gợi ý cụ thể cho từng vấn đề
3. **Code sau tối ưu**: Đưa ra code hoàn chỉnh sau khi cải tiến
```

## Bản rút gọn: Mẫu đặt câu hỏi nhanh

Khi vấn đề khá đơn giản, có thể dùng bản rút gọn này:

```markdown
**Vấn đề**: [Một câu mô tả vấn đề]

**Bối cảnh**: [Ngữ cảnh cần thiết]

**Code**:
```[Ngôn ngữ]
Code liên quan]
```

**Kỳ vọng**: [Bạn mong nhận được sự giúp đỡ gì]
```

## Kỹ năng đặt câu hỏi: Làm thế nào để câu trả lời hữu ích hơn

### Kỹ năng 1: Nói kết luận trước, rồi mới đưa chi tiết

```markdown
❌ Tôi có một dự án React, dùng TypeScript, rồi tôi đang làm một cái xác thực form...
   (AI đọc nửa ngày vẫn chưa biết vấn đề là gì)

✅ Code xác thực form của tôi báo lỗi.
   Stack kỹ thuật là React + TypeScript, thông tin lỗi là [xxx].
```

### Kỹ năng 2: Đưa ra code tái hiện tối thiểu

Đừng dán cả file, chỉ dán **dòng code tối thiểu có thể tái hiện vấn đề**. Như vậy AI dễ định vị vấn đề hơn.

### Kỹ năng 3: Nói rõ đã thử những gì

Điều này giúp AI tránh đưa ra phương án vô dụng mà bạn đã thử rồi.

## Sai lầm thường gặp khi điền

| Sai lầm | Vấn đề | Cách làm đúng |
|-----|------|---------|
| Chỉ nói "không chạy được" | AI không biết triệu chứng cụ thể | Mô tả sai lệch giữa kỳ vọng vs thực tế |
| Thông tin lỗi cắt một nửa | Mất thông tin then chốt | Dán đầy đủ, bao gồm stack trace |
| Không đưa code | AI chỉ có thể đoán mò | Dán đoạn code liên quan |
| Vấn đề khái niệm quá rộng | "Giải thích JavaScript chút" | Cụ thể vào điểm nào đó, như "Giải thích closure" |

## Điểm cốt yếu phần này

- ✅ **Rà soát lỗi**: Thông tin lỗi đầy đủ + Các bước kích hoạt + Code liên quan + Phương pháp đã thử
- ✅ **Lỗi logic**: Dùng test case thể hiện "Kỳ vọng vs Thực tế"
- ✅ **Lựa chọn kỹ thuật**: Làm rõ ưu tiên nhu cầu + Liệt kê các yếu tố cân nhắc
- ✅ **Giải thích khái niệm**: Nói rõ cách hiểu hiện tại và điểm thắc mắc + Độ sâu giải thích mong muốn
