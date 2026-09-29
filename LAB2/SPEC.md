# SPEC — LAB 2: VÍ VÀ GIAO DỊCH ĐẦU TIÊN

## 1. Mục đích
Thực hiện, quan sát và mổ xẻ vòng đời của giao dịch chuyển tiền (ETH) trên mạng thử nghiệm Sepolia, phân tích nguyên nhân thất bại và rút ra bài học nghiệp vụ về tính bất biến của Blockchain.

## 2. Đầu vào
- Ví MetaMask cá nhân có tối thiểu 0.05 Sepolia ETH.
- Địa chỉ ví người nhận hợp lệ (dạng 42 ký tự Hexa, chuẩn EIP-55).
- Tham số chuyển tiền: 0.01 Sepolia ETH.

## 3. Quy tắc nghiệp vụ
- R1: Giao dịch hợp lệ phải chuyển đổi trạng thái từ Pending sang Confirmed và sinh ra Transaction Hash duy nhất trên mạng Sepolia.
- R2: Phí giao dịch (Gas fee) luôn được tính bằng đồng tiền gốc (ETH) của mạng lưới và trừ trực tiếp vào số dư ví gửi (không trừ vào số tiền chuyển đến người nhận).
- R3: Địa chỉ người nhận phải thỏa mãn kiểm tra mã băm checksum (EIP-55); nếu sai ký tự hoặc sai định dạng, phần mềm ví phải từ chối khởi tạo giao dịch.
- R4: Số dư khả dụng của ví gửi phải lớn hơn hoặc bằng (Số tiền chuyển + Phí gas ước tính).
- R5: Giao dịch một khi đã được xác nhận (Confirmed) vào khối thì không thể đảo ngược hay thu hồi số tiền đã gửi.

## 4. Đầu ra
- Mã băm (Tx Hash) của 01 giao dịch chuyển 0.01 Sepolia ETH thành công.
- Bản ghi nhận diện và thông tin lỗi của 01 giao dịch thất bại có chủ đích (Sai địa chỉ hoặc Không đủ phí gas).
- Tệp `lab02.md` chứa bảng đối chiếu 2 trạng thái giao dịch và câu trả lời nghiệp vụ 3 câu.

## 5. Trường hợp ngoại lệ
- Nếu người gửi nhập sai một ký tự trong địa chỉ ví: MetaMask cảnh báo "Invalid address" và chặn nút gửi do vi phạm thuật toán Checksum EIP-55.
- Nếu người gửi chọn gửi toàn bộ số dư (Max balance): Hệ thống báo lỗi "Insufficient funds" do không đủ tiền thanh toán phí gas cho validator.
- Nếu mạng Sepolia bị nghẽn (Gas price tăng đột biến): Giao dịch có thể bị kẹt ở trạng thái Pending lâu hơn bình thường hoặc cần tăng gas (Speed Up).

## 6. Ngoài phạm vi
- Không thực hiện giao dịch chuyển tiền trên mạng chính thức (Ethereum Mainnet).
- Không tương tác với các Smart Contract phức tạp hoặc gửi các token tùy chỉnh trong bài này (chỉ thao tác chuyển ETH gốc giữa 2 tài khoản EOA).
