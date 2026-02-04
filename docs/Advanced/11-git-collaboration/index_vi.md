---
title: "Chương 11: Kiểm soát phiên bản Git và Cộng tác đa nền tảng"
---

# Chương 11: Kiểm soát phiên bản Git và Cộng tác đa nền tảng

## Lời tựa

Tính năng ngày càng phong phú, kho lưu trữ Git cục bộ của bạn đã tích lũy một chồng dày hồ sơ lưu trữ. Một ngày nọ, bạn thân của bạn cũng định tham gia cùng làm với bạn.

Có thể bạn nghĩ một mình là cân được hết. Thực tế là: một mình thường bị phân tán sự chú ý, còn team nhỏ 2-3 người —— người lo giao diện Frontend, người lo API Backend, người lo viết Test —— ngược lại chạy nhanh hơn. Cốt lõi của cộng tác Git, chính là để mỗi người tập trung vào lãnh địa của mình, đồng thời giữ cho code được đồng bộ.

Bây giờ, để bạn bè có thể lấy được code của bạn, sư phụ bảo, bạn cần đồng bộ những hồ sơ lưu trữ cục bộ này lên đám mây.

### Kho lưu trữ đám mây và Chứng thực

Ông giới thiệu cho bạn các nền tảng lưu trữ code (như **GitHub** hoặc **Gitee**). Bản chất của cộng tác thực ra rất đơn giản: Bạn đã dùng AI rèn luyện thói quen commit cục bộ tốt trên máy mình rồi (Commit cục bộ nhắc đến ở Chương 2), giờ chỉ cần thêm một bước thao tác nữa.

**Chứng thực SSH**: Sư phụ khuyên dùng **Chứng thực SSH** an toàn và tiện lợi hơn, sau khi tạo cặp khóa (key pair), không cần nhập mật khẩu mỗi lần thao tác nữa. Chương này sẽ giảng giải chi tiết nguyên lý SSH và các bước cấu hình.

Trước khi bắt đầu đẩy code, bạn cần đăng ký một tài khoản trên GitHub. Đăng ký thì đơn giản, nhưng **đăng nhập trong terminal** thường là cửa ải đầu tiên của người mới. Khi bạn chạy `git push` lần đầu, terminal sẽ yêu cầu bạn cung cấp chứng thực. Sư phụ đặc biệt dặn dò:

- **Đừng nhập mật khẩu đăng nhập GitHub của bạn**: GitHub đã bỏ tính năng đăng nhập terminal bằng mật khẩu từ lâu rồi.
- **Sử dụng Access Token (Thẻ bài)**: Bạn cần vào cài đặt trên trang web GitHub để sinh một thẻ bài (Token), coi nó như mật khẩu để điền vào.
- **Hoặc khuyên dùng cách SSH**: Sinh một cặp khóa SSH (khóa công khai đưa cho GitHub, khóa riêng giữ cho mình), như vậy mỗi lần đẩy code đều không cần nhập mật khẩu, vừa an toàn vừa tiện.
- **Lưu trữ chứng thực cục bộ**: Nếu bạn dùng cách HTTPS (nhập tài khoản mật khẩu/token), Git thường sẽ chu đáo lưu chứng thực của bạn vào "Trình quản lý chứng thực" của hệ thống, như vậy bạn cũng không cần nhập tay mỗi lần.

Sau khi chứng thực thông qua, quy trình sẽ trơn tru:

- **`git push` (Đẩy)**: Upload hồ sơ lưu trữ cục bộ của bạn lên kho đám mây.
- **`git pull` (Kéo)**: Bạn của bạn ở đầu bên kia, tải tiến độ mới nhất trên mây về máy tính của họ.

Cách này đáng tin cậy hơn nhiều so với việc gửi file nén cho nhau, vì Git có thể ghi lại chính xác từng dòng code do ai sửa vào lúc nào.

### Cộng tác đa nền tảng

Tuy nhiên, khi máy tính Windows của bạn gặp máy tính Mac của bạn bè, bạn dẫm phải 3 cái hố cộng tác đa nền tảng kinh điển.

**Một: .gitignore**

