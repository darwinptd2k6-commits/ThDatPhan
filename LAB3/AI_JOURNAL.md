# NHẬT KÝ LÀM VIỆC VỚI AI — LAB 3: ĐỌC GIAO DỊCH VÀ HỢP ĐỒNG TRÊN ETHERSCAN

## Lần 1: Xây dựng đặc tả, mổ xẻ giao dịch on-chain và thẩm định hợp đồng USDT

**Prompt:**
> Từ giao dịch bởi 2 mã địa chỉ ví ở Lab2, hãy tiếp tục thực hiện Lab3: Đọc giao dịch và hợp đồng trên Etherscan

**AI trả về:**
> AI đã phân tích chi tiết yêu cầu của Lab 3 từ Sổ tay thực hành ECO2432 (Trang 11-12):
> 1. Xây dựng bản đặc tả kỹ thuật `SPEC.md` theo chuẩn cấu trúc 6 phần, bổ sung các quy tắc nghiệp vụ về kiểm toán on-chain.
> 2. Sử dụng mã băm giao dịch thực tế từ Lab 2 (`0xa86f43080e63535b6bde87668ae0f6877056bb7ab0ee4c7c4b5e1b0336ec1bc4`) để mổ xẻ đầy đủ 8 trường thông tin cốt lõi (Status, Block, Timestamp, From/To, Value, Tx Fee, Gas Price, Nonce) gắn với góc nhìn nghiệp vụ kế toán/tuân thủ AML.
> 3. Lập báo cáo `forensics.md` thẩm định hợp đồng USDT (`0xdAC17F958D2ee523a2206206994597C13D831ec7`), phân biệt Bytecode vs Verified Code, Read vs Write Contract và làm rõ cơ chế đóng băng tài khoản qua hàm `addBlackList()`.

**Đánh giá:** [Đạt] Dùng được ngay, rất chi tiết và chuẩn xác.

**Chỗ sai:** Không có.

**Cách sửa:** Không cần sửa. Số liệu khớp chính xác với dữ liệu chuỗi khối và mã nguồn trên Ethereum Mainnet.

**Ai phát hiện:** Sinh viên kiểm tra và xác nhận.
