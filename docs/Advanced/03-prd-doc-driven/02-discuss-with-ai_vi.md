---
title: "3.2 Xác nhận nhu cầu với AI"
description: "Kỹ thuật giao tiếp tránh hiểu lầm"
chapter: "Chương 3"
priority: "🔴"
---

# 3.2 Xác nhận nhu cầu với AI 🔴

> **Đọc xong phần này, bạn sẽ thu hoạch được:**
>
> - Hiểu điểm mù nhận thức của AI, biết khi nào cần chủ động xác nhận
> - Nắm vững template prompt để AI xác nhận mức độ hiểu
> - Học cách dùng checklist xác nhận để kiểm tra chi tiết then chốt
> - Nắm vững phương pháp prompt để phát hiện điểm mù

> Lời nói đầu đã nhắc đến: AI sẽ không chủ động hỏi bạn, bạn cần chủ động để nó xác nhận mức độ hiểu.

---

## Điểm mù nhận thức của AI

AI sẽ không chủ động đặt câu hỏi. Khi mô tả nhu cầu mơ hồ, nó sẽ xử lý theo cách hiểu mặc định hoặc mô hình phổ biến. Cách xử lý mặc định này thường không khớp với kỳ vọng.

Sự hiểu của AI đến từ ngữ cảnh. Ngữ cảnh càng đầy đủ, sự hiểu càng chính xác. Nhưng ngữ cảnh không phải "càng nhiều chữ càng tốt", mà là "thông tin then chốt càng rõ ràng càng tốt".

Sự khác biệt này bắt nguồn từ cách làm việc của AI. Khi bạn bàn bạc nhu cầu với lập trình viên, nếu đối phương có chỗ chưa rõ, họ sẽ dừng lại hỏi bạn: "Nút này đặt góc trên trái hay trên phải?", "Người dùng chưa đăng nhập có thấy trang này không?". Những câu hỏi này có thể làm bạn thấy hơi phiền, nhưng chúng đảm bảo sự thống nhất trong cách hiểu của cả hai bên. AI không làm thế. Khi bạn đưa ra một yêu cầu mơ hồ, AI sẽ dựa trên các mẫu phổ biến trong dữ liệu huấn luyện để đưa ra giả định, sau đó bắt đầu sinh code luôn. Nếu giả định này vô tình khớp ý bạn thì tốt; nhưng nếu giả định sai, bạn sẽ tốn thêm chi phí giao tiếp ở các bước lặp sau để sửa lại.

Tệ hơn nữa, các giả định của AI thường "hợp lý" —— giải pháp nó chọn khả thi về kỹ thuật, tự logic về lý luận, chỉ là không khớp nhu cầu cụ thể của bạn. Sự sai lệch này rất khó phát hiện trước khi sinh code, vì bạn có thể chẳng bao giờ nghĩ đến việc đi xác nhận những chi tiết "hiển nhiên" đó. Chỉ khi code chạy lên, thấy kết quả không như ý, vấn đề mới lộ ra.

Nguồn gốc sai lệch nhận thức phổ biến:

| Nguồn sai lệch               | Vấn đề gây ra                                       |
| ---------------------------- | --------------------------------------------------- |
| Người dùng nói mơ hồ         | AI đoán người dùng mục tiêu, có thể đoán sai        |
| Ranh giới chức năng không rõ | AI có thể thêm chức năng, cũng có thể sót chức năng |
| Ràng buộc kỹ thuật chưa nói  | AI chọn công nghệ không tương thích                 |
| Trường hợp biên chưa xét     | Code sinh ra thiếu xử lý lỗi                        |

Cốt lõi của việc chủ động xác nhận là: **Đừng đợi AI hỏi bạn, hãy bắt AI nói rõ cách hiểu của nó**.

---

## Template prompt xác nhận mức độ hiểu

Mỗi khi thảo luận xong nhu cầu, dùng template sau để AI xác nhận mức độ hiểu:

> Hãy xác nhận bạn đã hiểu nhu cầu của tôi. Vui lòng phản hồi theo định dạng sau:
>
> 1. **Người dùng mục tiêu**: [Người dùng mục tiêu bạn hiểu là ai]
> 2. **Chức năng cốt lõi**: [3-5 chức năng cốt lõi bạn hiểu]
> 3. **Những việc không làm**: [Những chức năng bạn hiểu là sẽ không làm]
> 4. **Vấn đề tiềm ẩn**: [Những chỗ bạn nghĩ tôi có thể chưa cân nhắc đến]
>
> Nếu có bất kỳ chỗ nào không chắc chắn, hãy liệt kê danh sách câu hỏi.