Ở chương 6, chúng ta đã cấu hình `.gitignore` vì lý do bảo mật. Ở giai đoạn cộng tác, file này có ý nghĩa mới: **Phòng ngừa ô nhiễm môi trường của đồng đội**. Nếu bạn lỡ tay upload `node_modules`, bạn của bạn khi kéo code về sẽ tải xuống hàng ngàn gói dependency không tương thích với hệ thống máy tính của họ, dẫn đến dự án không chạy nổi. Về việc những nội dung nào tuyệt đối không được commit, xem chi tiết ở mục "Cảnh báo an toàn Git" bên dưới.

**Hai: Tương thích đa nền tảng**

Dự án của bạn sang máy Mac của bạn bè thì báo lỗi "Không tìm thấy file". Rõ ràng bạn viết là `import Button from './button'`, tên file là `Button.tsx`, chạy trên máy Windows của bạn ngon lành cành đào.

Sư phụ bảo, cộng tác đa nền tảng sẽ gặp 3 vấn đề kinh điển: File rác hệ thống, Chữ hoa chữ thường trong tên file, Khác biệt dấu xuống dòng và Dấu phân cách đường dẫn. Xem chi tiết ở mục "Ba nguyên tắc cộng tác đa nền tảng" bên dưới.

Cấu hình xong mấy cái này, cộng tác đa nền tảng sẽ mượt mà hơn nhiều.

**Ba: Dấu phân cách đường dẫn**

