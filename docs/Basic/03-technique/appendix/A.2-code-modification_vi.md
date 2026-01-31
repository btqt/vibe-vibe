---
title: "A.2 Mẫu sửa đổi code"
---


![03-technique_appendix_A.2-code-modification.png](../../../public/images/Basic/03-technique_appendix_A.2-code-modification.png)
# A.2 Mẫu sửa đổi code

Phần này cung cấp các mẫu Prompt để sửa đổi code hiện có, bao gồm mở rộng chức năng, tái cấu trúc code, tối ưu hóa hiệu năng và điều chỉnh style.

## Mẫu 1: Mở rộng chức năng

Thích hợp cho: Thêm chức năng mới trên nền tảng code hiện có

```markdown
## Trạng thái hiện tại

**Bối cảnh dự án**: [Tóm tắt dự án làm gì]
**Stack kỹ thuật**: [Công nghệ sử dụng]
**Module cần mở rộng**: [File/Component nào]

## Code hiện tại

```[Ngôn ngữ]
[Dán code hiện tại]
```

## Nhu cầu mở rộng

**Chức năng mới**: [Mô tả cần thêm chức năng gì]

**Chi tiết chức năng**:
- [Chi tiết 1]
- [Chi tiết 2]
- [Chi tiết 3]

**Cách kích hoạt**: [Người dùng kích hoạt chức năng này như thế nào]
**Kết quả kỳ vọng**: [Sau khi chức năng thực thi thì chuyện gì xảy ra]

## Điều kiện ràng buộc

**Phải giữ nguyên**:
- [Chức năng A hiện có không được bị ảnh hưởng]
- [Chức năng B hiện có phải tiếp tục hoạt động bình thường]

**Không được sửa**:
- [Phần 1 không được sửa]
- [Phần 2 không được sửa]

## Yêu cầu đầu ra

- [ ] Chỉ xuất code sau khi sửa, không cần lặp lại phần không sửa
- [ ] Dùng chú thích đánh dấu code mới thêm
- [ ] Giải thích các thư viện phụ thuộc cần cài thêm (nếu có)
```

### Ví dụ điền mẫu: Thêm chức năng "Hoàn tác xóa" cho danh sách việc cần làm

```markdown
## Trạng thái hiện tại

**Bối cảnh dự án**: Ứng dụng web danh sách việc cần làm cá nhân
**Stack kỹ thuật**: React + TypeScript + Tailwind CSS
**Module cần mở rộng**: Component TaskList.tsx

## Code hiện tại

```tsx
function TaskList({ tasks, onDelete }) {
  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>
          {task.content}
          <button onClick={() => onDelete(task.id)}>Xóa</button>
        </li>
      ))}
    </ul>
  );
}
```

## Nhu cầu mở rộng

**Chức năng mới**: Sau khi xóa nhiệm vụ hiển thị nhắc nhở "Hoàn tác", có thể khôi phục trong vòng 3 giây

**Chi tiết chức năng**:
- Sau khi xóa nhiệm vụ, dưới đáy hiển thị nhắc nhở "Đã xóa, nhấn để hoàn tác"
- Nhắc nhở hiển thị 3 giây rồi tự biến mất
- Nhấn nút "Hoàn tác", nhiệm vụ khôi phục về vị trí cũ
- Cùng lúc chỉ có một nhắc nhở hoàn tác

**Cách kích hoạt**: Người dùng nhấn nút xóa
**Kết quả kỳ vọng**: Nhiệm vụ biến mất khỏi danh sách, dưới đáy xuất hiện nhắc nhở hoàn tác

## Điều kiện ràng buộc

**Phải giữ nguyên**:
- Logic hiển thị nhiệm vụ hiện tại không đổi
- Vị trí và style của nút xóa không đổi

**Không được sửa**:
- Không thay đổi định nghĩa kiểu props
- Không giới thiệu thư viện quản lý trạng thái mới

## Yêu cầu đầu ra

- [x] Chỉ xuất code sau khi sửa
- [x] Dùng chú thích đánh dấu code mới thêm
- [ ] Giải thích các thư viện phụ thuộc cần cài thêm
```

## Mẫu 2: Tái cấu trúc code

Thích hợp cho: Cải thiện chất lượng code, nâng cao khả năng đọc, thống nhất phong cách code

