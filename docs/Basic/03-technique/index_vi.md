---
title: "Chương 3: Kỹ pháp —— Nghệ thuật đối thoại với AI"
---


![03-technique_index.png](../../public/images/Basic/03-technique_index.png)
# Chương 3: Kỹ pháp —— Nghệ thuật đối thoại với AI

> **Định vị chương**: Chương này là chương kỹ năng cốt lõi của Vibe Coding, từ "biết nói" đến "nói đúng", giúp độc giả nắm vững phương pháp luận và kỹ thuật thực hành giao tiếp hiệu quả với AI.

## Từ "nghĩ thông suốt" đến "nói rõ ràng"

Ở Chương 2, chúng ta đã học cách **nghĩ thông suốt** —— sử dụng các công cụ tư duy của Giám đốc sản phẩm (JTBD, tư duy ngược, tư duy phép trừ, tư duy câu chuyện, ba câu hỏi linh hồn) để chải chuốt nhu cầu, xác định rõ làm cái gì, làm cho ai, tại sao làm.

Chương này, chúng ta sẽ học cách **nói rõ ràng** —— diễn đạt những thứ đã nghĩ thông suốt theo cách mà AI có thể hiểu được.

Mối quan hệ giữa hai chương này là:

| Chương | Nhiệm vụ cốt lõi | Ví von |
|------|---------|------|
| Chương 2 Tâm pháp | Nghĩ thông suốt làm cái gì | Viết kịch bản tốt |
| Chương 3 Kỹ pháp | Nói rõ ràng để AI làm | Đạo diễn chỉ huy |

**Không có sự suy nghĩ của Chương 2, kỹ thuật của Chương 3 chỉ là lầu các trên không; không có sự diễn đạt của Chương 3, suy nghĩ của Chương 2 không thể hạ cánh.**

## Tại sao chương này lại quan trọng đến vậy

Trong thế giới của Vibe Coding, **khả năng diễn đạt của bạn chính là khả năng lập trình**.

Lập trình truyền thống cần học cú pháp của ngôn ngữ lập trình, còn Vibe Coding cần học cú pháp của "đối thoại với AI". Đây không đơn giản là dịch nhu cầu sang ngôn ngữ tự nhiên, mà là một bộ phương pháp luận giao tiếp hoàn chỉnh —— bạn cần biết:

- Khi nào nên nói gì (Thời điểm và chiến lược)
- Nói thế nào để AI hiểu (Cấu trúc và định dạng)
- AI không hiểu thì làm sao (Lặp lại và sửa chữa)
- Làm sao để AI nhớ những gì bạn đã nói (Quản lý ngữ cảnh)

**Một prompt tốt có thể khiến AI đưa ra code 90 điểm ngay lần đầu; một prompt tệ có thể khiến bạn vật lộn trong cái hố 20 điểm suốt hai tiếng đồng hồ.**

## Mục tiêu học tập chương này

Sau khi hoàn thành chương này, bạn sẽ có thể:

- ✅ Hiểu các nguyên tắc cốt lõi của Prompt Engineering, nắm vững tinh túy của "Context is King"
- ✅ Vận dụng khung cấu trúc (S.C.A.F.F., R.G.C.) để viết prompt rõ ràng, hiệu quả
- ✅ Nắm vững các kỹ thuật cốt lõi như Zero-shot, Few-shot, Chain of Thought, Tree of Thoughts
- ✅ Chuyển hóa tư duy sản phẩm của Chương 2 (chân dung người dùng, bản đồ hành trình, ba câu hỏi linh hồn) thành PRD mà AI có thể thực thi
- ✅ Học cách đối thoại lặp lại nhiều vòng với AI, từng bước tiếp cận kết quả lý tưởng
- ✅ Nhận diện bốn loại ảo giác của AI (ảo giác gói, ảo giác API, ảo giác logic, ảo giác phiên bản), nắm vững kỹ thuật xác minh
- ✅ Hiểu phương pháp cấu hình dự án của các AI IDE chủ đạo (Cursor/Windsurf/Claude Code, v.v.)

## Điểm sáng chương này

Chương này bao gồm nhiều nội dung thực dụng, giúp bạn ít đi đường vòng:

- 📦 **Cảnh báo an toàn 2024-2025**: Nhận diện tấn công Slopsquatting —— nghiên cứu cho thấy khoảng 20% gói AI đề xuất có thể không tồn tại, kẻ tấn công đã lợi dụng lỗ hổng này để tấn công chuỗi cung ứng
- 🛠️ **Bảng đối chiếu cấu hình 9 loại AI IDE**: Tổng hợp phương pháp cấu hình ngữ cảnh của các công cụ như Cursor, Windsurf, Claude Code, GitHub Copilot, Trae
- 📋 **Mẫu Prompt có thể sao chép trực tiếp**: Các kịch bản tạo dự án, sửa code, giải quyết vấn đề có thể dùng ngay
- ⚖️ **So sánh Prompt tệ vs Prompt tốt**: Hiển thị trực quan ảnh hưởng của cách diễn đạt đối với chất lượng đầu ra của AI

