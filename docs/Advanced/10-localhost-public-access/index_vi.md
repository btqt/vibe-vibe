---
title: "Chương 10: Localhost và Truy cập công khai"
---

# Chương 10: Localhost và Truy cập công khai

## Lời tựa

Bạn nhìn trang web hoàn hảo trên máy tính, muốn cho bạn bè trầm trồ một chút. Bạn tự tin copy địa chỉ `http://localhost:3000` trên thanh địa chỉ trình duyệt gửi cho bạn bè qua Zalo. Một phút sau, bạn bè nhắn lại một dấu chấm hỏi: "Không mở được, sao thế?"

Khoảnh khắc đó, bạn đỏ mặt tía tai. Cuối cùng bạn cũng hiểu được sự khác biệt giữa môi trường local và mạng Internet.

### Các tầng mạng

Để giải quyết vấn đề này, Sư phụ từ góc độ **khả năng truy cập của địa chỉ IP**, phân chia cho bạn ba tầng mạng:

- **Local Loopback (Localhost / 127.0.0.1)**: `localhost` trong mạng máy tính được gọi là **địa chỉ loopback (hoàn ngược)**, nó mãi mãi trỏ về **chính thiết bị phát ra request**. Khi bạn gửi đường link này cho bạn bè, trình duyệt của họ sẽ thử truy cập **máy tính của chính họ**. Vì máy tính của họ không chạy dịch vụ Next.js của bạn, nên trình duyệt sẽ báo lỗi "Kết nối bị từ chối" ngay lập tức. Đây là một môi trường đơn máy cách ly vật lý.
- **Mạng cục bộ (LAN / Intranet)**: Đây là mạng nội bộ do router của bạn dựng lên. Tuy mạng Internet bên ngoài không thể truy cập trực tiếp, nhưng các thiết bị kết nối vào cùng một WiFi/dây mạng (như điện thoại, máy tính bảng) là thông nhau. Một khâu quan trọng của phát triển Fullstack là debug trên máy thật. Bạn không cần mỗi lần đều phải deploy lên mạng công khai, chỉ cần cho điện thoại truy cập IP mạng cục bộ của máy tính, là có thể lập tức test thao tác cảm ứng và bố cục Responsive trên máy thật.
  - **Xem IP**:
    - Windows: Nhập `ipconfig` trong terminal
    - macOS: Nhập `ifconfig` trong terminal hoặc xem trong System Settings
    - Linux: Nhập `ip addr` hoặc `ip a` (khuyên dùng), hoặc `ifconfig` (cần cài net-tools)
      Tìm địa chỉ có định dạng `192.168.x.x` hoặc `10.x.x.x`.
  - **Test truy cập**: Nhập `http://192.168.x.x:3000` vào trình duyệt điện thoại.
  - **Khắc phục sự cố**: Nếu không truy cập được, 90% trường hợp là do tường lửa máy tính chặn kết nối đến (inbound connection). Tạm thời tắt tường lửa hoặc cho phép Node.js giao tiếp thường sẽ giải quyết được vấn đề.
- **Mạng diện rộng (WAN / Internet)**: Đây mới là Internet thực sự. Muốn cho người dùng ở môi trường mạng khác nhau (ví dụ bạn bè ở thành phố bên cạnh) truy cập trang web của bạn, bạn cần một IP công khai. Thông thường, việc này đòi hỏi bạn deploy code lên Cloud Server hoặc nền tảng Hosting có IP công khai.

### Chia sẻ

Bạn nhận ra, Localhost chỉ là điểm khởi đầu của phát triển. Muốn phá vỡ sự cách ly vật lý, để người khác nhìn thấy hoặc tham gia dự án, bạn cần thiết lập các con đường khác nhau tùy theo đối tượng mục tiêu:

**Kịch bản 1: Hướng tới người dùng sử dụng (Deployment)** Nếu bạn muốn bạn bè hoặc người dùng trực tiếp **sử dụng** sản phẩm của bạn, bạn cần tiến hành **Triển khai ứng dụng (Deploy)**. Thông qua việc đóng gói code (Build) và phát hành lên Vercel, Tencent Cloud EdgeOne hoặc Cloud Server truyền thống, bạn sẽ có được một tên miền công khai (như `https://my-app.com`). Người dùng thông qua tên miền là truy cập được ứng dụng, không cần quan tâm code bên dưới.

