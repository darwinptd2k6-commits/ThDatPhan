# NHẬT KÝ LÀM VIỆC VỚI AI — LAB 5: VIẾT ĐẶC TẢ CHO CÔNG CỤ PHÂN TÍCH DÒNG TIỀN

## Lần 1: Xây dựng đặc tả yêu cầu nghiệp vụ theo vai trò Business Analyst (BA)

**Prompt:**
> Tiếp tục thực hiện Viết đặc tả cho công cụ phân tích dòng tiền (LAB 5). Xây dựng đặc tả chi tiết 6 phần theo chuẩn Sổ tay thực hành ECO2432, không viết mã nguồn trong buổi này.

**AI trả về:**
> AI đã xây dựng hoàn chỉnh tệp `SPEC.md` với đầy đủ 6 phần:
> 1. Mục đích công cụ phân tích dòng tiền on-chain.
> 2. Các tham số đầu vào (Địa chỉ ví, biến môi trường `ETHERSCAN_API_KEY`, số ngày phân tích).
> 3. Hệ thống 7 quy tắc nghiệp vụ rõ ràng (R1–R7), bao gồm cơ chế tính dòng vào, dòng ra, trừ phí gas, xử lý giao dịch fail, quy đổi đơn vị Wei sang ETH, sắp xếp thời gian và trường hợp tự chuyển tiền cho chính mình.
> 4. Định dạng đầu ra chi tiết (Bảng dữ liệu, biểu đồ đường số dư lũy kế, 3 chỉ số tài chính tổng hợp).
> 5. 4 trường hợp ngoại lệ (E1–E4) xử lý lỗi API, danh sách rỗng, phân trang trên 10.000 tx và kiểm tra định dạng địa chỉ.
> 6. Giới hạn ngoài phạm vi dự án.

**Đánh giá:** [Đạt] Bản đặc tả rất chặt chẽ, đầy đủ logic để bàn giao cho đội kỹ thuật hoặc công cụ AI sinh mã ở Lab 6 mà không bị hiểu sai lệch.

**Chỗ sai:** Không có.

**Cách sửa:** Không cần sửa.

**Ai phát hiện:** Sinh viên kiểm tra và xác nhận.

---

## Biên bản Kiểm tra chéo (Peer Review theo Bước 3 - Sổ tay Lab 5)

* **Nhóm thực hiện đặc tả:** Nhóm K58 Fintech/MIS
* **Nhóm kiểm tra chéo:** Nhóm phản biện bên cạnh

### 2 điểm mơ hồ được chỉ ra và cách khắc phục:
1. **Chỗ mơ hồ 1:** *Trường hợp ví tự gửi tiền cho chính mình (`from == to`) thì tính dòng tiền vào hay ra?*
   - **Cách khắc phục:** Đã bổ sung quy tắc **R7**: Giá trị chuyển tự triệt tiêu, chỉ tính dòng tiền ra bằng đúng khoản phí gas thực tế tiêu tốn.
2. **Chỗ mơ hồ 2:** *Nếu ví có lịch sử hoạt động khổng lồ vượt qua giới hạn 10.000 giao dịch trả về của 1 truy vấn Etherscan API thì sao?*
   - **Cách khắc phục:** Đã làm rõ tại ngoại lệ **E3**: Yêu cầu công cụ phải cài đặt cơ chế lặp phân trang (`pagination`) với các tham số `page` và `offset` để thu thập đủ 100% dữ liệu trong kỳ phân tích.