## Ví dụ xuyên suốt chương này

Chương này sẽ tiếp nối dự án "Danh sách việc cần làm" của Tiểu Lý ở Chương 2, diễn giải cách:
- Chuyển hóa phân tích JTBD và ba câu hỏi linh hồn của Chương 2 thành PRD mà AI có thể thực thi
- Dùng khung cấu trúc viết Prompt hoàn chỉnh đầu tiên
- Thông qua đối thoại lặp lại từng bước hoàn thiện chức năng

Đồng thời, cũng sẽ sử dụng các kịch bản điển hình như "Trang đăng nhập", "Chuyển đổi code", "Lựa chọn kỹ thuật" để diễn giải các kỹ thuật prompt khác nhau.

## Đặc sắc giảng dạy chương này

Chương này sử dụng nhiều **phương pháp giảng dạy so sánh** —— hiển thị "Prompt tệ" và "Prompt tốt" cho cùng một nhiệm vụ, để bạn thấy trực quan ảnh hưởng của cách diễn đạt đến chất lượng đầu ra của AI.

Ví dụ:
- ❌ "Giúp tôi làm một trang đăng nhập"
- ✅ Phiên bản khung S.C.A.F.F. hoàn chỉnh bao gồm bối cảnh dự án, stack kỹ thuật, yêu cầu chức năng, ràng buộc giao diện (xem tiết 3.2)

**Tại sao dạy như vậy**: Nghiên cứu cho thấy, học tập so sánh giúp xây dựng mô hình tâm trí đúng đắn nhanh hơn. Thấy "tệ" ở đâu, mới hiểu "tốt" ở chỗ nào.

## Gắn kết với Chương 2

Chương này và Chương 2 có mối quan hệ "Suy nghĩ" và "Diễn đạt". Bảng dưới đây hiển thị cách chuyển hóa thành quả Chương 2 thành kỹ năng Chương 3:

| Thành quả Chương 2 | Vị trí ứng dụng Chương 3 | Chuyển hóa thế nào |
|-----------|--------------|---------|
| Ba câu hỏi linh hồn (Người dùng là ai, nỗi đau ở đâu, tại sao chọn bạn) | 3.4 Mẫu PRD | Điền trực tiếp vào phần "Mục tiêu sản phẩm" |
| Tư duy phép trừ (Ưu tiên P0/P1/P2) | 3.4 Phát triển phân giai đoạn | Dùng độ ưu tiên dẫn dắt AI thực hiện từng bước |
| Chân dung người dùng | 3.2 Phần Context của khung | Giúp AI hiểu người dùng mục tiêu |
| Bản đồ hành trình người dùng | 3.4 Luồng người dùng | Điền bản rút gọn vào PRD |
| Prompt kể chuyện | 3.2 Lựa chọn khung | Trong một số trường hợp hiệu quả hơn cấu trúc hóa |
| Danh sách không làm | 3.2 Ràng buộc Constraints | Nói rõ cho AI biết không làm cái gì |

## Ranh giới chương này

Chương này tập trung vào **phương pháp luận chung**, không ràng buộc với bất kỳ công cụ cụ thể nào. Về cấu hình cụ thể của AI IDE:
- Bản cơ bản chỉ giới thiệu khái niệm cốt lõi và tác dụng của file cấu hình
- Hướng dẫn cấu hình chi tiết vui lòng tham khảo bản nâng cao hoặc tài liệu chính thức của từng công cụ

Lý do thiết kế như vậy: Công cụ sẽ thay đổi, phương pháp luận thì không. Nắm vững tư duy của chương này, bạn có thể chuyển giao sang bất kỳ công cụ lập trình AI nào.

## Xem trước cấu trúc chương này

| Tiểu tiết | Câu hỏi cốt lõi | Bạn sẽ nhận được |
|-----|---------|---------|
| 3.1 Cơ sở Prompt Engineering | AI cần biết gì? | Mô hình ngữ cảnh ba lớp |
| 3.2 Khung cấu trúc | Nói sao để AI hiểu? | Khung S.C.A.F.F. và R.G.C. |
| 3.3 Kỹ thuật Prompt nâng cao | Trường hợp nào dùng kỹ thuật gì? | Hướng dẫn chọn Zero-shot/Few-shot/CoT/ToT |
| 3.4 Viết PRD đầu tiên | Làm sao tích hợp suy nghĩ Chương 2? | Mẫu PRD có thể điền vào |
| 3.5 Đối thoại lặp lại | Một lần không đủ thì sao? | Kỹ thuật vòng lặp phản hồi - sửa chữa |
| 3.6 Khi AI không nghe lời | Đầu ra có vấn đề thì sao? | Nhận diện ảo giác + Danh sách xác minh |
| 3.7 Tổng kết và diễn tập | Ứng dụng tổng hợp thế nào? | Quy trình làm việc hoàn chỉnh + Bài tập thực chiến |
