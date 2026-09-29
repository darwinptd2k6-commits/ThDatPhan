# BÁO CÁO GIÁM ĐỊNH ON-CHAIN — LAB 3: ĐỌC GIAO DỊCH VÀ HỢP ĐỒNG TRÊN ETHERSCAN

---

## 1. Mổ xẻ chi tiết giao dịch chuyển tiền (Sepolia Testnet)

- **Mã băm giao dịch (Tx Hash):** [`0xa86f43080e63535b6bde87668ae0f6877056bb7ab0ee4c7c4b5e1b0336ec1bc4`](https://sepolia.etherscan.io/tx/0xa86f43080e63535b6bde87668ae0f6877056bb7ab0ee4c7c4b5e1b0336ec1bc4)
- **Trình khám phá chuỗi khối:** Etherscan (Sepolia Testnet Explorer)

### Bảng phân tích 8 trường dữ liệu cốt lõi

| STT | Tên trường | Giá trị thực tế trên Etherscan | Ý nghĩa kỹ thuật | Vì sao người làm nghiệp vụ (AML / Kế toán) cần |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Status** | `Success` (Confirmed) | Trạng thái giao dịch: Thành công hay Thất bại trên chuỗi. | Giao dịch thất bại (Fail) vẫn bị trừ phí gas tiêu thụ. Kế toán cần biết để không ghi nhận tài sản vào nhưng vẫn phải hạch toán chi phí giao dịch. |
| **2** | **Block** | `11805551` | Số thứ tự khối (Block height) chứa giao dịch này. | Xác định chính xác thời điểm đóng băng dữ liệu vào sổ cái, dùng đối soát thứ tự phát sinh sự kiện tài chính. |
| **3** | **Timestamp** | `Sep-29-2026 05:16:48 AM +UTC` | Thời gian khối được thợ đào/validator đóng dấu xác nhận. | Mốc thời gian pháp lý chuẩn để quy đổi tỷ giá sang tiền pháp định (USD/VND), ghi nhận doanh thu/chi phí tại kỳ kế toán. |
| **4** | **From / To** | **From:** `0xe65449A5a0f67e390ca250326c3f3F166463A899`<br>**To:** `0xefF0071F6AdBE649892656765aE9cFC60d69247f` | Địa chỉ ví gửi (bên chuyển) và địa chỉ ví nhận (bên thụ hưởng). | Đối tượng bắt buộc để định danh (KYC/AML), kiểm tra xem ví có nằm trong danh sách đen (OFAC/Sanctions list) hay không. |
| **5** | **Value** | `0.01 Sepolia ETH`<br>*(10,000,000,000,000,000 Wei)* | Khối lượng ETH thực tế được chuyển giao giữa 2 ví. | Giá trị giao dịch kinh tế cốt lõi cần hạch toán vào số dư tài sản của các bên tham gia. |
| **6** | **Transaction Fee** | `0.000053208340017 ETH`<br>*(53,208,340,017,000 Wei)* | Tổng chi phí thực tế mà ví gửi phải thanh toán cho validator (`Gas Used × Gas Price`). | Chi phí vận hành trực tiếp, bắt buộc phải hạch toán riêng vào mục Chi phí tài chính/phí dịch vụ thanh toán. |
| **7** | **Gas Price** | `2.533730477 Gwei`<br>*(2,533,730,477 Wei)* | Đơn giá gas tại thời điểm giao dịch được đóng khối. | Giải thích nguyên nhân biến động chi phí: vì sao cùng chuyển 0.01 ETH nhưng thời điểm mạng nghẽn lại tốn phí cao hơn lúc vắng. |
| **8** | **Nonce** | `2` | Số thứ tự tăng dần của giao dịch phát đi từ địa chỉ ví gửi `0xe654...`. | Phát hiện giao dịch bị thất lạc, kẹt lệnh (pending nonce) hoặc bị thay thế (front-running/speed-up). Tránh lỗi gian lận chi tiêu kép (Double Spending). |

---

## 2. Đọc và thẩm định hợp đồng thực tế (Tether USD — USDT trên Ethereum Mainnet)

- **Địa chỉ hợp đồng:** [`0xdAC17F958D2ee523a2206206994597C13D831ec7`](https://etherscan.io/address/0xdAC17F958D2ee523a2206206994597C13D831ec7)
- **Tên token:** Tether USD (USDT)
- **Chuẩn hợp đồng:** ERC-20 (có phần mở rộng quyền quản trị)

### 2.1. Phân biệt cấu trúc Contract trên Etherscan
1. **Bytecode:** Chuỗi mã máy dạng thập lục phân (Hexadecimal) mà máy ảo Ethereum Virtual Machine (EVM) thực thi. Con người không thể đọc hiểu trực tiếp được logic nghiệp vụ.
2. **Verified Source Code:** Toàn bộ mã nguồn Solidity do tổ chức phát hành tải lên và đã được hệ thống Etherscan biên dịch, đối chiếu trùng khớp 100% với Bytecode trên chuỗi. Giúp kiểm toán viên và người dùng minh bạch hóa toàn bộ thuật toán hoạt động.
3. **Tab Read Contract:** Tập hợp các hàm dạng `view` hoặc `pure`. Chỉ truy xuất đọc dữ liệu từ blockchain, thực thi hoàn toàn miễn phí (0 gas), không cần ví Web3 ký lệnh.
4. **Tab Write Contract:** Tập hợp các hàm thay đổi trạng thái sổ cái (State-changing functions). Bắt buộc phải có chữ ký từ ví cá nhân và tiêu tốn phí gas để validator đóng khối.

---

### 2.2. Trả lời 3 câu hỏi nghiệp vụ trọng tâm

#### Câu 1: Hợp đồng bạn xem có công bố mã nguồn đã xác thực không?
- **Trả lời:** **Có.** Hợp đồng Tether USD (USDT) trên Etherscan đã được xác minh đầy đủ (có tích xanh **Contract Source Code Verified**). Toàn bộ mã nguồn Solidity của các hợp đồng con (`TetherToken`, `StandardToken`, `BasicToken`, `ERC20Basic`, `ERC20`, `Ownable`, `BlackList`) đều được công khai hoàn toàn trên trình duyệt Etherscan.

#### Câu 2: Tổng cung của đồng đó là bao nhiêu? Đọc ra từ hàm nào?
- **Trả lời:** 
  - Đọc ra từ hàm **`totalSupply()`** trong tab **Read Contract**.
  - Kết quả trả về là một số nguyên rất lớn (do USDT quy định `decimals = 6`). Ví dụ giá trị đọc được là `119,000,000,000,000,000` đơn vị nhỏ nhất, tương đương **119 tỷ USDT** sau khi chia cho $10^6$.
  - Ngoài ra có thể gọi hàm `balanceOf(address)` để kiểm tra số dư khả dụng của bất kỳ địa chỉ ví nào đang nắm giữ USDT.

#### Câu 3: Trong tab Write Contract, có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không? Nếu có, tên hàm là gì?
- **Trả lời:** **CÓ.** Hợp đồng USDT tích hợp hợp đồng `BlackList` với quyền quản trị đặc biệt của `Owner`:
  - Tên hàm đóng băng tài khoản: **`addBlackList(address _evilUser)`** — Chỉ có `owner` (Tether Limited) mới có quyền gọi.
  - Khi một địa chỉ bị đưa vào danh sách đen (`isBlackListed[_evilUser] = true`), người dùng này **hoàn toàn bị khóa quyền chuyển tiền (`transfer`) và nhận tiền**.
  - Hợp đồng còn có hàm hủy số dư ví bị chặn: **`destroyBlackFunds(address _blackListedUser)`** cho phép chủ sở hữu đốt toàn bộ số token USDT trong ví bị đóng băng.
  - Tên hàm gỡ bỏ đóng băng: **`removeBlackList(address _clearedUser)`**.

> [!IMPORTANT]
> **Ý nghĩa nghiệp vụ tài chính:**
> Phát hiện này chứng minh các đồng ổn định giá tập trung như USDT/USDC không hoàn toàn phi tập trung và không có tính kháng kiểm duyệt tuyệt đối. Nhà phát hành giữ đặc quyền can thiệp vào tài sản người dùng theo yêu cầu từ cơ quan hành pháp hoặc lệnh trừng phạt quốc tế (OFAC/AML).
