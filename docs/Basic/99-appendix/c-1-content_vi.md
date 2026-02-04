---
title: "C.1 Liên quan đến Lập trình AI"
---

![99-appendix_c-1-content.png](../../public/images/Basic/99-appendix_c-1-content.png)

# C.1 Liên quan đến Lập trình AI

Gặp từ không biết? Tra ở đây. Mỗi thuật ngữ đều được giải thích bằng ngôn ngữ bình dân nhất.

## Vibe Coding

**Giải thích một câu**: Không viết code, dùng ngôn ngữ tự nhiên bảo AI bạn muốn gì, để AI giúp bạn sinh ra code.

**Ví dụ tương tự**: Giống như bạn bảo thợ sửa nhà "Tôi muốn một phòng khách ấm cúng", chứ không phải tự mình đi xây tường trát vữa.

**Ví dụ**:

- Bạn nói: "Làm một trang web hiển thị danh ngôn mỗi ngày, nền xanh, chữ trắng to"
- AI: Xuất ra code HTML/CSS/JS hoàn chỉnh

## Spec Coding

**Giải thích một câu**: Viết tài liệu quy tả chi tiết trước, sau đó để AI sinh ra code theo quy tả đó.

**Ví dụ tương tự**: Giống như vẽ bản vẽ thiết kế trước khi xây nhà, mỗi phòng rộng bao nhiêu, cửa sổ ở đâu đều viết rõ ràng.

**Phân biệt với Vibe Coding**:
| | Vibe Coding | Spec Coding |
|---|---|---|
| Tài liệu | Không cần | Cần tài liệu chi tiết |
| Phù hợp | Dự án đơn giản, xác minh nhanh | Dự án phức tạp, cộng tác team |
| Đặc điểm | Nhanh, linh hoạt | Chắc chắn, dễ bảo trì |

## Prompt

**Giải thích một câu**: Chỉ thị hoặc câu hỏi bạn đưa cho AI.

**Ví dụ tương tự**: Giống như bạn ghi chú cho shipper: "Ít muối ít dầu, cho nhiều ớt". Prompt viết càng rõ, đồ AI làm ra càng đúng ý bạn.

**Đặc điểm của Prompt tốt**:

- Nói rõ muốn gì (Mục tiêu)
- Nói rõ cho ai dùng (Người dùng)
- Nói rõ không muốn gì (Hạn chế)

## Context (Ngữ cảnh)

**Giải thích một câu**: Thông tin nền tảng mà AI cần để hiểu nhu cầu của bạn.

**Ví dụ tương tự**: Giống như bác sĩ khám bệnh cần biết bệnh sử của bạn. Bạn cung cấp càng nhiều thông tin nền tảng, AI càng đưa ra câu trả lời chính xác.

**Context bao gồm những gì**:

- Những gì bạn đã nói trước đó
- Code bạn cung cấp
- Bối cảnh dự án bạn mô tả
- Tech stack bạn sử dụng

## Context Window (Cửa sổ ngữ cảnh)

**Giải thích một câu**: Giới hạn lượng thông tin AI có thể "nhớ" trong một lần.

**Ví dụ tương tự**: Giống như dung lượng bộ nhớ ngắn hạn của con người. Nói chuyện quá dài, AI sẽ "quên" nội dung nói lúc đầu.

**Ảnh hưởng thực tế**:

- Khi đối thoại quá dài, có thể cần giải thích lại bối cảnh
- Đưa quá nhiều code một lúc, AI có thể xử lý không xuể
- Các công cụ AI khác nhau có kích thước cửa sổ khác nhau

## Hallucination (Ảo giác)

**Giải thích một câu**: AI nói hươu nói vượn một cách nghiêm túc, bịa đặt thông tin không tồn tại.

**Ví dụ tương tự**: Giống như một người bạn quá nhiệt tình muốn giúp đỡ, không biết câu trả lời cũng cố bịa ra một cái.

**Biểu hiện thường gặp**:

- Bịa ra tên thư viện hoặc tên hàm không tồn tại
- Đưa ra code "trông có vẻ đúng nhưng thực tế không chạy được"
- Trích dẫn tài liệu hoặc liên kết không tồn tại

**Cách đối phó**:

- Giữ thái độ hoài nghi với đầu ra của AI, thông tin quan trọng cần xác minh
- Bảo AI giải thích code của nó, kiểm tra logic xem có thông suốt không
- Chạy thử code xem có chạy được không

## Agent (Tác nhân)

**Giải thích một câu**: Hệ thống AI có thể tự chủ hoàn thành nhiệm vụ nhiều bước.

**Ví dụ tương tự**: AI thông thường giống máy tính (bạn hỏi một câu trả lời một câu), Agent giống trợ lý (bạn giao một việc, nó tự lên kế hoạch các bước để hoàn thành).

**Ví dụ**:

- Bạn nói: "Làm giúp tôi một ứng dụng danh sách việc cần làm"
- Agent: Tự phân tích nhu cầu → Thiết kế cấu trúc → Viết code → Kiểm thử → Sửa lỗi

## MCP (Model Context Protocol)

**Giải thích một câu**: Giao thức tiêu chuẩn giúp AI kết nối với công cụ và dữ liệu bên ngoài.

**Ví dụ tương tự**: Giống như tiêu chuẩn cổng USB. Có tiêu chuẩn thống nhất, AI có thể tiện lợi "cắm vào" đủ loại công cụ để sử dụng.

**Công dụng thực tế**:

- Để AI đọc ghi file cục bộ
- Để AI truy cập cơ sở dữ liệu
- Để AI gọi API

## Token

**Giải thích một câu**: Đơn vị cơ bản để AI xử lý văn bản, xấp xỉ một từ tiếng Anh hoặc vài chữ Hán/Việt.

**Ví dụ tương tự**: Giống như "phút" gọi điện thoại. Bạn chat với AI tiêu tốn Token, dùng hết phải nạp tiền.

**Về chi phí**:

- Đa số công cụ tính phí theo Token
- Đầu vào và đầu ra đều tốn Token
- Tiếng Việt/Hán thường tốn nhiều Token hơn tiếng Anh

**Mẹo tiết kiệm Token**:

- Mô tả cố gắng ngắn gọn nhưng không mơ hồ
- Đừng lặp lại thông tin đã nói
- Một lần đối thoại giải quyết một vấn đề
