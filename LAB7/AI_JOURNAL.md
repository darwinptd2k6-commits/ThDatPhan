# NHẬT KÝ LÀM VIỆC VỚI AI — LAB 7: ƯỚC TÍNH CHI PHÍ VẬN HÀNH GAS & LAYER 2

## Lần 1

**Prompt:** 
> Bạn là chuyên viên phân tích tài chính và kế toán tài sản số. Hãy giúp tôi giải bài toán tính chi phí vận hành cho ứng dụng thẻ tích điểm sinh viên với các thông số sau:
> Mỗi tháng có 1.000 lượt cộng điểm (mỗi lượt ghi 1 biến mới ~20.000 gas). Đơn giá Gas trên Ethereum Mainnet: 20 Gwei. Giá ETH tham chiếu: 3.000 USD. Mạng Layer 2 rẻ hơn Ethereum Mainnet 100 lần.
> Yêu cầu:
> + Tính chi phí 1 giao dịch và tổng chi phí 1 tháng (bằng ETH và USD) trên Ethereum Mainnet (sử dụng công thức: Phí ETH = Gas tiêu thụ × Đơn giá Gwei × $10^{-9}$).
> + Tính chi phí tương ứng trên mạng Layer 2.
> + Trình bày dưới dạng bảng so sánh chi tiết. Chỉ tính toán dựa trên công thức và dữ liệu tôi cung cấp, không suy đoán ngoài phạm vi.

**AI trả về:** 
- Tính toán chính xác chi phí 1 giao dịch và tổng tháng trên Ethereum Mainnet ($0,0004$ ETH / $1,20$ USD và $0,4$ ETH / $1.200$ USD).
- Tính toán chính xác chi phí tương ứng trên Layer 2 ($0,000004$ ETH / $0,012$ USD và $0,004$ ETH / $12$ USD).
- Trình bày bảng so sánh đối chiếu đa chiều, đầy đủ các đơn vị tính Gas, Gwei, ETH, USD và mức tiết kiệm $99\%$ ($1.188$ USD/tháng).
- Tạo đầy đủ tài liệu đặc tả `SPEC.md`, báo cáo thực hành `lab07.md` và mã nguồn kiểm chứng tự động `gas_cost_calculator.py` trong thư mục `LAB7`.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không có sai sót toán học hay logic. Đã tuân thủ nghiêm ngặt công thức và dữ liệu được cung cấp.

**Cách sửa:** Sinh viên kiểm tra đối chiếu công thức toán học và chạy script Python `gas_cost_calculator.py` để tự động hóa kiểm thử kết quả.

**Ai phát hiện:** AI thực hiện chính xác, sinh viên nghiệm thu.

---

## Lần 2

**Prompt:** 
> Bạn là chuyên viên thẩm định rủi ro dự án Web3. Dựa trên kết quả tính toán chi phí ở Prompt 1 (Lần 1 trong AI_JOURNAL.md) (1.200 USD/tháng trên Mainnet vs 12 USD/tháng trên Layer 2), hãy phân tích:
> Nếu sinh viên tự trả phí (~1,20 USD/lượt trên Mainnet vs ~0,012 USD/lượt trên Layer 2), sinh viên có chấp nhận không? Vì sao?
> Nếu Câu lạc bộ tài trợ phí, mức ngân sách nào là thực tế cho một CLB sinh viên?
> Đưa ra kết luận ngắn gọn về tính khả thi của mô hình này trên Ethereum Mainnet và Layer 2. Trả lời dưới góc độ tài chính thực tế và trải nghiệm người dùng.

**AI trả về:** 
- Phân tích chi tiết rủi ro tài chính và rào cản UX: Sinh viên từ chối trả $1,20$ USD/lượt vì cao hơn giá trị tích điểm; trong khi $0,012$ USD/lượt trên Layer 2 là hoàn toàn khả thi.
- Thẩm định ngân sách CLB: Ngân sách $1.200$ USD/tháng (~30 triệu VNĐ) trên Mainnet là phi thực tế; ngân sách $12$ USD/tháng (~300.000 VNĐ) trên Layer 2 hoàn toàn nằm trong quỹ hoạt động và có thể tài trợ qua Paymaster.
- Kết luận: Mô hình Bất khả thi trên Ethereum Mainnet và Khả thi tuyệt đối trên Layer 2.

**Đánh giá:** Dùng được.

**Chỗ sai:** Không có.

**Cách sửa:** Đồng bộ phân tích vào mục 4 của `lab07.md`.

**Ai phát hiện:** AI thực hiện chính xác, sinh viên nghiệm thu.
