# SPEC — LAB 5: VIẾT ĐẶC TẢ CHO CÔNG CỤ PHÂN TÍCH DÒNG TIỀN

## 1. Mục đích
Xây dựng công cụ phân tích dòng tiền on-chain tự động cho chuyên viên phân tích dữ liệu và kế toán tài sản số, cho phép trích xuất, đối soát lịch sử biến động số dư và trực quan hóa dòng tiền vào/ra của một địa chỉ ví Ethereum trong 90 ngày gần nhất qua Etherscan API.

## 2. Đầu vào
- Một địa chỉ ví Ethereum cần phân tích: dạng chuỗi ký tự 42 ký tự Hexadecimal bắt đầu bằng `0x` (chuẩn EIP-55).
- Khóa API của Etherscan: đọc từ biến môi trường `ETHERSCAN_API_KEY` (không ghi trực tiếp trong mã nguồn theo quy ước `AGENTS.md`).
- Khoảng thời gian phân tích: số ngày cần lấy dữ liệu tính ngược từ thời điểm hiện tại, mặc định là 90 ngày.

## 3. Quy tắc nghiệp vụ
- **R1 (Dòng tiền vào):** Giao dịch có trường `to` trùng khớp với địa chỉ ví đang xét (và trạng thái thành công) được ghi nhận là dòng tiền vào (Inflow). Số tiền cộng vào số dư bằng đúng giá trị trường `value`.
- **R2 (Dòng tiền ra):** Giao dịch có trường `from` trùng khớp với địa chỉ ví đang xét được ghi nhận là dòng tiền ra (Outflow).
- **R3 (Khấu trừ phí giao dịch):** Đối với mọi giao dịch đi ra thành công, tổng số tiền thực trừ khỏi ví bằng `Giá trị chuyển (value) + Phí giao dịch (gasUsed × gasPrice)`.
- **R4 (Xử lý giao dịch thất bại):** Giao dịch do ví gửi đi có trạng thái thất bại (`isError == "1"` hoặc `txreceipt_status == "0"`) thì giá trị chuyển không đi (`value = 0`), nhưng phí gas vẫn bị tiêu hao và phải được tính toàn bộ vào dòng tiền ra.
- **R5 (Chuẩn hóa đơn vị tiền tệ):** Mọi số liệu số dư, dòng tiền và phí thu về từ API ở đơn vị `wei` bắt buộc phải quy đổi sang đơn vị `ETH` bằng cách chia cho $10^{18}$ trước khi tính toán lũy kế và hiển thị.
- **R6 (Thứ tự thời gian):** Toàn bộ giao dịch phải được sắp xếp theo mốc thời gian (`timeStamp`) tăng dần (từ quá khứ đến hiện tại) trước khi tính số dư lũy kế từng thời điểm.
- **R7 (Tự chuyển tiền cho chính mình):** Trường hợp đặc biệt ví tự gửi tiền cho chính mình (`from == to`), giá trị chuyển bù trừ bằng 0, số tiền thực giảm của ví chính bằng phí giao dịch.

## 4. Đầu ra
- **Bảng dữ liệu dòng tiền chi tiết:** Gồm các cột: Mốc thời gian (UTC), Mã băm giao dịch (Tx Hash rút gọn), Loại giao dịch (VÀO / RA), Số lượng ETH chuyển, Phí giao dịch (ETH), và Số dư lũy kế tại thời điểm đó (ETH).
- **Biểu đồ đường trực quan (Balance Timeline):** Trục hoành ($X$) là dòng thời gian (ngày/tháng), trục tung ($Y$) là số dư ví lũy kế (ETH).
- **Báo cáo tóm tắt 3 chỉ số tài chính:**
  1. Tổng dòng tiền vào (Total Inflow).
  2. Tổng dòng tiền ra (Total Outflow bao gồm cả phí gas).
  3. Biến động số dư ròng trong kỳ (Net Balance Change).

## 5. Trường hợp ngoại lệ
- **E1 (Không có giao dịch trong kỳ):** Nếu API trả về danh sách rỗng hoặc ví không phát sinh giao dịch nào trong 90 ngày qua, in thông báo rõ ràng: `"Ví không có giao dịch trong kỳ phân tích"` và dừng chương trình bình thường, không gây lỗi crash/exception.
- **E2 (Lỗi kết nối / Khóa API không hợp lệ):** Nếu API trả về mã lỗi (như `NOTOK`, `Invalid API Key`, hoặc lỗi mạng), in thông báo lỗi chi tiết cùng mã lỗi và dừng chương trình an toàn.
- **E3 (Phân trang với ví có khối lượng giao dịch lớn):** Nếu ví có hơn 10.000 giao dịch (vượt giới hạn 1 trang của Etherscan API), hệ thống phải tự động lặp phân trang (`page`, `offset`) để thu thập đầy đủ toàn bộ giao dịch trong kỳ.
- **E4 (Định dạng địa chỉ không hợp lệ):** Nếu người dùng nhập chuỗi không đúng chuẩn 42 ký tự hoặc sai cấu trúc Hex, hệ thống từ chối xử lý và yêu cầu nhập lại trước khi gọi API.

## 6. Ngoài phạm vi
- Không phân tích các giao dịch chuyển token ERC-20 / ERC-721 / ERC-1155 (chỉ tập trung vào đồng tiền gốc ETH).
- Không tự động quy đổi tỷ giá biến động sang tiền pháp định (USD / VND) trong bài này.
- Không hỗ trợ gửi lệnh giao dịch hoặc can thiệp vào tài khoản ví (công cụ chỉ đọc dữ liệu on-chain).
