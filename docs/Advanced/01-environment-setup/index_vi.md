---
title: "Chương 1: Xây dựng môi trường và Cơ sở chạy mã"
---

![01-environment-setup_index.png](../../public/images/Advanced/01-environment-setup_index.png)

# Chương 1: Xây dựng môi trường và Cơ sở chạy mã

## Lời mở đầu

Bạn có một chiếc máy tính mới, bên trong sạch sẽ tinh tươm, ngoài trình duyệt ra thì chẳng có gì cả. Bạn không biết viết code, nhưng bạn thấy dạo này AI rất hot, trong lòng có một ý tưởng App tuyệt vời, định lên mạng chỉ huy AI giúp bạn làm một cái Demo.

### Định dạng code

Khúc mắc đầu tiên bạn gặp phải là **định dạng code mà AI đưa ra**. Đôi khi, AI sẽ đưa trực tiếp cho bạn một đoạn code dài, bảo bạn lưu thành `index.html`. Bạn làm theo, tạo file mới, dán, lưu, nhấp đúp mở ra, trình duyệt thực sự hiện lên một trang web biết chuyển động. Bạn rất vui, tưởng lập trình cũng chỉ có thế. Loại file này thường nhét cả cấu trúc (HTML), kiểu dáng (CSS) và logic (JavaScript) vào chung một chỗ, thích hợp làm demo đơn giản.

Nhưng khi bạn yêu cầu chức năng phức tạp hơn, AI bắt đầu đưa cho bạn code có đuôi `.ts` hoặc `.tsx`, còn nhắc đến những từ như `import`, `React`. Bạn cũng lưu file như trước, nhấp đúp mở ra, nhưng phát hiện không mở được, hoặc hiển thị một đống code không hiểu gì. Bạn ngơ ngác, sao code không chạy được nữa?

Bạn khó hiểu hỏi: "Đã có AI giúp tôi viết code rồi, sao còn phải học mấy cái này?"

Người thầy già nói: "AI có thể viết code, nhưng 'làm sao để nó chạy được' thì cần bạn hiểu. Giống như điều hướng vậy: có thể chỉ đường cho bạn, nhưng trước tiên bạn phải biết lái xe. Xây dựng môi trường không phải là rào cản, mà là bước đầu tiên để bạn cộng tác với AI."

→ **[1.1 Sự tiến hóa của định dạng code](./01-code-formats_vi.md)** sẽ đưa bạn đi từ HTML tệp đơn đến phát triển mô-đun hóa hiện đại.

---

::: details 🎮 Bấm để trải nghiệm: Demo tương tác
Dưới đây là một demo tương tác tinh tế, bao gồm chức năng bộ đếm, đồng hồ bấm giờ và chuyển đổi cơ số:

<InteractiveDemo />

> 💡 **Đây chính là trải nghiệm phát triển Frontend hiện đại**: Giao diện tinh tế, hoạt hình mượt mà, tương tác phong phú. Sử dụng phím tắt ↑↓ để điều chỉnh giá trị, R để đặt lại, H để chuyển đổi lịch sử.
> :::

### TypeScript và Node.js

Người thầy già bảo bạn, đó là vì phát triển hiện đại sử dụng **TypeScript** (gọi tắt là TS), nó chặt chẽ hơn JavaScript thông thường, phù hợp để làm dự án lớn. Tuy nhiên, trình duyệt không hiểu TS, nó cần một "phiên dịch viên" (trình biên dịch) để dịch TS sang JavaScript mà trình duyệt hiểu được. Trình biên dịch này cũng như các công cụ build cần môi trường **Node.js** để chạy. Nếu không cài Node.js, máy tính của bạn sẽ không thể chạy các công cụ build code hiện đại này.

→ **[1.2 Khái niệm Tech Stack](./02-tech-stack_vi.md)** và **[1.3 Cơ bản về Trình duyệt và Server](./03-browser-server_vi.md)** sẽ giúp bạn xây dựng những nhận thức này.

### Quản lý phiên bản nvm

