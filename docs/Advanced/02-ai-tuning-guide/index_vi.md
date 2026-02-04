---
title: "Chương 2: Hướng dẫn sử dụng AI"
---

![02-dev-tools-ai-tuning_index.png](../../public/images/Advanced/02-dev-tools-ai-tuning_index.png)

# Chương 2: Hướng dẫn sử dụng AI

## Lời nói đầu

> Ở chương trước, bạn đã hiểu sự khác biệt giữa mô hình và công cụ, đồng thời hoàn thành việc xây dựng môi trường phát triển. Giờ đây, chúng ta sẽ học cách để AI làm việc cho bạn tốt hơn.

### Kinh tế học trong lập trình AI

Sư phụ nói với bạn, lập trình AI có một thực tế thường bị bỏ qua: **Token chính là tiền**. Mỗi lần bạn bảo AI đọc file dự án, tìm kiếm code, sinh câu trả lời, đều đang tiêu tốn chi phí thực.

Nguyên tắc cốt lõi chỉ có một: **Ngữ cảnh càng lớn, tốn kém càng nhiều**. Đọc cả dự án vs chỉ đọc một file, sự khác biệt là số mũ. Nhưng quan trọng hơn —— ngữ cảnh chính xác không chỉ tiết kiệm tiền, mà còn giúp đầu ra chính xác hơn.

Tối ưu hóa prompt (câu nhắc) không phải là "trau chuốt lời văn", mà là **giảm phạm vi ngữ cảnh AI cần đọc**. Chỉ định đường dẫn file tốt hơn mô tả mơ hồ, chỉ rõ phạm vi chức năng tốt hơn nói chung chung "dự án có vấn đề", xóa bớt lời khách sáo, không cần thiết lập vai chuyên gia, hãy nói thẳng nhiệm vụ.

> 2.1 Kinh tế học trong lập trình AI (./01-ai-economics.md) sẽ giảng giải chi tiết chiến lược tối ưu chi phí.

### Quy trình làm việc VibeCoding

Bạn phát hiện đôi khi đầu ra của AI muôn hình vạn trạng, hoặc nói hươu nói vượn một cách nghiêm túc. Bạn còn gặp lúc AI không biết câu trả lời, nhưng cố tình bịa ra một tình huống.

Sư phụ bảo bạn, cao thủ thực sự không dựa vào cấu hình, mà dựa vào nghệ thuật giao tiếp. Hãy cho AI một "lối thoát", bảo nó: "Nếu không chắc chắn, hãy nói thẳng ra, đợi tôi xác nhận, chứ đừng cố bịa chuyện."

Trước kia bạn nghĩ đâu làm đó, để AI viết luôn, nhưng như thế thường dẫn đến việc phải làm lại. Sư phụ truyền thụ quy trình tiêu chuẩn chỉ có 5 bước: **Trước tiên khám phá cấu trúc dự án, tiếp theo quy hoạch các bước thực hiện, sau đó viết code, kiểm thử xác minh, cuối cùng là commit**. Nghe có vẻ thừa thãi, nhưng làm theo vài lần, bạn thấy hiệu suất tăng hẳn —— vì bạn sẽ không gặp cảnh viết được một nửa mới phát hiện file đó đã có rồi.

Bạn nhận thức sâu sắc: **Cốt lõi của Vibecoding không chỉ là Prompt (Câu nhắc), mà là Workflow (Luồng công việc).**

> 2.2 Quy trình làm việc VibeCoding (./02-vibecoding-workflow.md) sẽ giảng giải chi tiết tâm pháp prompt và quy trình phát triển tiêu chuẩn.

### Kiểm soát phiên bản Git

Nhìn bạn nóng lòng muốn để AI sửa lớn code, sư phụ đột nhiên giữ tay bạn lại. Ông bảo, lập trình AI rất quyết liệt, có thể vì sửa 1 Bug mà làm hỏng 3 chức năng cũ. Nên bắt buộc phải cấu hình tốt **Git**, thiết lập thói quen **ghi lại phiên bản cục bộ** tần suất cao.

> **"Mỗi khi bạn hoàn thành phát triển một chức năng độc lập, hoặc sửa xong một Bug và kiểm thử thông qua, hãy tự động chạy git commit để nộp code, và sinh một câu commit message tiếng Việt ngắn gọn."**