Là người dùng Windows, bạn còn dẫm phải một cái hố tàng hình. Đường dẫn bạn copy trực tiếp từ File Explorer chứa dấu gạch chéo ngược `\`, ví dụ `src\components\Button`. Cái này vào trong code sẽ bị nhận diện là ký tự thoát (escape character), dẫn đến báo lỗi. Còn hệ thống Linux/Mac sử dụng dấu gạch chéo thuận `/`. Do đó, khi viết code tham chiếu đường dẫn, hãy luôn thủ công dùng dấu gạch chéo thuận `/`. Các công cụ hiện đại như Node.js sẽ tự động xử lý tính tương thích của nó trên các hệ thống khác nhau.

Cấu hình xong những thứ này, việc cộng tác của bạn và đồng đội sẽ trơn tru hơn nhiều. Mỗi lần sửa code xong, nhớ thực hiện Git Workflow theo thứ tự (xem chi tiết mục "Thực hành tốt nhất về Git Workflow" bên dưới). Đồng đội bên kia dùng `git pull` là lấy được sửa đổi mới nhất của bạn.

### Git Workflow tự động hóa

Tuy nhiên, sư phụ nhắc nhở, "bộ ba tiêu chuẩn" này là chuẩn bị cho con người thao tác thủ công. Đã là dùng AI lập trình, bạn hoàn toàn có thể giao việc này cho AI:

> **"Mỗi lần hoàn thành tính năng hoặc sửa Bug xong, tự động thực hiện git add, git commit (kèm mô tả tiếng Việt) và git push."**

Như vậy bạn hoàn toàn không cần nhớ mấy lệnh này, AI sẽ tự động xử lý giúp bạn vào thời điểm thích hợp.

### Xem lịch sử và sự khác biệt

Đôi khi bạn muốn xem "AI rốt cuộc đã sửa cái gì" hoặc "code hôm qua viết thế nào", trực tiếp bảo AI so sánh ghi chép Git là được. Sư phụ giải thích cho bạn vài lệnh hữu dụng:

- **`git log`**: Xem lịch sử commit, hiển thị tất cả hồ sơ lưu trữ. Nếu chỉ muốn xem 5 cái gần nhất, dùng `git log -5`.
- **`git diff`**: Xem sửa đổi hiện tại chưa commit —— nghĩa là, AI sửa code xong nhưng chưa lưu hồ sơ, bạn có thể dùng lệnh này kiểm tra xem nó sửa gì.
- **`git diff HEAD~1`**: So sánh với phiên bản trước, xem lần commit gần nhất đã sửa gì.
- **`git show <commit-id>`**: Xem nội dung chi tiết của một lần commit cụ thể.

### Rollback (Quay lui)

Chương 2 có nhắc đến Git là "thuốc hối hận" của bạn. Dưới đây là 3 ngữ cảnh:

**Ngữ cảnh 1: Sửa sai rồi, nhưng chưa commit**

Bạn phát hiện code AI vừa sửa nát bét, nhưng nó chưa thực hiện `git commit`. Cách đơn giản nhất:

- **`git checkout -- <đường dẫn file>`**: Hủy bỏ sửa đổi của file nào đó, khôi phục về trạng thái của lần commit trước.
- Hoặc trực tiếp bảo AI: "**Hủy bỏ tất cả sửa đổi đối với file xxx**".

**Ngữ cảnh 2: Đã commit rồi, nhưng muốn quay lại phiên bản trước**

AI vừa commit xong, bạn chạy dự án thấy toang. Bạn muốn quay lại phiên bản chạy được trước đó:

- **`git reset --hard HEAD~1`**: Quay lui về commit trước đó, vứt bỏ tất cả sửa đổi hiện tại.
- **`git reset --hard <commit-id>`**: Quay lui về một phiên bản cụ thể nào đó.

**Ngữ cảnh 3: Đã push lên đám mây rồi**

Tình huống phiền phức nhất: Code lỗi đã `git push` lên kho từ xa rồi. Lúc này `git reset` sẽ vô hiệu, vì lịch sử local và lịch sử cloud của bạn không khớp nhau nữa.

Sư phụ dạy bạn một lệnh an toàn hơn:

- **`git revert <commit-id>`**: Tạo một commit mới, dùng để "hủy bỏ" các sửa đổi của commit được chỉ định. Như vậy lịch sử ghi chép vẫn liên tục, không làm gián đoạn kho đám mây.

Bạn hoàn toàn có thể giao những thao tác này cho AI. Ví dụ trực tiếp nói: "**Rollback về phiên bản chạy được trước đó**" hoặc "**Hủy bỏ lần commit gần nhất**", AI sẽ tự động thực hiện lệnh chính xác.

### Branch (Nhánh)

Dự án càng lớn, bạn có thể muốn thử nghiệm một tính năng mới, nhưng lại sợ làm hỏng code hiện có. Lúc này cần dùng đến **Branch (Nhánh)**.

Sư phụ dùng một ví dụ để giải thích Branch: Giống như "slot lưu game". Tuyến chính gọi là `main` hoặc `master`, bạn có thể mở một nhánh mới ví dụ `feature-login`, tha hồ quậy trên tính năng mới. Quậy hỏng thì quay về tuyến chính; quậy xong thì hợp nhất nhánh mới vào tuyến chính.

Lệnh cốt lõi:

- **`git branch <tên nhánh>`**: Tạo nhánh mới.
- **`git checkout <tên nhánh>`**: Chuyển sang nhánh chỉ định. Cách viết hiện đại là `git switch <tên nhánh>`.
- **`git checkout -b <tên nhánh>`**: Tạo và chuyển sang nhánh mới luôn, một lệnh xong ngay.
- **`git merge <tên nhánh>`**: Hợp nhất nhánh chỉ định vào nhánh hiện tại.

Trong ngữ cảnh cộng tác, nhánh rất quan trọng: Mỗi người phát triển trên nhánh riêng của mình, làm xong mới hợp nhất vào tuyến chính, như vậy sẽ không ảnh hưởng lẫn nhau.

### Pull Request - Rà soát code

Sư phụ bảo, trong cộng tác team thực tế, trực tiếp merge nhánh vào tuyến chính là cách làm nguy hiểm. Bạn có thể vô tình đưa Bug vào, hoặc chất lượng code không đủ tốt, ảnh hưởng đến sự ổn định của toàn dự án.

Thế là, **Pull Request (gọi tắt là PR)** ra đời. Nghĩa đen của PR là "Yêu cầu kéo", nhưng hiểu chính xác hơn là "Yêu cầu hợp nhất". Khi bạn phát triển xong tính năng trên nhánh của mình, không phải merge trực tiếp, mà là khởi tạo một PR, nói rằng: "Này, tôi làm xong tính năng mới rồi, nhờ các bạn kiểm tra code giúp, không vấn đề gì thì hợp nhất vào nhé."

Giá trị cốt lõi của quy trình này là **Code Review (Rà soát code)**: Người khác trong team xem code của bạn, đưa ra gợi ý cải tiến, phát hiện vấn đề tiềm ẩn. Nghiên cứu chỉ ra rằng, Code Review tốt có thể giảm hơn 80% lỗi. Trong thời đại lập trình AI, bạn có thể để AI làm **Self-Review** trước khi tạo PR, kiểm tra lỗi logic, lỗ hổng bảo mật, vấn đề hiệu năng, phong cách code..., như vậy chất lượng PR nộp lên sẽ cao hơn.

PR còn mang lại 2 lợi ích: **Kiểm tra tự động** (Nền tảng tự động chạy test, không qua thì không cho merge) và **Ghi chép thảo luận** (Bình luận ngay dưới dòng code cụ thể, tất cả thảo luận được lưu lại).

Sư phụ nói, tuy với team nhỏ hoặc dự án cá nhân, PR có vẻ hơi rườm rà. Nhưng khi bạn bắt đầu cộng tác với người khác, đặc biệt là tham gia dự án nguồn mở, PR là quy trình làm việc không thể thiếu. Có điều mới bắt đầu không cần quá xoắn xuýt chiến lược phân nhánh, cứ rèn thói quen tự động commit trên tuyến chính trước đã, đợi độ phức tạp của dự án tăng lên hẵng áp dụng quản lý nhánh.

### Giải quyết xung đột (Conflict)

Đã là cộng tác thì khó tránh khỏi tình huống xung đột: Khi bạn và bạn bè cùng sửa một dòng code trong cùng một file, Git không biết nên nghe ai.

Trong thời đại Vibecoding, bạn không cần đối mặt với mấy ký hiệu `<<<<<<< HEAD` đau đầu rồi luống cuống tay chân nữa. Bạn chỉ cần gửi **nội dung file chứa đánh dấu xung đột** cho AI, rồi bảo nó:

> **"Giải quyết xung đột Git này. Giữ lại logic của tôi và logic mới nhất từ remote, nếu logic xung đột, hãy lấy của tôi làm chuẩn (hoặc lấy remote làm chuẩn)."**

AI sẽ giúp bạn hợp nhất code hoàn hảo, bạn chỉ cần copy code đã sửa về, commit lại lần nữa là xong.

Thông qua Git, bạn và bạn bè có thể đồng bộ code rồi. Nhưng sư phụ bảo, ngoài code ra, rất nhiều "kiến thức ngầm" của team bạn —— quy ước đặt tên, quy trình làm việc, kỹ năng debug —— cũng cần được chia sẻ. Những cái này còn có thể thông qua **Agent Skills** để mã hóa thành các đơn vị kiến thức tái sử dụng được. Commit Skills lên Git, đồng đội kéo code về, AI của họ sẽ tự động học được những quy ước team này. Về việc phát triển và sử dụng Skills, chúng ta sẽ giảng giải ở các nội dung sau.

::: tip Thực hành tốt nhất về Git Workflow

**Bộ ba phát triển hàng ngày**:

```bash
git add .                    # Tạm lưu tất cả thay đổi
git commit -m "mô tả"        # Commit vào local
git push                     # Đẩy lên remote
```

**Quy chuẩn thông tin Commit (Conventional Commits)**:

- `feat:` Tính năng mới
- `fix:` Sửa Bug
- `docs:` Cập nhật tài liệu
- `style:` Định dạng code
- `refactor:` Tái cấu trúc
- `test:` Kiểm thử
- `chore:` Xây dựng/Công cụ

**Ví dụ**:

```bash
git commit -m "feat(auth): Thêm tính năng đăng nhập người dùng"
git commit -m "fix(api): Sửa lỗi timeout interface đăng nhập"
```

:::

::: tip Nguyên tắc vàng trong cộng tác team

**Ba nguyên tắc cộng tác đa nền tảng**:

1. **Cấu hình .gitignore**: Ngăn chặn ô nhiễm môi trường đồng đội
   - ❌ Tuyệt đối không commit: `node_modules`, `.env`, file khóa bí mật
   - ❌ Rác hệ thống: `.DS_Store`, `Thumbs.db`
   - ✅ Dùng bản mẫu: github/gitignore

2. **Thống nhất dấu xuống dòng**: Tránh diff giả

   ```bash
   # Cấu hình Git
   git config --global core.autocrlf input   # Mac/Linux
   git config --global core.autocrlf true    # Windows
   ```

3. **Thống nhất dấu phân cách đường dẫn**: Luôn dùng `/`
   ```javascript
   // ✅ Đúng
   import { Button } from "src/components/Button";
   // ❌ Sai
   import { Button } from "src\\components\\Button";
   ```
   :::

::: warning Cảnh báo an toàn Git

**⚠️ Nội dung TUYỆT ĐỐI KHÔNG commit**:

- ❌ API Key, Token, Chứng chỉ
- ❌ Mật khẩu Database, Chuỗi kết nối
- ❌ Khóa riêng (`.pem`, `.key`, `id_rsa`)
- ❌ File biến môi trường (`.env`, `.env.local`)
- ❌ Thông tin nhạy cảm cá nhân

**Danh sách kiểm tra**:

```bash
# Kiểm tra trước khi commit
git diff --cached --name-only | grep -E '\.(env|pem|key)$'
```

**Nếu lỡ commit rồi? Thu hồi ngay**:

```bash
# Xóa triệt để khỏi lịch sử (Thao tác nguy hiểm)
# Khuyên dùng BFG Repo-Cleaner hoặc git filter-repo (nhanh và an toàn hơn filter-branch)
# Ví dụ dùng BFG:
# bfg --delete-files .env
# git reflog expire --expire=now --all
# git gc --prune=now --aggressive
git push origin --force --all
```

:::

::: tip Tra cứu nhanh vấn đề cộng tác thường gặp

| Vấn đề                   | Nguyên nhân                | Giải pháp                        |
| ------------------------ | -------------------------- | -------------------------------- |
| **Push thất bại**        | Remote có commit mới       | `git pull --rebase`              |
| **Pull xung đột**        | Hai người sửa cùng một chỗ | Xem chương "Giải quyết xung đột" |
| **Windows commit CRLF**  | Chưa cấu hình autocrlf     | `git config core.autocrlf true`  |
| **Không tìm thấy file**  | Vấn đề chữ hoa thường      | Thống nhất đặt tên chữ thường    |
| **node_modules ô nhiễm** | Chưa cấu hình .gitignore   | Thêm `node_modules/`             |

**Gợi ý giải quyết xung đột**:

```
"Gửi nội dung xung đột cho AI, bảo: Giải quyết xung đột Git này,
giữ lại logic của tôi và logic mới nhất từ remote, nếu logic xung đột, hãy lấy của tôi làm chuẩn"
```

:::

## Điều hướng tiểu tiết

```
- 11.1 Dòng chảy dữ liệu Git (./01-git-data-flow.md) 🔴 - Hiểu mô hình 3 vùng của Git và sự luân chuyển dữ liệu
- 11.2 Tạo kho GitHub/Gitee (./02-create-repo.md) 🔴 - Tạo và cấu hình kho code đám mây từ con số 0
- 11.3 Chi tiết SSH (./03-ssh-details.md) 🔴 - Hiểu nguyên lý SSH, cấu hình và khắc phục sự cố
- 11.4 Vấn đề cộng tác đa nền tảng (./04-cross-platform-issues.md) 🔴 - Giải quyết khác biệt cộng tác giữa Windows, Mac, Linux
- 11.5 Lệnh Git thường dùng (./05-git-commands.md) 🔴 - Nắm vững các lệnh Git thường dùng nhất trong phát triển hàng ngày
- 11.6 Thực chiến thao tác Rollback (./06-rollback-practice.md) 🔴 - Nắm vững giải pháp cho các ngữ cảnh rollback khác nhau
- 11.7 Quản lý nhánh (./07-branch-management.md) 🔴 - Hiểu mô hình nhánh và chiến lược cộng tác team
- 11.8 Thực chiến giải quyết xung đột (./08-conflict-resolution.md) 🔴 - Bình tĩnh đối phó với xung đột hợp nhất Git
- 11.9 Quy trình Pull Request (./09-pull-request-workflow.md) 🔴 - Hiểu quy trình PR và rà soát code
- 11.10 Chia sẻ kiến thức team bằng Skills (./10-team-skills-sharing.md) 🟡 - Sử dụng Skills để mã hóa và chia sẻ quy chuẩn team
- 11.11 Cộng tác team bằng Agent Skills (./11-agent-skills-collaboration.md) 🟡 - Sử dụng Agent Skills xây dựng luồng công việc team thông minh
```
