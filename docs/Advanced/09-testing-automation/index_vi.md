---
title: "Chương 9: Quy trình kiểm thử chức năng và kịch bản tự động hóa"
---

# Chương 9: Quy trình kiểm thử chức năng và kịch bản tự động hóa

## Lời tựa

Tính năng ngày càng nhiều, bạn bắt đầu gặp phải hiện tượng đau đầu: **"Đập chuột chũi"**. Bạn vừa sửa xong Bug ở "Trang đăng nhập", kết quả "Trang đăng ký" lại không mở được; bạn tối ưu style trang chủ, kết quả nút giỏ hàng lại bấm không ăn.

Sư phụ bảo, muốn ngăn chặn thảm án "rút dây động rừng" kiểu này, phải nắm bắt cả hai tay: **Đầu tiên là "Nội công": Quy hoạch hợp lý cấu trúc code và thư mục**. Đừng chất đống logic vào một file, mà phải tách biệt các chức năng thành các module độc lập (ví dụ `components/` chứa khối component, `lib/` chứa hàm tiện ích, `app/` chứa trang). Cấu trúc rõ ràng rồi, sửa module A tự nhiên sẽ khó làm hỏng lây sang module B. **Tiếp theo là "Ngoại công": Kiểm thử hồi quy (Regression Testing)**. Mỗi lần sửa code, bạn đều phải test lại tất cả các tính năng từng chạy được trước đó, đảm bảo không bị code mới "làm hỏng". Nhưng dựa vào sức người ngồi bấm bấm trên web, vừa mệt vừa dễ sót.

**Tuy nhiên, sư phụ cũng đưa ra lời khuyên thực tế:** Tự động hóa tuy sướng, nhưng không bắt buộc. Nếu dự án của bạn chỉ có 2 trang, hoặc đang ở giai đoạn sửa nhu cầu điên cuồng, thì cứ **trực tiếp dùng tay bấm** lại kinh tế hơn. Kiểm thử tự động là để giải quyết lao động **quy mô lớn, lặp lại**, đừng vì tự động hóa mà tự động hóa, rơi vào cái bẫy viết kịch bản test còn lâu hơn viết code.

::: tip Tỷ lệ đầu tư / thu hoạch của kiểm thử tự động
**Khi nào cần kiểm thử tự động?**

✅ **Nên tự động hóa**:

- Dự án có 5+ trang
- Quy trình nghiệp vụ cốt lõi vượt quá 3 bước
- Quy mô team trên 2 người
- Cần sửa code thường xuyên
- Đã từng gặp tình trạng "Sửa Bug A đẻ ra Bug B"

❌ **Khoan hẵng tự động hóa**:

- Giai đoạn kiểm chứng Prototype (nhu cầu thay đổi liên tục)
- Dự án dùng một lần (làm xong không bảo trì nữa)
- Trang quá đơn giản (như trang tĩnh)

**Ghi nhớ**: Test là để nâng cao sự tự tin, chứ không phải để hoàn thành nhiệm vụ
:::

### Playwright

Sư phụ giới thiệu **Playwright**. Bạn có thể hiểu nó là **công cụ điều khiển trình duyệt tự động**. Nó sở hữu một nhân trình duyệt thực thụ, có thể dùng tốc độ nhanh gấp 100 lần con người để mô phỏng thao tác click chuột, gõ phím thậm chí upload file của bạn. Quan trọng hơn, nó **không biết mệt**. Dù là 3 giờ sáng, chỉ cần bạn ra lệnh, nó có thể chạy lại quy trình "Đăng nhập - Đặt hàng - Thanh toán" 100 lần trong vài giây, mà tuyệt đối không nhìn nhầm.

