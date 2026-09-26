# SPEC — LAB 1: CHUẨN BỊ MÔI TRƯỜNG LÀM VIỆC

## 1. Mục đích
Thiết lập và kiểm thử toàn bộ môi trường công cụ cần thiết cho môn học ECO2432 (Google Antigravity, Ví MetaMask kết nối mạng thử nghiệm Sepolia, Kho mã nguồn GitHub và Quy ước AGENTS.md).

## 2. Đầu vào
- Tài khoản Google (để đăng nhập công cụ AI Antigravity).
- Trình duyệt Chrome / Edge (để cài đặt tiện ích ví MetaMask).
- Tài khoản GitHub cá nhân (để fork kho mã nguồn `hce-web3-starter`).
- Liên kết kho mã nguồn mẫu: `hce-web3-starter`.
- Cổng vòi nhận Sepolia ETH (Google Cloud Web3 Faucet hoặc ví kho bạc của lớp).

## 3. Quy tắc nghiệp vụ
- R1: Công cụ lập trình hỗ trợ AI (Antigravity) phải khởi động thành công và phản hồi đúng câu hỏi kiểm tra lý thuyết ban đầu.
- R2: Ví MetaMask phải được tạo mới, sao lưu an toàn 12 cụm từ khôi phục bí mật (Secret Recovery Phrase) trên giấy, không lưu trực tuyến.
- R3: Ví MetaMask phải kích hoạt hiển thị mạng thử nghiệm (Test networks) và chuyển sang đúng mạng **Sepolia**.
- R4: Ví phải nhận được tối thiểu 0.05 - 0.5 Sepolia ETH để chuẩn bị phí giao dịch (gas) cho các bài thực hành tiếp theo.
- R5: Kho mã nguồn cá nhân phải được fork từ `hce-web3-starter` và clone về máy trạm.
- R6: Tệp `AGENTS.md` phải được đọc hiểu và bổ sung thêm ít nhất 1 quy tắc cá nhân vào cuối tệp trước khi tạo commit đầu tiên.

## 4. Đầu ra
- Ảnh chụp màn hình giao diện Antigravity đang mở thư mục dự án `hce-web3-starter`.
- Địa chỉ ví MetaMask cá nhân trên mạng Sepolia (đã điền vào bảng tính của lớp).
- Đường dẫn tới bản ghi thay đổi đầu tiên (First Commit URL) trên GitHub chứa tệp `AGENTS.md` đã cập nhật.

## 5. Trường hợp ngoại lệ
- Nếu máy tính không cài đặt được Antigravity: Chuyển sang phương án dự phòng sử dụng Gemini Code Assist trong VS Code hoặc Remix IDE + Gemini Web.
- Nếu các cổng Faucet tự động từ chối cấp Sepolia ETH (do yêu cầu số dư mainnet): Gửi địa chỉ ví cho Giảng viên để nhận ETH từ ví kho bạc của lớp.
- Nếu sinh viên chưa cài đặt Git CLI: Sử dụng giao diện Git tích hợp trong Antigravity hoặc GitHub Desktop / GitHub Web UI để tải và commit mã nguồn.

## 6. Ngoài phạm vi
- Không thực hiện giao dịch chuyển tiền hoặc tương tác smart contract trên mạng Ethereum Mainnet (chỉ thao tác trên mạng thử nghiệm Sepolia).
- Không chia sẻ hoặc đưa 12 từ khôi phục / Khóa riêng tư (Private Key) vào bất kỳ tệp tin hay công cụ nào.