Từ đó, quy trình phát triển của bạn trở thành: AI viết xong chức năng → Tự động lưu trữ. Một khi code vỡ trận, có thể quay lui bất cứ lúc nào. Về cấu hình chi tiết `.gitignore`, chúng ta sẽ giảng ở các chương sau.

### Kỹ thuật cấu hình

Ngoài chọn đúng công cụ, sư phụ còn truyền cho bạn 3 chiêu để AI dùng sướng hơn, giải quyết vấn đề AI hay quên, viết bậy:

**Quy tắc dự án**: Tạo file kiểu `.iderules` ở thư mục gốc dự án, viết vào các quy tắc như "Cấm dùng kiểu `any`", "Bắt buộc dùng `pnpm`". Từ đó về sau, mỗi khi viết code AI sẽ tham khảo **quy chuẩn dự án** này trước, chất lượng code sinh ra tăng vọt.

**Kỹ năng chuyên biệt**: Tạo hoặc cài đặt **Skills**, dùng ngôn ngữ tự nhiên định nghĩa chỉ thị riêng, ví dụ "Mỗi khi tôi nói 'phân tích dữ liệu', thì tự động chạy script phân tích". Điều này tương đương định nghĩa một quy trình thao tác chuẩn (SOP) cho AI.

**Trao quyền năng**: Cấu hình **MCP và Plugin**, để AI **kết nối kho GitHub** xem code, **kết nối cơ sở dữ liệu** tra dữ liệu, đọc bản thiết kế **Figma**. Bạn không cần hiểu nguyên lý bên dưới, chỉ cần cấu hình đơn giản, AI sẽ sở hữu năng lực thao tác công cụ bên ngoài.

> 2.3 MCP, Plugin và Skills (./03-mcp-and-skills.md) và 2.4 Cấu hình quy tắc dự án (./04-project-config.md) sẽ giảng giải chi tiết các kỹ thuật cấu hình này.

### Tâm pháp Debug

Trước khi kết thúc lời nói đầu, sư phụ còn truyền một bộ tâm pháp debug. Ông nói: "Có AI rồi, gặp lỗi đừng hoảng. Nhưng muốn AI giúp, con phải học cách cầu cứu đúng đắn."

**Thứ nhất, cung cấp nhật ký lỗi đầy đủ**. Người mới thấy báo lỗi đỏ lòm thường sợ, chỉ copy dòng cuối cùng. Nhưng AI giống bác sĩ, cần thấy triệu chứng đầy đủ mới chẩn đoán chính xác. Bạn nên **chọn toàn bộ, copy, gửi nguyên văn cho AI những thông tin lỗi màu đỏ trông dài nhất, phức tạp nhất**.

**Thứ hai, mô hình sửa lỗi vòng lặp**. Nếu lần đầu AI sửa chưa được, đừng bỏ cuộc. Mô tả kết quả sau khi bạn thử: "Tôi sửa theo cách của bạn rồi, nhưng giờ xuất hiện lỗi mới...", để AI tiếp tục thử. Đa số Bug đều cần 2-3 vòng lặp mới giải quyết được.

> 2.5 Tâm pháp debug hiệu quả (./05-debugging-tips.md) sẽ dạy bạn phương pháp debug trọn vẹn này.

### Kiến thức mở rộng

Sư phụ bảo, khi bạn thành thạo luồng công việc cốt lõi, còn có thể khám phá hệ thống đa đại lý (multi-agent): Để nhiều AI phối hợp làm việc, một viết code, một review; một viết test, một viết tài liệu. Chúng có thể xử lý song song để tăng tốc độ, hoặc xử lý tuần tự để đảm bảo chất lượng. Phần nội dung này đã được giảng chi tiết trong 2.2 Quy trình làm việc VibeCoding.

Hiện tại hãy nắm vững luồng công việc cốt lõi trước, đi từng bước một.

---

### Thực hành

Tôi biết bạn đang rất nóng lòng, nhưng đừng vội —— xem xong chương 3 PRD và tài liệu hướng dẫn sẽ rõ ràng hơn. Sau đó tìm một chức năng bạn vừa viết hoặc muốn viết gần đây, nói với AI: "Trước tiên khám phá cấu trúc dự án, tiếp theo quy hoạch các bước thực hiện, sau đó viết code, mỗi khi hoàn thành một bước thì commit code". Làm theo nhịp điệu của nó, bạn sẽ phát hiện cốt lõi của Vibecoding là Workflow chứ không phải Prompt!