Tác dụng của template này là bắt AI xuất ra rõ ràng cách hiểu của nó, tiện cho việc kiểm tra từng mục.

Khi dùng template này, đừng coi nó là quy trình hình thức. Giá trị thực sự của nó nằm ở việc ép AI hiển thị hóa các giả định ngầm. Khi AI viết ra "Người dùng mục tiêu là dân văn phòng", bạn có thể phát hiện ngay sự hiểu này có chuẩn không —— có thể ý bạn là "sinh viên", hay "freelancer". Sự đối chiếu hiển thị này khiến hiểu lầm không còn chỗ trốn.

Một lợi ích khác dễ bị bỏ qua là template này thực chất đang huấn luyện AI hiểu nhu cầu của bạn tốt hơn. Khi bạn dùng lần đầu, sự xác nhận của AI có thể sai lệch nhiều; nhưng qua quá trình bạn liên tục sửa nắn, AI sẽ dần học được sở thích và thói quen của bạn, những lần sau sẽ hiểu chuẩn hơn. Đây là quá trình thích nghi hai chiều (two-way adaptation).

### Tại sao lại hiệu quả

| Chỉ nói "Giúp tôi làm X"            | Dùng template xác nhận                 |
| ----------------------------------- | -------------------------------------- |
| AI hiểu theo phán đoán              | AI bắt buộc nói rõ cách hiểu           |
| Không biết AI hiểu đúng không       | Có thể kiểm tra từng mục               |
| Có hiểu lầm thì phải đập đi làm lại | Phát hiện hiểu lầm trước khi viết code |

---

## Checklist chi tiết bắt buộc xác nhận

Khi để AI xác nhận, hãy kiểm tra xem nó đã trả lời những câu hỏi then chốt sau chưa.

### Người dùng và Ngữ cảnh

| Mục xác nhận              | Tại sao quan trọng                         |
| ------------------------- | ------------------------------------------ |
| Người dùng mục tiêu là ai | Quyết định độ phức tạp UI, cách thao tác   |
| Ngữ cảnh sử dụng là gì    | Quyết định chọn công nghệ (Mobile/Desktop) |
| Giải quyết vấn đề gì      | Đảm bảo làm tính năng có giá trị           |

### Chức năng cốt lõi

| Mục xác nhận                             | Tại sao quan trọng                              |
| ---------------------------------------- | ----------------------------------------------- |
| 3-5 chức năng cốt lõi nhất               | Ngăn AI thêm quá nhiều tính năng                |
| Quy trình người dùng hoàn thành nhiệm vụ | Đảm bảo AI hiểu logic nghiệp vụ                 |
| Có những thay đổi trạng thái nào         | Ảnh hưởng thiết kế UI (Loading, Success, Error) |

### Những việc không làm

| Mục xác nhận                      | Tại sao quan trọng                  |
| --------------------------------- | ----------------------------------- |
| Những chức năng lần này không làm | Ngăn phạm vi phình to (scope creep) |
| Những chức năng mãi mãi không làm | Giữ sản phẩm tập trung              |

AI có xu hướng "làm thêm", phải bảo rõ ranh giới cho nó.

Xu hướng này có nguồn gốc của nó. Trong dữ liệu huấn luyện, AI nhìn thấy vô số ứng dụng nhiều chức năng, nó học được "sản phẩm hoàn chỉnh nên bao gồm những gì". Nhưng nhu cầu của bạn có thể chỉ là một bản prototype cực giản, hoặc một công cụ cho ngữ cảnh đặc thù. Nếu không rõ ranh giới, AI sẽ mặc định sinh code theo tiêu chuẩn "sản phẩm hoàn chỉnh", kết quả là over-engineering (kỹ thuật thái quá).

Việc làm rõ "những việc không làm" còn có lợi ích tâm lý: Nó buộc bạn suy nghĩ xem cốt lõi sản phẩm là gì. Khi bạn liệt kê "không làm đăng nhập, không đồng bộ cloud, không phân loại tag", thực ra bạn đang xác nhận giá trị bản chất nhất của sản phẩm. Sự tập trung này cực kỳ quan trọng với sản phẩm giai đoạn đầu.