Tại sao chọn Playwright chứ không phải framework test khác? Đầu tiên nó đa trình duyệt (hỗ trợ cả Chrome, Firefox, Safari), thứ hai nhanh và ổn định (hỗ trợ chạy song song, tự động đợi phần tử xuất hiện), quan trọng nhất là thân thiện với AI —— có thể dùng `npx playwright codegen` ghi lại thao tác thủ công, tự động sinh code test. Khái niệm cốt lõi của Playwright rất đơn giản: Page đại diện trang trình duyệt, Locator dùng để định vị phần tử, Assertion dùng để khẳng định phán đoán. Lý thuyết tháp kiểm thử khuyên dùng 60% Unit Test, 30% Integration Test, 10% E2E Test. E2E Test tuy chiếm tỷ trọng nhỏ, nhưng bao phủ quy trình nghiệp vụ cốt lõi (đăng nhập, đăng ký, thanh toán), giá trị cao nhất. AI còn có thể giúp bạn tối ưu test case, thêm trường hợp biên và xử lý lỗi. Giá trị của test không phải phát hiện Bug, mà là ngăn chặn Bug hồi quy —— sửa Bug A không sinh ra Bug B.

Trong quá trình VibeCoding, viết kịch bản test không còn là đặc quyền của kỹ sư kiểm thử cao cấp, trong công cụ lập trình AI chín muồi, bạn chỉ cần **trích dẫn** file code nghiệp vụ của bạn trong khung chat (thường là gõ `@` chọn file, hoặc dán đường dẫn file, thậm chí kéo thả file vào khung chat). Tuy AI hiện tại rất thông minh, có thể tự lục lọi tìm code trong cả dự án, nhưng nếu bạn có thể **chỉ định đường dẫn file thủ công**, phản ứng của AI sẽ nhanh hơn nhiều, viết test cũng chuẩn hơn.

::: info Lộ trình học chương này
**Phần cơ bản** (Hiểu lý thuyết test):

1. Lý thuyết tháp kiểm thử → Hiểu phân tầng kiểm thử
2. Chi tiết các loại kiểm thử → Biết khi nào dùng loại nào
3. Khái niệm Mock → Học cách cách ly phụ thuộc bên ngoài

**Phần thực hành** (Làm quen Playwright): 4. Cài đặt và cấu hình Playwright → Dựng môi trường test 5. Hướng dẫn toàn diện Playwright → Nắm vững API cốt lõi 6. Thực chiến UI Test → Viết test thực tế 7. Thực chiến API Test → Test giao diện Backend

**Phần nâng cao** (Quy trình làm việc tự động): 8. Chi tiết quy trình TDD → Viết test trước viết code sau 9. Hooks Automation Test → Tự động chạy test trước khi commit 10. Checkpoint và Revert → Quản lý phiên bản code an toàn 11. Chạy test và Debug → Sửa test lỗi hiệu quả
:::

::: tip Hệ thống kiểm thử mới thời đại lập trình AI
**Quy trình test truyền thống** (Tốn thời gian):

```
Tự viết code test (1 tiếng)
→ Chạy test
→ Sửa lỗi
→ Lặp lại
```

**Quy trình test hỗ trợ bởi AI** (Nhanh):

```
Để AI sinh test (10 giây)
→ Chạy test
→ Để AI sửa lỗi (10 giây)
→ Hoàn thành
```

**Chuyển đổi then chốt**:

- Từ "Viết test thế nào" → Chuyển sang "Thiết kế test gì"
- Từ "Viết thủ công" → Chuyển sang "Rà soát và điều chỉnh"
- Từ "Độ phủ test" → Chuyển sang "Giá trị test"

**Vai trò của bạn**: Kiến trúc sư kiểm thử, chứ không phải thợ viết code test
:::

### UI Test

Đối với kiểm thử giao diện người dùng (UI), bạn chỉ cần trích dẫn `app/login/page.tsx` (giả sử đây là trang đăng nhập của bạn) vào khung Chat, rồi ra lệnh: "**Đọc file này, viết cho tôi một kịch bản test Playwright. Ngữ cảnh test bao gồm: 1. Nhập sai mật khẩu phải báo lỗi; 2. Nhập đúng mật khẩu phải chuyển hướng về trang chủ.**" AI sẽ đọc ngay nội dung file bạn chỉ định, phân tích cấu trúc component, sinh ra code chứa đầy đủ quy trình định hướng, thao tác, xác thực một cách chính xác.

### API Test

Ngoài test giao diện, sư phụ nhắc bạn đừng quên test giao diện Backend (API). Đôi khi trang web báo lỗi không phải do nút hỏng, mà do API backend sập. Playwright không chỉ mô phỏng được trình duyệt, mà còn có thể gửi HTTP request trực tiếp. Bạn không cần đi viết test cho từng API một, mà trực tiếp trích dẫn cả thư mục `app/api`, ra một chỉ thị vĩ mô cho AI:

