---
title: "Chương 3: Tư duy sản phẩm và Điều hướng bằng tài liệu"
---

# Chương 3: Tư duy sản phẩm và Điều hướng bằng tài liệu

## Lời nói đầu: Tại sao phải viết tài liệu trước khi viết code?

Trước khi để AI viết code, sư phụ giữ tay bạn lại khi bạn định lao đầu vào làm. Ông bảo: **"Trước khi viết code, hãy viết tài liệu"**. Nếu không có bản vẽ, AI sẽ dễ dàng trở thành con ngựa đứt cương, sinh ra đống code thiếu cấu trúc, tạo ra một mớ hỗn độn không ai hiểu nổi, cũng chẳng ai sửa nổi.

### Phương pháp 3 bước kiểm chứng sản phẩm

Sư phụ nói: "Trước khi viết bất kỳ dòng code nào, hãy thực hiện **Phương pháp 3 bước kiểm chứng sản phẩm**:

**Bước 1: 3 câu hỏi linh hồn**. Người dùng là ai? Nỗi đau ở đâu? Tại sao dùng của bạn? 3 câu hỏi này trông đơn giản nhưng nhiều người không trả lời được. Nếu người dùng là 'tất cả mọi người', thì bằng với không có người dùng. Nếu nỗi đau là 'tôi thấy cần', thì đó không phải nỗi đau thật. Nếu câu trả lời cho 'tại sao dùng của bạn' là 'vì chúng tôi có công nghệ xịn nhất', thì người dùng chẳng quan tâm đâu.

**Bước 2: Tư duy MVP**. Phiên bản đơn giản nhất để kiểm chứng giả thuyết là gì? Đừng mong một phát làm ra sản phẩm hoàn hảo. Hãy làm sản phẩm khả thi tối thiểu (MVP) trước, kiểm chứng nhanh giả thuyết cốt lõi. Ví dụ muốn làm App giao đồ ăn, MVP có thể chỉ là một nhóm Zalo + nhân viên trực đơn, chứ không phải một App hoàn chỉnh.

**Bước 3: Kiểm chứng nhanh**. Dùng chi phí thấp nhất để kiểm chứng giả thuyết. Có thể dùng cách thủ công để phục vụ trước, hoặc làm một trang Landing Page đơn giản để thu thập phản hồi. Nhớ kỹ: Thất bại càng sớm, chi phí càng thấp.

PRD chính là quy chuẩn thực thi của AI. Khi bạn đã nghĩ thông 3 bước trên, PRD chính là việc phiên dịch những suy nghĩ đó thành tài liệu cấu trúc hóa mà AI hiểu được.

### Tác dụng và Cấu trúc của PRD

Trong phát triển truyền thống, PRD là để cho team xem; nhưng trong phát triển AI, tác dụng quan trọng hơn của PRD là cung cấp ngữ cảnh hoàn chỉnh cho AI, để nó không cần đoán mò ý đồ của bạn.

Sư phụ bảo bạn, một PRD hoàn chỉnh bao gồm 5 phần cốt lõi:

**Phần 1: Thông tin tài liệu**. Ghi lại phiên bản hiện tại, giai đoạn dự án (Review nhu cầu, Đang thiết kế UI, Đang Dev, Đã lên sóng), ai là người phụ trách chính. Còn phải có bảng lịch sử cập nhật, ghi rõ quá trình từ "Bản 1" đến "Bản 9", để thành viên team hiểu sự biến đổi của nhu cầu.

**Phần 2: Bối cảnh và Mục tiêu**. Đây là linh hồn của PRD, phải trả lời 4 vấn đề then chốt:

- **Tổng quan dự án**: Dùng một hai câu tóm tắt sản phẩm này làm gì
- **Vấn đề cốt lõi**: Người dùng mục tiêu là ai? Họ gặp nỗi đau gì trong ngữ cảnh nào? Những vấn đề này gây ra ảnh hưởng tiêu cực gì?
- **User Story**: Mô tả nhu cầu cụ thể theo format "Là một [Vai trò], tôi muốn [Làm gì đó], để [Đạt được giá trị gì]"
- **Mục tiêu dự án**: Giá trị người dùng là gì? Giá trị thương mại là gì? Kỳ vọng đạt mục tiêu cụ thể nào (nguyên tắc SMART)?

**Phần 3: Tổng quan giải pháp**. Dùng phương thức trực quan hóa hiển thị toàn cảnh sản phẩm:

