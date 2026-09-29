# SPEC — LAB 4: NHẬN DIỆN HỢP ĐỒNG CÓ RỦI RO

## 1. Mục đích
Trang bị năng lực thẩm định rủi ro hợp đồng thông minh (Smart Contract Risk Assessment) cho chuyên viên phân tích tài sản số, giúp phát hiện sớm các đặc quyền bất lợi (đặc quyền phát hành vô hạn, khóa quyền bán/honeypot) nhằm bảo vệ người dùng và nhà đầu tư khỏi các dự án gian lận.

## 2. Đầu vào
- Mã nguồn 03 hợp đồng token mẫu được cung cấp trong Phụ lục I (Sổ tay thực hành ECO2432):
  1. Hợp đồng A (`ClubTokenA.sol`)
  2. Hợp đồng B (`ClubTokenB.sol`)
  3. Hợp đồng C (`ClubTokenC.sol`)
- Quy chuẩn thẩm định theo mẫu câu lệnh chuẩn tại `prompt_templates.md`.

## 3. Quy tắc nghiệp vụ
- **R1:** Mọi kết luận về đặc quyền quản trị phải được chỉ đích danh tên hàm, quyền truy cập (`onlyOwner`), và **trích dẫn chính xác số dòng mã nguồn** làm bằng chứng kiểm toán.
- **R2:** Phân loại rõ ràng mức độ rủi ro:
  - **Sạch / Không rủi ro (Low/None):** Tổng cung cố định, không có cơ chế can thiệp sau khi triển khai.
  - **Rủi ro lạm phát / Pha loãng (Inflation/Dilution Risk):** Chủ sở hữu có thể tự do phát hành (mint) token mới không giới hạn trần (`MAX_SUPPLY`).
  - **Rủi ro thanh khoản / Khóa tài sản (Honeypot / Blacklist Risk):** Chủ sở hữu có thể đưa ví người dùng vào danh sách hạn chế (`restricted`) để chặn chuyển/bán token.
- **R3:** Thẩm định phải phân biệt giữa lời giải thích trong chú thích (comment/NatSpec) và logic thực thi thực tế của mã lệnh máy ảo EVM.

## 4. Đầu ra
- Tệp `lab04.md`: Bảng kết luận thẩm định 3 hợp đồng A, B, C kèm trích dẫn số dòng và đánh giá tác động tài chính.
- Tệp `AI_JOURNAL.md`: Bảng nhật ký so sánh kết quả đọc thủ công và kết quả do AI phân tích, chỉ rõ các điểm lưu ý khi thẩm định.

## 5. Trường hợp ngoại lệ
- **E1:** Nếu hợp đồng chứa hàm `mint` có `onlyOwner` nhưng có chặn trần `require(totalSupply() + amount <= MAX_SUPPLY)` thì không xếp vào rủi ro vô hạn mà xếp vào mức kiểm soát có giới hạn.
- **E2:** Nếu hợp đồng có cơ chế `restricted` nhưng thiếu phát sự kiện `event` khi chặn ví, mức độ rủi ro tăng lên vì hành vi lạm quyền bị che giấu, không thể giám sát qua log sự kiện on-chain.
- **E3:** Nếu người dùng mua phải token của hợp đồng C (`ClubTokenC`), họ có thể nạp tiền vào mua nhưng khi bị đưa vào `restricted[from]` sẽ hoàn toàn mất khả năng rút vốn hoặc cắt lỗ.

## 6. Ngoài phạm vi
- Không thực hiện tấn công khai thác lỗ hổng bằng hợp đồng thông minh tấn công (chỉ thẩm định tĩnh trên mã nguồn).
- Không kiểm toán các lỗi logic kinh tế phức tạp bên ngoài phạm vi mã nguồn được cung cấp.
