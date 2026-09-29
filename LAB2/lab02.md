# BÁO CÁO THỰC HÀNH — LAB 2: VÍ VÀ GIAO DỊCH ĐẦU TIÊN

## 1. Bảng đối chiếu giao dịch

| Trường thông tin | Giao dịch thành công | Giao dịch thất bại (có chủ đích) |
| :--- | :--- | :--- |
| **Mã băm giao dịch (Tx Hash)** | [`0xa86f43080e63535b6bde87668ae0f6877056bb7ab0ee4c7c4b5e1b0336ec1bc4`](https://sepolia.etherscan.io/tx/0xa86f43080e63535b6bde87668ae0f6877056bb7ab0ee4c7c4b5e1b0336ec1bc4) | `N/A` *(Không sinh Tx Hash do bị chặn tại client)* |
| **Ví gửi (From)** | `0xe65449A5a0f67e390ca250326c3f3F166463A899` | `0xe65449A5a0f67e390ca250326c3f3F166463A899` |
| **Ví nhận (To)** | `0xefF0071F6AdBE649892656765aE9cFC60d69247f` | `0xefF0071F6AdBE649892656765aE9cFC60d69247e` *(Sửa 1 ký tự cuối)* |
| **Số tiền chuyển (Value)** | `0.01 Sepolia ETH` (10,000,000,000,000,000 Wei) | `0.01 Sepolia ETH` |
| **Gas Used / Gas Limit** | `21,000` / `31,500` | `0` *(Chưa phát sinh)* |
| **Phí giao dịch thực tế (Tx Fee)**| `0.000053208340017 ETH` (53,208,340,017,000 Wei) | `0 ETH` *(Không tốn gas khi bị chặn ở lớp ứng dụng ví)* |
| **Block Number & Nonce** | Block `11805551` \| Nonce `2` | `N/A` |
| **Trạng thái** | `Confirmed (Success)` | `Blocked by Client (Invalid Address)` |
| **Nguyên nhân (nếu thất bại)** | Không có (Giao dịch hợp lệ, đầy đủ số dư và phí gas) | **Tình huống A (Sai Checksum EIP-55):** Khi thay đổi 1 ký tự trong địa chỉ ví nhận, MetaMask phát hiện lỗi định dạng checksum và cảnh báo *"Invalid address"*, vô hiệu hóa nút gửi để bảo vệ tài sản người dùng |

---

## 2. Phân tích nghiệp vụ & Câu hỏi tình huống

> **Câu hỏi:** *Nếu bạn chuyển nhầm tiền mã hóa (ETH) cho người lạ, có lấy lại được không? Vì sao?*

**Trả lời (3 câu chuẩn mực):**
1. **Khả năng lấy lại:** Trong mạng lưới Blockchain công khai như Ethereum, người gửi **hoàn toàn không thể tự ý hủy, đảo ngược hoặc yêu cầu hệ thống hoàn lại** số tiền đã chuyển nhầm cho người lạ một khi giao dịch đã được xác nhận vào khối (Confirmed).
2. **Nguyên nhân kỹ thuật:** Do đặc tính **bất biến (immutability)** của sổ cái phân tán và cơ chế **đồng thuận phi tập trung**, không có bất kỳ tổ chức trung gian, ngân hàng hay tổng đài máy chủ trung tâm nào có quyền can thiệp vào số dư hoặc sửa đổi trạng thái giao dịch của các địa chỉ ví.
3. **Giải pháp thực tế:** Cách duy nhất để lấy lại tiền là chủ động liên hệ và trông đợi vào sự tự nguyện chuyển trả lại của chủ sở hữu địa chỉ ví nhận (nếu có thể xác định danh tính ngoài đời thực của họ).