Bạn hào hứng đi tải Node.js, nhưng người thầy già cũng giống như trang chủ Nodejs, ngăn bạn lại. Ông ấy khuyên bạn cài **nvm** (Node Version Manager). Vì Node.js cập nhật thường xuyên, các dự án khác nhau có thể cần phiên bản khác nhau, nvm giúp bạn chuyển đổi phiên bản dễ dàng mà không cần gỡ đi cài lại nhiều lần. Bạn cài đặt phiên bản LTS (Hỗ trợ dài hạn, ổn định) mới nhất thông qua nvm, và dưới sự giới thiệu của người thầy già, bạn đổi sang **nguồn mirror trong nước** (để giải quyết vấn đề tải chậm), cuối cùng cũng sở hữu cái gọi là môi trường chạy.

→ **[1.4 Nhập môn Terminal](./04-terminal-basics_vi.md)** sẽ dạy bạn nắm vững các thao tác dòng lệnh cơ bản, **[1.5 Môi trường Node.js và Quản lý gói](./05-nodejs-and-pnpm_vi.md)** sẽ đưa bạn hoàn thành các cấu hình này.

---

::: details 🔄 Bấm để trải nghiệm: Trình quản lý phiên bản Node
Thử chuyển đổi các phiên bản Node.js khác nhau, trải nghiệm sự tiện lợi của nvm:

<NodeVersionManager />

> 💡 **Bài tập**: Bấm vào các phiên bản khác nhau để chuyển đổi, quan sát sự thay đổi của phiên bản hiện tại. Thử cài đặt một phiên bản chưa cài đặt.
>
> 🎯 **Khái niệm cốt lõi**: nvm giúp bạn quản lý nhiều phiên bản Node.js trên cùng một máy tính, các dự án khác nhau có thể sử dụng phiên bản khác nhau mà không xung đột.
> :::

### Terminal (Cửa sổ lệnh)

Tiếp theo, bạn tiếp xúc với **Terminal** (như CMD, PowerShell của Windows hoặc Terminal của Mac). Nó không phải công cụ hacker bí ẩn gì cả, mà là một cách thức trực tiếp đối thoại với hệ điều hành thông qua chỉ thị văn bản. So với dùng chuột bấm biểu tượng, terminal có thể thực hiện các nhiệm vụ phức tạp chính xác hơn, nhanh hơn.

Khoảnh khắc dễ sụp đổ nhất của người mới, chính là gõ xong lệnh enter thì thấy `command not found`. Lỗi này thực ra có tư duy bài bản để kiểm tra: kiểm tra chính tả lệnh trước, sau đó xác nhận công cụ đã cài chưa, rồi kiểm tra thư mục hiện tại có đúng không. Xây dựng tư duy kiểm tra này quan trọng hơn ghi nhớ thông tin lỗi cụ thể.

---

::: details 🖥️ Bấm để trải nghiệm: Terminal Pro
Thử nhập lệnh trong trình giả lập terminal chuyên nghiệp bên dưới:

<TerminalPro />

> 💡 **Bài tập**: Thử nhập `ls` để xem tệp tin, sau đó nhập `cd Documents` để chuyển thư mục, rồi dùng `pwd` để xem đường dẫn hiện tại.
>
> 🎨 **Giải thích màu sắc**: Xanh dương=Thư mục, Xanh lá=Tệp thực thi, Xanh lơ=Liên kết, Trắng=Tệp thường
>
> ⌨️ **Phím tắt**: `Tab` Tự động hoàn thành | `↑↓` Lệnh lịch sử | `Ctrl+L` Xóa màn hình | `Ctrl+C` Hủy bỏ
> :::

### Gói mã nguồn mở

Có môi trường rồi, người thầy già bảo bạn, phát triển phần mềm hiện đại rất ít khi viết từ con số 0. Giống như xây nhà không cần tự nung gạch, bạn có thể trực tiếp sử dụng code mà lập trình viên toàn thế giới đóng góp —— tức là **gói mã nguồn mở**. React giúp bạn lo giao diện, Axios giúp bạn lo yêu cầu mạng, Day.js giúp bạn xử lý thời gian, Zod giúp bạn xác thực dữ liệu... Những gói code có sẵn này giúp bạn tập trung vào logic nghiệp vụ, thay vì lặp lại việc phát minh lại bánh xe.