> **“Đọc tất cả các file route trong thư mục `app/api`, hiểu logic nghiệp vụ của từng API. Sau đó sinh kịch bản test tương ứng cho mỗi API, bao phủ ngữ cảnh request bình thường (200 OK) và các ngữ cảnh request lỗi thường gặp (400/500).”**

AI sẽ nhanh chóng duyệt qua đường dẫn bạn chỉ định, phân tích ra bạn có mười mấy API như đăng ký, đăng nhập, lấy danh sách bài viết..., và tự động sinh ra một bộ code test chặt chẽ cho chúng. Cách này tốc độ cực nhanh, giúp bạn nhanh chóng định vị xem rốt cuộc là vấn đề logic hiển thị Frontend hay vấn đề xử lý dữ liệu Backend.

### Chạy Test

Cuối cùng, bạn học được cách chạy `npx playwright test`. Nhìn từng dòng **PASS** màu xanh chạy vùn vụt trong terminal, cảm giác an toàn đó chưa từng có. Điều này có nghĩa là code của bạn **đáng tin cậy** về mặt logic. Sư phụ còn dạy bạn mở **chế độ trực quan (UI Mode)** của Playwright. Nhìn cửa sổ trình duyệt tự động trên màn hình nháy liên tục, tự động điền form, bấm nút, lần đầu tiên bạn trải nghiệm cảm giác sướng rơn của phát triển công nghiệp hóa. Bạn đảm bảo được rằng trước khi đối mặt với người dùng thật, những Bug logic cấp thấp kia đã bị tiêu diệt từ trong trứng nước.

### Test Driven Development (TDD)

Tuy nhiên, sư phụ bảo bạn, còn có cách chơi cao cấp hơn. Bạn hiện tại là viết code trước, rồi bù test sau, cái này gọi là phiên bản ngược của "Phát triển hướng kiểm thử (TDD)". Trong thời đại lập trình AI, **TDD thực sự là viết test trước, rồi mới viết code**. Tại sao làm thế? Khi bạn cho AI một mục tiêu test rõ ràng, biểu hiện của nó sẽ được nâng cao đáng kể.

Sư phụ giới thiệu cho bạn quy trình làm việc **TDD**:

1. **Viết test trước**: Viết test dựa trên cặp đầu vào/đầu ra kỳ vọng, nói rõ với AI bạn đang tiến hành TDD, tránh việc nó tạo ra các hiện thực hóa giả (mock).
2. **Chạy test, xác nhận thất bại**: Ở giai đoạn này nói rõ với AI đừng viết bất kỳ code hiện thực hóa nào.
3. **Commit test**: Khi bạn hài lòng với bài test, bảo AI commit test.
4. **Viết code, cho đến khi test thông qua**: Bảo AI viết code để thông qua bài test, chỉ thị nó không được sửa code test. Thường cần vài lần lặp.
5. **Commit code**: Khi bạn hài lòng với thay đổi, bảo AI commit code.

Bạn thử một lần, phát hiện quá trình viết test thực ra chính là đang "thiết kế interface". Khi bạn viết test, bạn sẽ suy nghĩ "phương thức này nên nhận tham số gì, trả về kết quả gì", quá trình suy nghĩ này quan trọng hơn việc trực tiếp viết code. Tuy lúc đầu cảm thấy chậm, nhưng rất nhanh phát hiện số lần phải làm lại giảm hẳn. Quan trọng hơn, bạn phát hiện test thực ra là "công cụ thiết kế" tốt nhất, nó ép bạn phải nghĩ rõ interface và logic trước khi viết code.

Sư phụ bảo, sự tự động hóa này còn có thể tiến thêm bước nữa —— thông qua cấu hình **Hooks**, mỗi khi AI sửa code xong, tự động chạy test liên quan. Bạn không cần gõ lệnh thủ công, toàn bộ quy trình test sẽ tự động hoàn thành.

### Hooks Automation

Sư phụ báo trước: "Cậu có thể cấu hình Git Hooks, để mỗi lần trước khi commit code tự động chạy test. Như vậy có thể sớm phát hiện vấn đề, tránh việc đẩy code có bug vào kho."