```markdown
## Mục tiêu tái cấu trúc

**Vấn đề hiện tại**: [Code hiện tại có vấn đề gì]
**Cải tiến kỳ vọng**: [Sau khi tái cấu trúc hy vọng đạt hiệu quả gì]

## Code chờ tái cấu trúc

```[Ngôn ngữ]
[Dán code cần tái cấu trúc]
```

## Yêu cầu tái cấu trúc

**Hướng đi**: [Có thể chọn nhiều]
- [ ] Nâng cao khả năng đọc (đặt tên biến, tách hàm)
- [ ] Giảm code lặp (tách hàm chung)
- [ ] Thống nhất phong cách code
- [ ] Thêm định nghĩa kiểu (TypeScript)
- [ ] Cải thiện xử lý lỗi
- [ ] Khác: [Giải thích cụ thể]

**Phải giữ nguyên**:
- Hành vi chức năng hoàn toàn không đổi
- [Ràng buộc khác]

**Quy chuẩn tham khảo** (Tùy chọn):
[Nếu có quy chuẩn code cụ thể, có thể dán vào đây]

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Code hoàn chỉnh sau khi tái cấu trúc
2. Giải thích tóm tắt đã sửa những gì
3. Lý do sửa đổi
```

### Ví dụ điền mẫu: Tái cấu trúc code xác thực form bị lặp

```markdown
## Mục tiêu tái cấu trúc

**Vấn đề hiện tại**: Ba form đăng ký, đăng nhập, đổi mật khẩu đều có code xác thực tương tự nhau, copy paste 3 lần
**Cải tiến kỳ vọng**: Tách hàm xác thực chung, giảm lặp lại

## Code chờ tái cấu trúc

```typescript
// Form đăng ký
function validateRegister(data) {
  if (!data.email || !data.email.includes('@')) {
    return 'Định dạng email không đúng';
  }
  if (!data.password || data.password.length < 8) {
    return 'Mật khẩu ít nhất 8 ký tự';
  }
  if (data.password !== data.confirmPassword) {
    return 'Mật khẩu hai lần nhập không khớp';
  }
  return null;
}

// Form đăng nhập
function validateLogin(data) {
  if (!data.email || !data.email.includes('@')) {
    return 'Định dạng email không đúng';
  }
  if (!data.password || data.password.length < 8) {
    return 'Mật khẩu ít nhất 8 ký tự';
  }
  return null;
}

// Form đổi mật khẩu
function validateChangePassword(data) {
  if (!data.oldPassword || data.oldPassword.length < 8) {
    return 'Mật khẩu cũ ít nhất 8 ký tự';
  }
  if (!data.newPassword || data.newPassword.length < 8) {
    return 'Mật khẩu mới ít nhất 8 ký tự';
  }
  if (data.newPassword !== data.confirmPassword) {
    return 'Mật khẩu hai lần nhập không khớp';
  }
  return null;
}
```

## Yêu cầu tái cấu trúc

**Hướng đi**:
- [x] Giảm code lặp (tách hàm chung)
- [x] Thêm định nghĩa kiểu (TypeScript)
- [x] Cải thiện xử lý lỗi (hỗ trợ trả về nhiều lỗi)

**Phải giữ nguyên**:
- Hành vi chức năng hoàn toàn không đổi
- Văn bản thông báo lỗi giữ nguyên

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Code hoàn chỉnh sau khi tái cấu trúc
2. Giải thích tóm tắt đã sửa những gì
3. Cách sử dụng hàm xác thực mới trong các form cũ
```

## Mẫu 3: Tối ưu hóa hiệu năng

Thích hợp cho: Trang tải chậm, thao tác giật lag, chiếm dụng bộ nhớ cao

```markdown
## Mô tả vấn đề hiệu năng

**Hiện tượng vấn đề**: [Mô tả cụ thể chậm ở đâu, lag ở đâu]
**Điều kiện kích hoạt**: [Tình huống nào thì xuất hiện vấn đề này]
**Mức độ ảnh hưởng**: [Trễ khoảng bao lâu, lag bao lâu]

## Code liên quan

```[Ngôn ngữ]
[Dán code có thể gây ra vấn đề hiệu năng]
```

## Mục tiêu tối ưu

**Hiệu quả kỳ vọng**: [Sau tối ưu nên đạt mức độ nào]
**Tiêu chuẩn đo lường**: [Làm sao phán đoán tối ưu thành công]

## Thông tin đã biết

**Quy mô dữ liệu**: [Lượng dữ liệu xử lý khoảng bao nhiêu]
**Môi trường chạy**: [Trình duyệt/Node.js/Mobile]
**Đã thử tối ưu**: [Nếu có]

## Điều kiện ràng buộc

- Logic chức năng không được thay đổi
- [Ràng buộc khác]

## Yêu cầu đầu ra

Vui lòng cung cấp:
1. Code sau khi tối ưu
2. Giải thích nguyên nhân vấn đề hiệu năng
3. Nguyên lý tối ưu và dự đoán hiệu quả
```