### Dữ liệu và Trạng thái

| Mục xác nhận                  | Tại sao quan trọng                   |
| ----------------------------- | ------------------------------------ |
| Cần lưu trữ dữ liệu gì        | Quyết định thiết kế cấu trúc dữ liệu |
| Dữ liệu đến từ đâu            | Quyết định cách hiện thực hóa        |
| Xử lý trường hợp biên thế nào | Ngăn bug (click nhanh, lỗi mạng...)  |

### Ràng buộc kỹ thuật

| Mục xác nhận                      | Tại sao quan trọng             |
| --------------------------------- | ------------------------------ |
| Có giới hạn stack công nghệ không | Ảnh hưởng lựa chọn code của AI |
| Cần tương thích thiết bị nào      | Ảnh hưởng hiện thực hóa UI     |
| Có yêu cầu hiệu năng không        | Ảnh hưởng phương án kỹ thuật   |

---

## Prompt phát hiện điểm mù

Sau khi thảo luận nhu cầu, dùng prompt sau để AI giúp phát hiện vấn đề:

> Dựa trên thảo luận vừa rồi, hãy liệt kê:
>
> 1. Những trường hợp biên tôi có thể chưa tính đến
> 2. Những tính năng bạn thấy phổ biến nhưng tôi có thể không cần
> 3. Chi tiết kỹ thuật cần làm rõ
>
> Hãy liệt kê từng mục, tôi sẽ xác nhận từng cái.

AI có thể chỉ ra:

- Người dùng xóa dữ liệu xong có cần khôi phục không?
- Danh sách dữ liệu có giới hạn số lượng không?
- Nếu người dùng nhập nội dung siêu dài thì hiển thị thế nào?
- Có cần dùng trên điện thoại không?

Đây chính là những chi tiết bị bỏ sót.

Để AI giúp phát hiện điểm mù là cách làm hiệu quả cao. Là chủ sản phẩm, bạn khó tránh khỏi những định kiến tư duy —— bạn sẽ mặc định một số việc là "hiển nhiên", hoặc một số tình huống là "không xảy ra". AI không có định kiến đó, nó sẽ soi xét nhu cầu của bạn từ góc độ logic thuần túy, chỉ ra những vấn đề bạn bỏ qua vì quá quen thuộc.

Tất nhiên, vấn đề AI chỉ ra không nhất thiết đều phải giải quyết. Một số trường hợp biên có thể cực hiếm xảy ra, không đáng để tăng độ phức tạp. Nhưng biết sự tồn tại của chúng giúp bạn đưa ra sự đánh đổi có hiểu biết, chứ không phải mạo hiểm trong vô tri.

---

## Nguyên tắc Giải pháp đi trước

Trước khi để AI sinh code hoàn chỉnh, hãy để nó sinh giải pháp hoặc kiến trúc trước.

Lợi ích của việc để AI ra giải pháp trước:

- Phát hiện sai lệch trong cách hiểu nhanh hơn
- Sửa giải pháp tốn ít chi phí hơn sửa code
- Đảm bảo kiến trúc tổng thể hợp lý rồi mới đi vào chi tiết

Giải pháp đi trước là một ứng dụng của "Chuỗi tư duy" (Chain of Thought). Khi AI trực tiếp sinh code, nó đang "vừa nghĩ vừa viết" —— tên hàm, tên biến được quyết định tức thì. Cách này dễ rơi vào tối ưu cục bộ, dẫn đến kiến trúc tổng thể hỗn loạn. Còn việc xuất ra giải pháp trước tương đương để AI hoàn thành một lần suy nghĩ trọn vẹn, chốt khung sườn tổng thể, rồi mới đi vào hiện thực hóa cụ thể.

Từ góc độ tải nhận thức, xác nhận giải pháp cũng giảm độ khó khi review của bạn. Rà soát một tài liệu giải pháp, bạn chỉ cần quan tâm thiết kế tầng cao có hợp lý không; còn rà soát code, bạn cần quan tâm cả logic kiến trúc lẫn chi tiết cú pháp. Cái trước dễ phát hiện hiểu lầm căn bản, cái sau thường làm người ta sa lầy vào chi tiết mà bỏ qua vấn đề định hướng.

Template xác nhận giải pháp:

> Xin đừng viết code vội, hãy đưa ra phương án thực hiện trước:
>
> 1. Thiết kế cấu trúc dữ liệu
> 2. Các trang/component chính và trách nhiệm
> 3. Ý tưởng thực hiện quy trình cốt lõi
> 4. Điểm khó kỹ thuật có thể gặp phải

---

## So sánh: Có xác nhận vs Không xác nhận

### Không xác nhận (Lỗi thường gặp)

```
Bạn: Giúp tôi làm một cái Todo List.
AI: [Sinh phiên bản phức tạp có đăng nhập, đồng bộ cloud, phân loại tag]
Bạn: Nhiều quá, tôi chỉ cần cái đơn giản thôi.
AI: [Sinh lại, nhưng có thể vẫn còn tính năng khác bạn không nói]
```

### Có xác nhận (Cách làm đúng)

```
Bạn: Giúp tôi làm một cái Todo List. Hãy xác nhận mức độ hiểu...
AI: Tôi có vài câu hỏi... Dùng cá nhân hay cho nhóm?
Bạn: Cá nhân, chỉ cần thêm/tick/xóa.
AI: Đã xác nhận: Dùng cá nhân, chức năng cốt lõi là thêm/tick/xóa task, không làm đăng nhập/đồng bộ cloud/phân loại tag.
AI: [Sinh phiên bản chính xác]
```

---

## Checklist kiểm tra kết thúc thảo luận

Khi có thể tích (tick) hết các mục này, là có thể để AI sinh PRD hoặc code rồi:

- [ ] AI đã nói rõ người dùng mục tiêu là ai
- [ ] AI đã liệt kê 3-5 chức năng cốt lõi
- [ ] AI đã làm rõ không làm những chức năng nào
- [ ] AI đã hiểu quy trình sử dụng trọn vẹn
- [ ] Dữ liệu lưu thế nào, lưu cái gì đã rõ
- [ ] Trường hợp biên đã thảo luận
- [ ] Ràng buộc kỹ thuật đã nói rõ
- [ ] **Để AI tóm tắt xác nhận, cách hiểu của nó chính xác**

---

## Câu hỏi thường gặp

### Q1: AI liệt kê rất nhiều chức năng tôi không cần

**A**: Điều này chứng tỏ ranh giới chưa đủ rõ. Trong template xác nhận hãy nhấn mạnh "những việc không làm", và liệt kê cụ thể các loại chức năng không cần thiết.

### Q2: AI hiểu sai hoàn toàn

**A**: Đừng nói thẳng "sai rồi". Hãy tìm hiểu xem nó đang hiểu thế nào, rồi chỉ ra sai lệch. Dùng cấu trúc đối chiếu "Ý tôi nói X là chỉ..., bạn lại hiểu là...".

### Q3: Lần nào cũng phải viết prompt xác nhận dài thế à?

**A**: Không cần. Lần đầu hoặc nhu cầu phức tạp mới cần xác nhận đầy đủ. Nhu cầu đơn giản hoặc các lần lặp sau, có thể rút gọn thành "Hãy xác nhận cách hiểu" hoặc "Có chỗ nào chưa rõ không".

### Q4: AI xác nhận rồi, nhưng sinh code vẫn sai

**A**: Kiểm tra xem có sót chi tiết nào không, hoặc lúc AI sinh giải pháp bạn chưa rà soát kỹ. Giải pháp là bản vẽ của code, giải pháp sai thì code chắc chắn sai.

---

## Trọng điểm cốt lõi

- ✅ **AI sẽ không chủ động hỏi**, cần chủ động bắt nó xác nhận cách hiểu
- ✅ Dùng template xác nhận để AI nói rõ cách hiểu
- ✅ Kiểm tra phản hồi xác nhận của AI, phát hiện hiểu lầm phải sửa ngay
- ✅ Để AI liệt kê các vấn đề có thể bị bỏ sót
- ✅ Giải pháp đi trước, xác nhận phương án rồi mới sinh code
- ✅ Hai bên thống nhất cách hiểu rồi mới để AI viết PRD

Sau khi xác nhận xong, tiếp theo dùng template tiêu chuẩn viết PRD.

---

## Nội dung liên quan

- Trước đó: [3.1 Thực chiến kiểm chứng ý tưởng](./01-product-validation_vi.md)
- Chi tiết: [3.3 Thực chiến viết PRD](./03-prd-template-guide_vi.md)
