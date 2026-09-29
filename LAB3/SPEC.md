# SPEC — LAB 3: ĐỌC GIAO DỊCH VÀ HỢP ĐỒNG TRÊN ETHERSCAN

## 1. Mục đích
Trang bị năng lực đọc hiểu, giải mã và thẩm định chuyên sâu các thành phần dữ liệu giao dịch on-chain (Transaction) và cấu trúc hợp đồng thông minh (Smart Contract) trên Etherscan, phục vụ nghiệp vụ kiểm toán, kế toán và thẩm định tuân thủ/AML tài sản mã hóa.

## 2. Đầu vào
- Mã băm giao dịch (Tx Hash) chuyển 0.01 Sepolia ETH từ Lab 2: `0xa86f43080e63535b6bde87668ae0f6877056bb7ab0ee4c7c4b5e1b0336ec1bc4`.
- Địa chỉ ví người gửi (From): `0xe65449A5a0f67e390ca250326c3f3F166463A899`.
- Địa chỉ ví người nhận (To): `0xefF0071F6AdBE649892656765aE9cFC60d69247f`.
- Hợp đồng thông minh đồng ổn định giá chuẩn trên Ethereum Mainnet: Tether USD (USDT - `0xdAC17F958D2ee523a2206206994597C13D831ec7`) hoặc USD Coin (USDC - `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`).

## 3. Quy tắc nghiệp vụ
- **R1:** Mọi thông số trong biên lai giao dịch (Status, Block, Timestamp, From, To, Value, Tx Fee, Gas Price, Nonce) phải được đối chiếu trực tiếp từ trình khám phá khối (Blockchain Explorer) chính thức.
- **R2:** Phí giao dịch (Transaction Fee) phải được tính toán chính xác theo công thức: `Tx Fee = Gas Used × Effective Gas Price`, quy đổi rõ ràng từ đơn vị Wei sang ETH (chia cho 10^18).
- **R3:** Phân định rõ ràng giữa mã bytecode (chuỗi mã máy thực thi) và mã nguồn đã xác thực (Verified Source Code) của hợp đồng thông minh.
- **R4 (Mở rộng nghiệp vụ):** Phân loại rành mạch giữa thao tác Đọc (Read Contract - view/pure, không thay đổi trạng thái, không tốn gas) và thao tác Ghi (Write Contract - thay đổi trạng thái sổ cái, yêu cầu ký giao dịch bằng khóa bí mật và trả phí gas).
- **R5 (Mở rộng nghiệp vụ - Thẩm định rủi ro):** Nhận diện cơ chế kiểm soát đặc quyền tập trung (Centralized Privileges / Admin Controls), cụ thể là các hàm đóng băng số dư (Blacklist / Freeze) có thể gây rủi ro phong tỏa tài sản người dùng.

## 4. Đầu ra
- Tệp `forensics.md` chứa:
  1. Bảng mổ xẻ 8 trường thông tin cốt lõi của giao dịch Lab 2 kèm phân tích góc nhìn nghiệp vụ tài chính/tuân thủ.
  2. Báo cáo thẩm định hợp đồng USDT trên Ethereum Mainnet, trả lời đầy đủ 3 câu hỏi nghiệp vụ quan trọng.
- Tệp `AI_JOURNAL.md` ghi nhận nhật ký làm việc với AI cho Lab 3.

## 5. Trường hợp ngoại lệ
- **E1:** Nếu giao dịch thất bại (Status: Fail/Reverted), phí gas vẫn bị tiêu thụ và không được hoàn lại cho người gửi; kế toán phải hạch toán riêng phần chi phí mất này vào chi phí vận hành.
- **E2:** Nếu hợp đồng chưa được xác minh mã nguồn (Unverified Contract), nhà thẩm định chỉ thấy bytecode mà không thấy logic nghiệp vụ thực tế; hệ thống phải gắn cờ rủi ro cao (High Risk Flag).
- **E3:** Nếu trường Nonce của ví bị nhảy cóc (bỏ trống một chỉ số nonce), giao dịch có chỉ số nonce cao hơn sẽ bị kẹt ở trạng thái Pending cho đến khi giao dịch có nonce trước đó được xử lý.

## 6. Ngoài phạm vi
- Không thực hiện ký gửi các giao dịch Write Contract làm tiêu tốn ETH thật trên mạng Ethereum Mainnet.
- Không can thiệp sửa đổi dữ liệu đã ghi nhận trên chuỗi khối.