**Kịch bản 2: Hướng tới cộng tác viên phát triển (Git)** Nếu bạn muốn bạn bè **tham gia phát triển**, hoặc nhờ cao thủ Review code giúp, bạn cần tiến hành **Đồng bộ code**. Thông qua việc đẩy mã nguồn lên nền tảng quản lý code như GitHub, Gitee, người cộng tác có thể kéo (Pull) code về máy tính của họ. Lúc này, họ chạy dự án trên môi trường Localhost của chính họ, từ đó hiện thực hóa việc cộng tác phát triển đa thiết bị.

**Kịch bản 3: Demo và Test nhanh** Trong giai đoạn phát triển, có thể bạn cần cho bạn bè ở xa xem nhanh hiệu quả, nhưng lại không muốn deploy chính thức, lúc này công cụ **Xuyên ngầm (Tunneling)** sẽ phát huy tác dụng.

Sư phụ bảo, bản chất của xuyên ngầm là đào một đường hầm giữa máy tính local của bạn và mạng công khai. Người dùng bên ngoài truy cập một địa chỉ tạm thời, lưu lượng sẽ được chuyển tiếp qua đường hầm này đến máy tính local của bạn.

Ưu điểm của cách này là nhanh, không cần deploy. Nhược điểm cũng rất rõ ràng: Địa chỉ hay thay đổi, tốc độ không ổn định, máy tính của bạn phải luôn bật. Nó phù hợp để demo nhanh trong giai đoạn phát triển, chứ không hợp làm phương thức truy cập lâu dài.

Nếu bạn muốn sản phẩm được mọi người truy cập ổn định, thì cần phương án deploy chính thức.

Hiểu rõ những điều này, bạn không còn chấp niệm với việc gửi link `localhost` nữa, mà quay người đi sâu vào việc học **Git** —— bởi vì trước khi phát hành ứng dụng cho toàn thế giới, việc đầu tiên cần giải quyết là quản lý an toàn và đồng bộ phiên bản code.

::: tip Thực hành tốt nhất về An ninh mạng

**Mô hình phòng thủ 3 lớp**:

1. **Localhost**: Chỉ máy mình, cách ly vật lý, an toàn nhất
2. **Mạng cục bộ (LAN)**: Thiết bị cùng mạng truy cập được, cần tường lửa kiểm soát
3. **Mạng công khai (Public)**: Bất kỳ ai cũng truy cập được, cần xác thực danh tính nghiêm ngặt và mã hóa

**Nguyên tắc then chốt**:

- ✅ Môi trường phát triển dùng localhost
- ✅ Môi trường test dùng mạng cục bộ + xác thực danh tính
- ✅ Môi trường sản xuất dùng HTTPS + mật khẩu mạnh
- ❌ Không bao giờ để lộ dữ liệu nhạy cảm khi dùng công cụ xuyên ngầm
  :::

::: tip Bảng tra nhanh quyết định kịch bản chia sẻ

| Đối tượng mục tiêu     | Phương án đề xuất      | Công cụ             | Chi phí  | Thời lượng |
| ---------------------- | ---------------------- | ------------------- | -------- | ---------- |
| Bản thân (đa thiết bị) | Truy cập LAN           | -                   | Miễn phí | Tạm thời   |
| Demo cho bạn bè        | Xuyên ngầm (Tunneling) | ngrok/cpolar        | Miễn phí | Vài tiếng  |
| Người dùng sử dụng     | Triển khai ứng dụng    | Vercel/Cloud Server | Trả phí  | Lâu dài    |
| Cộng tác viên          | Quản lý mã nguồn       | GitHub              | Miễn phí | Lâu dài    |

:::

::: warning Cảnh báo an toàn khi xuyên ngầm

**Khi sử dụng công cụ xuyên ngầm**:

- ⚠️ Thêm bảo vệ mật khẩu: `ngrok http 3000 --auth="user:pass"`
- ⚠️ Giới hạn IP truy cập: `ngrok http 3000 --cidr-allow=203.0.113.0/24`
- ⚠️ Đóng ngay sau khi demo xong
- ⚠️ Không truyền tải dữ liệu nhạy cảm (Mật khẩu, Token)
- ⚠️ Không để lộ trang quản trị (Admin panel)

:::
