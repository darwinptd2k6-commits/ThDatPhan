# SPEC — LAB 7: PHÂN TÍCH VÀ ƯỚC TÍNH CHI PHÍ VẬN HÀNH TRÊN ON-CHAIN & LAYER 2

## 1. Mục đích
Hệ thống giải quyết bài toán ước tính và phân tích chi phí vận hành (gas fee) cho ứng dụng thẻ tích điểm sinh viên khi triển khai trên Ethereum Mainnet so với giải pháp mở rộng Layer 2, giúp nhà quản trị và kế toán tài sản số đưa ra quyết định kiến trúc kinh tế tối ưu.

## 2. Đầu vào
- **Tần suất giao dịch ($N$):** $1.000$ lượt cộng điểm / tháng.
- **Mức tiêu thụ Gas ($G$):** $20.000$ gas cho mỗi lượt ghi nhận một biến trạng thái mới trên smart contract.
- **Đơn vị giá Gas ($P_{\text{gas}}$):** $20$ Gwei trên Ethereum Mainnet.
- **Tỷ giá ETH tham chiếu ($P_{\text{ETH}}$):** $3.000$ USD / ETH.
- **Tỷ lệ giảm phí của Layer 2 ($R_{\text{L2}}$):** Rẻ hơn Ethereum Mainnet $100$ lần.

## 3. Quy tắc nghiệp vụ và Công thức tính toán
- **R1 (Tính phí 1 giao dịch ETH trên Mainnet):**
  $$\text{Phí 1 Tx (ETH)} = \text{Gas tiêu thụ} \times \text{Đơn giá Gwei} \times 10^{-9} = 20.000 \times 20 \times 10^{-9} = 0,0004\text{ ETH}$$
- **R2 (Tính phí 1 giao dịch USD trên Mainnet):**
  $$\text{Phí 1 Tx (USD)} = \text{Phí 1 Tx (ETH)} \times \text{Tỷ giá ETH} = 0,0004 \times 3.000 = 1,20\text{ USD}$$
- **R3 (Tính tổng chi phí tháng trên Mainnet):**
  - Bằng ETH: $\text{Tổng phí (ETH)} = 1.000 \times 0,0004 = 0,4\text{ ETH}$
  - Bằng USD: $\text{Tổng phí (USD)} = 1.000 \times 1,20 = 1.200\text{ USD}$
- **R4 (Tính chi phí trên Layer 2):**
  - Toàn bộ chi phí (từng giao dịch và tổng tháng) trên Layer 2 bằng chi phí Mainnet chia cho $100$:
    - Phí 1 Tx L2: $0,000004\text{ ETH}$ ($0,012\text{ USD}$).
    - Tổng phí tháng L2: $0,004\text{ ETH}$ ($12\text{ USD}$).
- **R5 (Phân tích hiệu quả kinh tế):** Tiết kiệm $99\%$ ngân sách vận hành ($1.188\text{ USD/tháng}$).

## 4. Đầu ra
- Bảng so sánh chi phí chi tiết đa chiều (Đơn vị tính: Gas, Gwei, ETH, USD theo từng giao dịch và tổng tháng).
- Báo cáo phân tích tài chính và khuyến nghị triển khai kiến trúc.

## 5. Trường hợp ngoại lệ
- **TH1 (Gas spike):** Khi giá gas Mainnet biến động tăng vọt (ví dụ lên 50-100 Gwei), hệ thống phải giữ nguyên mô hình tính toán tương đối và cảnh báo rủi ro biến động ngân sách.
- **TH2 (ETH price volatility):** Khi giá ETH biến động, chi phí bằng ETH không đổi nhưng chi phí USD biến động theo tỷ lệ thuận.
- **TH3 (Giao dịch không hợp lệ):** Lượt cộng điểm thất bại do sai quyền hoặc hết gas vẫn làm tiêu tốn gas của người gọi (theo quy tắc on-chain).

## 6. Ngoài phạm vi
- Không tính chi phí chuyển cầu nối (Bridge fee) tài sản từ L1 sang L2.
- Không tính chi phí triển khai hợp đồng khởi tạo ban đầu (Deployment Gas Fee).