- **Lưu đồ nghiệp vụ cốt lõi**: Dùng biểu đồ Mermaid mô tả quy trình trọn vẹn người dùng hoàn thành nhiệm vụ
- **Lưu đồ chức năng**: Hiển thị các trang chính và module chức năng tổ chức, xâu chuỗi thế nào
- **Kiến trúc thông tin**: Liệt kê tất cả nội dung thông tin và quan hệ phân cấp của sản phẩm

**Phần 4: Giải pháp chi tiết**. Đây là phần chi tiết nhất, là căn cứ trực tiếp cho Dev và Design:

- **Prototype và Tương tác**: Mô tả trạng thái khởi tạo, thao tác kích hoạt, trạng thái thành công/thất bại của mỗi trang
- **Xử lý trường hợp biên (Edge Case)**: Người dùng thoát giữa chừng thì sao? Bấm nhanh liên tục thì sao?
- **Nhu cầu phi chức năng**: Yêu cầu hiệu năng, tương thích, tracking số liệu

**Phần 5: Kế hoạch lên sóng**. Định nghĩa vòng đời nhu cầu:

- **Lịch trình**: Mốc thời gian Review, Design, Dev, Test
- **Gray Release (Phát hành hạn chế)**: Mở cho nhân viên nội bộ trước, rồi đến 1% người dùng hạt giống, rồi dần dần mở toàn bộ

Quan trọng nhất là **Cấu trúc hóa + Trực quan hóa**, combo **Markdown + Mermaid** là lựa chọn tối ưu, vì AI hiểu định dạng này tốt nhất. Có "Nguồn sự thật duy nhất" này rồi, đầu ra của AI sẽ ổn định hơn nhiều, không còn bị bùng nổ nhu cầu nữa.

### Thực chiến viết PRD

Sư phụ đưa bạn xem một mẫu PRD chuẩn doanh nghiệp, bên trong liệt kê chi tiết quá trình lặp từ "Bản 1" đến "Bản 9".

**Bản 1 (Review nội bộ)**: Trọng điểm trình bày bối cảnh, mục tiêu và giá trị cốt lõi. Lúc này chưa cần quá chi tiết, chỉ cần nói rõ "tại sao làm" là được.

**Bản 5 (Review dự án)**: Bổ sung quy trình nghiệp vụ cốt lõi, lưu đồ chức năng và mô tả tương tác prototype. Lúc này phải để Dev, Design, Test đều hiểu bạn định làm gì.

**Bản 9 (Chốt trước Dev)**: Hợp nhất thiết kế UI cuối cùng, bổ sung trường hợp biên, phương án tracking và kế hoạch lên sóng. Lúc này tài liệu phải đủ chi tiết để Dev cứ thế mà làm.

Sư phụ nhấn mạnh: "PRD không phải viết một phát xong ngay, mà là lặp lại (iteration). Bản 1 nghĩ rõ 'tại sao', bản 5 nghĩ rõ 'là gì', bản 9 nghĩ rõ 'làm thế nào'. Mỗi bước đều có review và sửa chữa, tránh để đến cuối mới phát hiện vấn đề lớn."

**Ngoài tư duy lặp lại, quản lý nhu cầu cũng là năng lực cốt lõi của Product Manager.**

### Kỹ thuật quản lý nhu cầu

Trong quá trình viết PRD, có vài điểm thực dụng:

**Quản lý phạm vi nhu cầu**. Xác định rõ "In-Scope (Trong phạm vi)" và "Out-of-Scope (Ngoài phạm vi)", quản lý kỳ vọng của team hiệu quả, tránh phạm vi phình to. Ví dụ lần này làm AI tóm tắt, phần lịch sử để V2.0 hẵng tính.

**Sắp xếp độ ưu tiên**. Phân rã nhu cầu thành các điểm cụ thể, dùng bảng liệt kê ID, Module, Mô tả, Độ ưu tiên, Trạng thái. Ưu tiên cao làm trước, trung bình thì quan sát, thấp thì lùi lại.

**User Story**. Xuất phát từ góc nhìn người dùng, mô tả nhu cầu theo format chuẩn. Cách này gần gũi với người dùng hơn là nói "tôi muốn làm một tính năng".

**Thiết lập mục tiêu SMART**. Mục tiêu dự án phải tuân thủ nguyên tắc SMART —— Cụ thể, Đo lường được, Khả thi, Liên quan, Có thời hạn. Ví dụ "Sau khi lên sóng 3 tháng, tỷ lệ sử dụng tính năng tóm tắt đạt 30%" rõ ràng hơn nhiều so với "tăng độ tích cực của người dùng".