---

::: details 📦 Bấm để trải nghiệm: Hệ sinh thái gói nguồn mở
Khám phá các gói nguồn mở thường dùng trong hệ sinh thái npm:

<PackageEcosystem />

> 💡 **Bài tập**: Bấm phân loại để lọc các loại gói khác nhau, bấm vào thẻ để xem chi tiết và mô phỏng cài đặt.
>
> 🎯 **Khái niệm cốt lõi**: npm sở hữu hơn 2 triệu gói nguồn mở, bao phủ gần như mọi nhu cầu phát triển, tăng tốc đáng kể hiệu quả phát triển.
> :::

### Trình quản lý gói pnpm

Vậy, làm sao để cài đặt gói code người khác viết sẵn? Bạn cần một **trình quản lý gói**. Node.js có sẵn một cái gọi là **npm**, nhưng nó cài đặt dependency bằng cách sao chép, chiếm dụng lượng lớn dung lượng đĩa. Hiện nay khuyến nghị dùng **pnpm** hơn —— thông qua kỹ thuật hard link và symbolic link, có thể tiết kiệm khoảng 50%-70% dung lượng đĩa, và tốc độ cài đặt nhanh hơn đáng kể.

Trong phát triển AI, bạn sẽ thường xuyên tạo dự án mới để thử các hướng đi khác nhau, pnpm giúp bạn tiết kiệm lượng lớn thời gian chờ đợi và không gian lưu trữ.

→ **[1.5 Môi trường Node.js và Quản lý gói](./05-nodejs-and-pnpm_vi.md)** sẽ giảng giải chi tiết cách cài đặt cấu hình nvm và pnpm.

---

::: details 📦 Bấm để trải nghiệm: Quá trình cài đặt pnpm
Xem pnpm cài đặt dependency dự án như thế nào:

<TypeScriptCompiler />

> 💡 **Bài tập**: Bấm nút "Cài đặt", quan sát 4 bước cài đặt dependency của pnpm.
>
> 🎯 **Khái niệm cốt lõi**: pnpm chia sẻ dependency thông qua kỹ thuật hard link, tiết kiệm 50%-70% dung lượng đĩa so với npm.
> :::

### Mô hình và Công cụ

Cài xong môi trường, bạn cầm trong tay danh sách công cụ khổng lồ, đối mặt với đủ loại mô hình, trình biên tập và công cụ CLI, bạn hoàn toàn chóng mặt.

Qua sự giới thiệu của người thầy già, cuối cùng bạn cũng hiểu: **Mô hình quyết định tốc độ và giới hạn năng lực code, công cụ quyết định phương thức và hiệu suất hiện thực hóa code.**

Nói về mô hình, có thể bạn sẽ thấy Claude năng lực mạnh nhất thì cứ dùng nó hết đi. Nhưng người thầy già nhắc bạn: **Mô hình nội địa rẻ và truy cập nhanh**. Ví dụ GLM 4.7, tổng lượng dùng mỗi tháng lên đến hàng tỷ tokens, tính ra cực kỳ tối ưu chi phí. Ý thức về chi phí này rất quan trọng trong phát triển AI Native, nếu không khi quy mô tăng lên hóa đơn sẽ làm bạn sốc.

→ **[1.6 Mô hình và Công cụ](./06-models-and-tools_vi.md)** sẽ giới thiệu chi tiết cách lựa chọn và cấu hình các loại công cụ phát triển.

### Đặt tên thư mục

Bây giờ, bạn đã sở hữu môi trường phát triển hiện đại hoàn chỉnh, có thể xử lý bất kỳ code TS nào do AI sinh ra. Người thầy già đặc biệt dặn dò: **Khi tạo dự án mới, nhất định phải tạo một thư mục không chứa tiếng Trung (tiếng Việt), dấu cách**. Đây là vì nhiều công cụ phát triển tầng dưới hỗ trợ không tốt cho ký tự phi Latin, đường dẫn tiếng Trung/Việt thường là nguồn gốc của đủ loại báo lỗi kỳ lạ.

