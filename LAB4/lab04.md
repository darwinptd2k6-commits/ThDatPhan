# BÁO CÁO THẨM ĐỊNH RỦI RO HỢP ĐỒNG — LAB 4: NHẬN DIỆN HỢP ĐỒNG CÓ RỦI RO

---

## 1. Bảng kết luận thẩm định 3 hợp đồng mẫu

| Hợp đồng | Kết luận | Tên hàm | Số dòng | Người được gọi | Mức độ | Rủi ro cụ thể cho người nắm giữ token |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Hợp đồng A**<br>*(ClubTokenA)* | **Sạch**<br>*(Không có rủi ro đặc quyền)* | Không có | Không có | Không có | An toàn | Tổng cung cố định 1,000,000 token được đúc 1 lần duy nhất trong constructor (Dòng 8). Không có quyền quản trị đặc biệt hay hàm can thiệp số dư sau khi khởi tạo. |
| **Hợp đồng B**<br>*(ClubTokenB)* | **Có rủi ro**<br>*(Pha loãng vô hạn)* | `mint(address to, uint256 amount)` | Dòng 14 – 16 | `onlyOwner`<br>*(Chủ sở hữu)* | **Nghiêm trọng (Cao)** | Chủ sở hữu có thể tùy ý phát hành thêm token không giới hạn số lượng và thời gian. Khi chủ sở hữu mint lượng lớn token ra bán, nguồn cung tăng đột biến làm giá trị token của người nắm giữ bị giảm về gần 0 (Rug Pull / Inflation attack). |
| **Hợp đồng C**<br>*(ClubTokenC)* | **Có rủi ro**<br>*(Bẫy thanh khoản / Khóa ví)* | `setRestricted(address user, bool status)` kết hợp `_update(...)` | Dòng 15 – 17 và Dòng 19 – 22 | `onlyOwner`<br>*(Chủ sở hữu)* | **Nghiêm trọng (Cao)** | Chủ sở hữu có quyền tùy ý đưa bất kỳ ví nào vào danh sách hạn chế (`restricted[user] = true`). Khi đó, điều kiện `require(!restricted[from])` tại dòng 20 sẽ chặn hoàn toàn lệnh gửi/bán token của nạn nhân. Người mua mua vào được nhưng không thể bán ra (Honeypot). |

---

## 2. Chi tiết phân tích & Trích dẫn bằng chứng mã nguồn

### 2.1. Hợp đồng A (`ClubTokenA.sol`) — Hợp đồng đối chứng sạch
```solidity
1: // SPDX-License-Identifier: MIT
2: pragma solidity ^0.8.20;
3: 
4: import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
5: 
6: /// @title Token cau lac bo - khong co quyen dac biet nao
7: contract ClubTokenA is ERC20 {
8:     constructor() ERC20("Club Token A", "CTA") {
9:         _mint(msg.sender, 1_000_000 * 10 ** decimals());
10:    }
11: }
```
- **Phân tích:** Hợp đồng không kế thừa `Ownable`, không có bất kỳ hàm ngoại vi (`external`/`public`) nào cho phép thay đổi trạng thái hoặc đúc thêm token sau khi hoàn tất hàm khởi tạo tại dòng 8–10.

---

### 2.2. Hợp đồng B (`ClubTokenB.sol`) — Rủi ro đúc vô hạn (Unlimited Minting)
```solidity
1: // SPDX-License-Identifier: MIT
2: pragma solidity ^0.8.20;
3: 
4: import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
5: import "@openzeppelin/contracts/access/Ownable.sol";
6: 
7: /// @title Token cau lac bo - ban B
8: contract ClubTokenB is ERC20, Ownable {
9:     constructor() ERC20("Club Token B", "CTB") Ownable(msg.sender) {
10:        _mint(msg.sender, 1_000_000 * 10 ** decimals());
11:    }
12: 
13:    /// @notice Phat hanh them token de phuc vu chuong trinh khuyen mai
14:    function mint(address to, uint256 amount) external onlyOwner {
15:        _mint(to, amount);
16:    }
17: }
```
- **Bằng chứng số dòng:** Dòng 14–16 chứa hàm `mint(address to, uint256 amount) external onlyOwner`.
- **Đánh giá thẩm định:** Chú thích tại dòng 13 ghi "phục vụ chương trình khuyến mại", tạo cảm giác vô hại. Tuy nhiên về mặt kỹ thuật, hàm hoàn toàn thiếu điều kiện kiểm tra trần tổng cung (`MAX_SUPPLY`). Chủ sở hữu có thể mint hàng triệu token về ví cá nhân để bán tháo ra thị trường.
- **Đề xuất khắc phục:** Thiết lập hằng số trần tổng cung cố định:
  ```solidity
  uint256 public constant MAX_SUPPLY = 2_000_000 * 10 ** 18;
  function mint(address to, uint256 amount) external onlyOwner {
      require(totalSupply() + amount <= MAX_SUPPLY, "Vuot tran tong cung");
      _mint(to, amount);
  }
  ```

---

### 2.3. Hợp đồng C (`ClubTokenC.sol`) — Bẫy khóa bán (Honeypot / Blacklist)
```solidity
1: // SPDX-License-Identifier: MIT
2: pragma solidity ^0.8.20;
3: 
4: import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
5: import "@openzeppelin/contracts/access/Ownable.sol";
6: 
7: /// @title Token cau lac bo - ban C
8: contract ClubTokenC is ERC20, Ownable {
9:     // Danh sach dia chi bi han che de bao ve cong dong
10:    mapping(address => bool) public restricted;
11: 
12:    constructor() ERC20("Club Token C", "CTC") Ownable(msg.sender) {
13:        _mint(msg.sender, 1_000_000 * 10 ** decimals());
14:    }
15: 
16:    function setRestricted(address user, bool status) external onlyOwner {
17:        restricted[user] = status;
18:    }
19: 
20:    function _update(address from, address to, uint256 value) internal override {
21:        require(!restricted[from], "Dia chi bi han che");
22:        super._update(from, to, value);
23:    }
24: }
```
- **Bằng chứng số dòng:**
  - Dòng 16–18: Hàm `setRestricted(address user, bool status) external onlyOwner` cho phép chủ sở hữu tự ý thay đổi cờ trạng thái bị khóa của bất kỳ tài khoản nào mà không cần sự đồng thuận của người dùng.
  - Dòng 20–23: Hàm `_update` chèn kiểm tra `require(!restricted[from], "Dia chi bi han che")` tại dòng 21. Khi `from` bị hạn chế, giao dịch chuyển đi/bán ra sẽ bị revert ngay lập tức.
- **Đánh giá thẩm định:** Không có thời hạn mở khóa tự động, không có cơ chế phân xử tranh chấp phi tập trung (multi-sig / DAO), và không phát sự kiện (`event Restricted(...)`) để cộng đồng giám sát hành vi lạm quyền.

---

## 3. Bài học kinh nghiệm & Kết luận nghiệp vụ
1. **Không tin vào chú thích (NatSpec):** Các dự án lừa đảo thường dùng lời giải thích tích cực (như "bảo vệ cộng đồng", "chương trình khuyến mại") để ngụy trang cho các đặc quyền nguy hiểm.
2. **Minh bạch mã nguồn là điều kiện tiên quyết:** Mọi dự án không công bố mã nguồn đã xác thực (Verified) trên Etherscan đều tiềm ẩn nguy cơ cao chứa các hàm `mint` vô hạn hoặc `blacklist` tương tự như Hợp đồng B và C.