### Markdown và Mermaid

Trong quá trình viết tài liệu, bạn cũng tiện thể tìm hiểu **Markdown (.md)** và **Mermaid**. Markdown dùng để soạn thảo văn bản được dàn trang ngay ngắn, Mermaid dùng để vẽ lưu đồ, biểu đồ tuần tự bằng code văn bản.

Sư phụ bảo, cung cấp những tài liệu này cho AI, tỷ lệ chính xác của code sinh ra sẽ tăng vọt.

> Mermaid trực quan hóa logic nghiệp vụ, AI có thể hiểu chính xác quy trình tương tác. Cách thức trực quan hóa này cực kỳ quan trọng trong phát triển AI.

Sư phụ bổ sung: "Viết PRD không phải hình thức chủ nghĩa, mà là để rèn luyện năng lực định nghĩa vấn đề của con. Nhiều người cứ bảo AI 'làm hộ cái chức năng', kết quả sửa tới sửa lui. Nhưng viết rõ mục tiêu, người dùng, ngữ cảnh, logic tương tác trước, AI thường làm một phát ăn ngay. Sự khác biệt nằm ở chỗ nghĩ có thông hay không."

Cuối cùng, sư phụ còn nhắc đến **Swagger**. Sau này khi dự án phức tạp lên, tận dụng Swagger tự động sinh tài liệu API, sẽ đảm bảo tài liệu và code nhất quán hiệu quả hơn.

À, nhớ bảo AI cập nhật tài liệu bất cứ lúc nào nhé.

> **Bước tiếp theo**: Về việc viết chi tiết bản hướng dẫn dự án, hãy xem phần "Tài liệu dự án README.md" trong **Chương 4: Thường thức phát triển và Tech Stack**.

---

### Điều hướng tiểu mục

```
- **3.1 Thực chiến kiểm chứng ý tưởng** (./01-product-validation.md) 🟢 - 3 câu hỏi linh hồn, Tư duy MVP, Xác định Out-of-Scope
- **3.2 Kỹ thuật thảo luận nhu cầu với AI** (./02-discuss-with-ai.md) 🟢 - Chủ động để AI xác nhận mức độ hiểu, phát hiện điểm mù
- **3.3 Mẫu PRD chuẩn và hướng dẫn tránh hố** (./03-prd-template-guide.md) 🟢 - Template hoàn chỉnh + Quan hệ nhân quả Chi tiết→Code + Kỹ thuật trực quan hóa
- **3.4 Hiểu cách AI thực thi PRD** (./04-coding-agents.md) 🟢 - Cách AI "đọc", Quan hệ nhân quả PRD→Code, Điểm mù nhận thức
```

---

### Mục tiêu học tập

Hoàn thành chương này, bạn sẽ có thể:

- ✅ Nắm vững danh sách chi tiết bắt buộc xác nhận khi thảo luận nhu cầu với AI
- ✅ Dùng phương pháp 3 bước kiểm chứng sản phẩm để phán đoán ý tưởng có đáng làm không
- ✅ Sử dụng template chuẩn viết PRD thân thiện với AI
- ✅ Hiểu những chi tiết nào ảnh hưởng đến chất lượng code AI sinh ra
- ✅ Rèn luyện năng lực định nghĩa vấn đề, nâng cao hiệu suất cộng tác với AI

---

### Thực hành

Bây giờ, hãy mở một ý tưởng chức năng bạn muốn làm gần đây, trên giao diện web trao đổi với AI theo danh sách chi tiết ở bài 3.2. Xác nhận xong, dùng template bài 3.3 để AI sinh bản nháp PRD.

Bạn sẽ phát hiện: Nghĩ càng thông, AI viết càng chuẩn.

---

## Triết lý cốt lõi

> "Nghĩ kỹ rồi hãy làm, dùng tài liệu rèn luyện tư duy."

Chương này nhấn mạnh rằng, trong kỷ nguyên AI, **năng lực định nghĩa vấn đề quan trọng hơn năng lực hiện thực hóa code**. PRD không phải hình thức, mà là sự thể hiện của tư duy sản phẩm —— từ "tại sao làm" đến "là gì" rồi đến "làm thế nào", bước nào cũng phải nghĩ thông. Có PRD cấu trúc hóa làm "Nguồn sự thật duy nhất", AI mới trở thành đối tác thực thi hiệu quả chứ không phải kẻ đoán mò.

---

**Chương sau**: Chương 4: Thường thức phát triển và Tech Stack (../04-dev-fundamentals/index.md)
