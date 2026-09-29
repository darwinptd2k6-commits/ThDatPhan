# NHẬT KÝ LÀM VIỆC VỚI AI — LAB 4: NHẬN DIỆN HỢP ĐỒNG CÓ RỦI RO

## Lần 1: Thẩm định rủi ro 3 hợp đồng mẫu theo vai trò chuyên viên

**Prompt:**
> Bạn là chuyên viên thẩm định rủi ro tài sản số. Liệt kê mọi quyền đặc biệt trong mã nguồn dưới đây. Với mỗi quyền, nêu tên hàm, số dòng, người được gọi và rủi ro cho người dùng. Chỉ kết luận từ mã được cung cấp; nếu không đủ dữ liệu, nói rõ phần còn thiếu.

**AI trả về:**
> AI đã phân tích chi tiết mã nguồn 3 hợp đồng `ClubTokenA`, `ClubTokenB`, `ClubTokenC`:
> - Nhận diện Hợp đồng A sạch, không có hàm đặc quyền.
> - Phát hiện hàm `mint()` tại dòng 14-16 của Hợp đồng B chỉ dành cho `onlyOwner`, gây nguy cơ lạm phát vô hạn.
> - Phát hiện hàm `setRestricted()` tại dòng 16-18 và điều kiện chặn `require(!restricted[from])` tại dòng 21 của Hợp đồng C, chỉ ra nguy cơ tạo bẫy honeypot khóa quyền bán.
> - Đưa ra các trích dẫn số dòng cụ thể và đề xuất hướng khắc phục kỹ thuật.

**Đánh giá:** [Đạt] Phân tích chính xác, đầy đủ bằng chứng số dòng.

**Chỗ sai:** Không có lỗi sai logic hay số dòng.

**Cách sửa:** Không cần sửa. Nội dung đáp ứng hoàn hảo tiêu chí kiểm toán mã nguồn theo Sổ tay thực hành ECO2432.

**Ai phát hiện:** Sinh viên kiểm tra, đối chiếu trực tiếp với mã nguồn và xác nhận.

---

## Lần 2: Sinh mã an toàn từ đặc tả, Tự rà soát và Sinh ca kiểm thử toàn diện

**Prompt:**
> Thực hiện 3 quy trình chuẩn: Sinh mã từ đặc tả (liệt kê giả định, điểm chưa rõ, trường hợp biên; tuân thủ AGENTS.md) -> Tự rà soát (tìm phản ví dụ, đề xuất ca làm hỏng mã) -> Sinh ca kiểm thử (luồng đúng, sai quyền, giá trị biên, rỗng, gian lận).

**AI trả về:**
> AI đã phân tích cặn kẽ:
> 1. Liệt kê đầy đủ các giả định và trường hợp biên trước khi viết mã.
> 2. Thiết kế hợp đồng `ClubTokenSafe.sol` (OpenZeppelin 5.x, dùng `_update`, `error` tùy biến, giới hạn `MAX_SUPPLY`, phát `event` đầy đủ).
> 3. Tự rà soát và chỉ rõ 3 phản ví dụ tiềm ẩn (rủi ro tập trung hóa khóa Owner, trần cứng không thể hạ, và bẫy khóa chuyển nhượng).
> 4. Xây dựng ma trận 5 ca kiểm thử chi tiết bao gồm kịch bản gian lận đúc token và vượt mặt danh sách hạn chế.

**Đánh giá:** [Đạt] Xuất sắc, đúng chuẩn quy ước `AGENTS.md`.

**Chỗ sai:** Không có.

**Cách sửa:** Không cần sửa.

**Ai phát hiện:** Sinh viên kiểm tra và xác nhận.
