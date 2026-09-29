# SPEC — LAB 6: SINH MÃ BẰNG AI VÀ KIỂM TRA KẾT QUẢ

## 1. Mục đích
Triển khai chương trình Python hoàn chỉnh thực thi công cụ phân tích dòng tiền ví on-chain theo đúng đặc tả `LAB5/SPEC.md`, tiến hành rà soát bắt lỗi mã nguồn do AI sinh ra dựa trên danh mục 6 tiêu chí kiểm tra bắt buộc.

## 2. Đầu vào
- Địa chỉ ví Ethereum hợp lệ (42 ký tự Hex bắt đầu bằng `0x`).
- Khóa API Etherscan đọc từ biến môi trường `ETHERSCAN_API_KEY`.
- Số ngày phân tích: mặc định 90 ngày.

## 3. Quy tắc nghiệp vụ
- **R1 (Dòng tiền vào):** `to == walletAddress` (thành công) $\rightarrow$ cộng giá trị `value` (ETH).
- **R2 (Dòng tiền ra):** `from == walletAddress` $\rightarrow$ trừ số tiền `value + gasFee` (ETH).
- **R3 (Khấu trừ phí gas):** Phí giao dịch $= \text{gasUsed} \times \text{gasPrice} \div 10^{18}$.
- **R4 (Xử lý giao dịch thất bại):** Giao dịch thất bại vẫn phải trừ phí gas vào dòng tiền ra (`value = 0`).
- **R5 (Chuẩn hóa Wei sang ETH):** Toàn bộ số liệu chia $10^{18}$ trước khi tính toán số dư lũy kế.
- **R6 (Sắp xếp thời gian):** Sắp xếp danh sách giao dịch theo `timeStamp` tăng dần.
- **R7 (Tự chuyển tiền):** `from == to` $\rightarrow$ giá trị chuyển triệt tiêu, dòng tiền ra bằng đúng phí gas.

## 4. Đầu ra
- Bảng dữ liệu dòng tiền chi tiết in ra màn hình hoặc xuất tệp.
- Biểu đồ đường biến động số dư theo thời gian (`balance_chart.png`).
- 3 chỉ số tài chính tổng hợp: Tổng dòng tiền vào, Tổng dòng tiền ra, Số dư ròng trong kỳ.

## 5. Danh mục 6 điểm kiểm tra bắt buộc (Audit Checklist)
1. **Đơn vị tiền:** Chia $10^{18}$, không hiển thị số nguyên 19 chữ số.
2. **Khóa API:** Đọc từ biến môi trường `ETHERSCAN_API_KEY`, không hardcode vào mã nguồn.
3. **Phân trang:** Xử lý lặp phân trang (`page`, `offset`) khi ví có nhiều giao dịch.
4. **Giao dịch thất bại:** Tính phí gas của giao dịch lỗi vào dòng tiền ra.
5. **Xử lý lỗi:** Thử khóa API sai / lỗi mạng $\rightarrow$ báo lỗi rõ ràng, dừng an toàn không crash.
6. **Phiên bản API:** Dùng đúng endpoint API chuẩn của Etherscan.

## 6. Ngoài phạm vi
- Không phân tích token phụ (ERC-20/721).
- Không tự động quy đổi ngoại tệ USD/VND.