→ **[1.7 Tạo dự án](./07-creating-project_vi.md)** sẽ dạy bạn từ quy tắc đặt tên thư mục đến tạo mẫu dự án.

---

::: details 📁 Bấm để trải nghiệm: Cấu trúc tệp dự án
Khám phá cấu trúc tệp của một dự án điển hình, tìm hiểu quy tắc đặt tên:

<FileSystemTree />

> 💡 **Bài tập**: Bấm thư mục để mở rộng/thu gọn, xem cấu trúc dự án. Chú ý quan sát gợi ý quy tắc đặt tên ở dưới đáy.
>
> ⚠️ **Nhắc nhở quan trọng**: Thư mục và tên tệp nên tránh sử dụng tiếng Trung/Việt và dấu cách, để phòng ngừa công cụ báo lỗi.
> :::

### Localhost và Cổng

Code đều ở local rồi, nhưng bạn hoàn toàn không biết làm sao để chạy nó lên. Bạn thăm dò gửi file cho AI, hỏi nó: "Tôi phải khởi động dự án này thế nào?" AI bảo bạn, cần chạy `pnpm install` cài đặt dependency trước, sau đó chạy `pnpm dev` khởi động server phát triển. Bạn làm theo, màn hình cuối cùng dừng lại ở `http://localhost:3000`.

Bạn nhìn chằm chằm địa chỉ này, người thầy già bổ túc cho bạn một bài cơ bản về mạng: **Localhost** cũng chính là **127.0.0.1**, trong thế giới mạng, nó đại diện cho "máy tính của chính bạn". Nếu ví máy tính của bạn là một tòa nhà, IP là địa chỉ tòa nhà, thì cổng chính là **số phòng** cụ thể. Ứng dụng web của bạn lúc này đang ngồi trong căn phòng số 3000, đợi trình duyệt của bạn đến gõ cửa.

Bạn kích động bấm vào liên kết này, trang web thực sự hiện ra! Người thầy già thuận miệng nói thêm một câu, tuy công cụ phát triển hiện nay đều rất thông minh —— nếu bạn mở thêm một dự án, thường chúng sẽ tự động chuyển sang phòng 3001 —— nhưng trong **môi trường sản xuất**, quy tắc rất nghiêm ngặt: **Một cổng cùng lúc chỉ có thể chứa một chương trình**. Nếu bạn thấy báo lỗi đỏ lòm `EADDRINUSE`, đừng hoảng, bảo AI đổi cho bạn một cổng khác là được.

→ **[1.8 Localhost và Cổng](./08-localhost-and-ports_vi.md)** sẽ giảng giải chi tiết về những kiến thức mạng cơ bản này.

---

::: details 🌐 Bấm để trải nghiệm: Trực quan hóa Localhost và Cổng
Chọn một cổng khả dụng, trải nghiệm quá trình kết nối localhost:

<NetworkPorts />

> 💡 **Bài tập**: Bấm vào cổng màu xanh lá (khả dụng), sau đó bấm nút "Kết nối". Thử bấm vào cổng màu đỏ (bị chiếm dụng) xem chuyện gì xảy ra.
>
> 🎯 **Khái niệm cốt lõi**: localhost (127.0.0.1) đại diện cho máy tính của bạn, số cổng là "số phòng" mà ứng dụng đang chạy.
> :::

---

### Bắt tay thực hành

Sau khi cài xong môi trường theo bài 1.5, tạo một thư mục tiếng Anh mới, mở công cụ AI lên và bảo nó: "Giúp tôi tạo một dự án Next.js tại đây", sau đó làm theo hướng dẫn của nó để thực thi lệnh, cuối cùng mở `localhost:3000` trên trình duyệt —— bạn đã chính thức bước vào thế giới lập trình AI!