## Mẫu 4: Điều chỉnh Style

Thích hợp cho: Làm đẹp UI, sửa bố cục, thích ứng Responsive

```markdown
## Style hiện tại

**Mô tả vấn đề**: [Giao diện hiện tại chỗ nào chưa ưng ý]

**Code hiện tại**:
```[css/html]
[Dán code style liên quan hiện tại]
```

## Hiệu quả kỳ vọng

**Mô tả**: [Dùng lời văn mô tả hiệu quả mong muốn]

**Tham khảo** (Tùy chọn):
- Website tham khảo: [URL]
- Ảnh tham khảo: [Mô tả hoặc link]
- Từ khóa: [Tối giản/Hiện đại/Bo tròn/Đổ bóng/Gradient/...]

## Yêu cầu cụ thể

**Điều chỉnh bố cục**:
- [Điều chỉnh 1]
- [Điều chỉnh 2]

**Hiệu quả thị giác**:
- [Hiệu quả 1]
- [Hiệu quả 2]

**Responsive**:
- Desktop (>1024px): [Yêu cầu]
- Tablet (768-1024px): [Yêu cầu]
- Mobile (<768px): [Yêu cầu]

## Ràng buộc kỹ thuật

**Công nghệ sử dụng**: [Tailwind CSS/CSS thuần/Khác]
**Phải tương thích**: [Yêu cầu phiên bản trình duyệt]

## Yêu cầu đầu ra

Vui lòng cung cấp code style sau khi sửa, và đánh dấu phần sửa đổi.
```

## Mẫu 5: Di trú code (Bản rút gọn)

Thích hợp cho: Nâng cấp phiên bản framework, thay đổi stack kỹ thuật

```markdown
## Nhu cầu di trú

**Công nghệ cũ**: [Ví dụ React Class Component]
**Công nghệ mục tiêu**: [Ví dụ React Hooks Function Component]

## Code cũ

```[Ngôn ngữ]
[Dán code cần di trú]
```

## Yêu cầu di trú

- Giữ nguyên chức năng hoàn toàn nhất quán
- Tuân thủ best practice của công nghệ mục tiêu
- [Yêu cầu khác]

## Yêu cầu đầu ra

Vui lòng cung cấp code sau khi di trú, và giải thích các điểm thay đổi chính.
```

## Bản rút gọn: Mẫu sửa nhanh

Khi bạn chỉ cần sửa nhỏ, có thể dùng bản rút gọn này:

```markdown
Hãy sửa đoạn code sau:

```[Ngôn ngữ]
[Code]
```

**Nội dung sửa**: [Tóm tắt sửa cái gì]

**Ràng buộc**:
- Giữ nguyên các phần khác
- [Ràng buộc khác]
```

## Sai lầm thường gặp khi điền

| Sai lầm | Vấn đề | Cách làm đúng |
|-----|------|---------|
| Không dán code hiện tại | AI không hiểu ngữ cảnh | Dán đoạn code liên quan |
| Chỉ nói "tối ưu một chút" | Không biết tối ưu hướng nào | Nói rõ là tính dễ đọc/hiệu năng/cấu trúc |
| Quên nói "không được sửa" | AI có thể tái cấu trúc cả file | Xác định ranh giới, cái nào không động vào |
| Mô tả tham khảo quá trừu tượng | "Đẹp hơn chút" quá mơ hồ | Cho website tham khảo hoặc mô tả cụ thể |

## Điểm cốt yếu phần này

- ✅ **Mở rộng chức năng**: Dán code hiện tại + Mô tả chức năng mới + Xác định phần không được động vào
- ✅ **Tái cấu trúc code**: Xác định hướng tái cấu trúc + Đảm bảo chức năng không đổi
- ✅ **Tối ưu hóa hiệu năng**: Mô tả hiện tượng vấn đề + Đưa ra quy mô dữ liệu + Thiết lập tiêu chuẩn đo lường
- ✅ **Điều chỉnh Style**: Cung cấp tham khảo + Mô tả cụ thể hiệu quả mong muốn
