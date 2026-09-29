# BÁO CÁO THỰC HÀNH — LAB 7: TÍNH CHI PHÍ VẬN HÀNH THỰC TẾ

## 1. Công thức tính chi phí Gas nền tảng
- **Phí một giao dịch (ETH):**
  $$\text{Phí một giao dịch (ETH)} = \text{Lượng gas tiêu thụ} \times \text{Đơn giá gas (Gwei)} \times 10^{-9}$$
- **Chi phí quy đổi (USD):**
  $$\text{Chi phí quy đổi (USD)} = \text{Phí giao dịch (ETH)} \times \text{Giá ETH (USD)}$$

---

## 2. Giải bài toán vận hành Thẻ tích điểm Sinh viên

### Bối cảnh đề bài:
- **Tần suất hoạt động:** $1.000$ lượt cộng điểm / tháng.
- **Lượng gas tiêu thụ:** Ghi $1$ biến mới $= 20.000\text{ gas}$ / lượt.
- **Đơn giá gas Ethereum Mainnet:** $20\text{ Gwei}$.
- **Giá ETH tham chiếu:** $3.000\text{ USD/ETH}$.
- **Mạng Layer 2:** Đơn giá rẻ hơn Mainnet khoảng $100$ lần.

---

### a. Chi phí một tháng trên Ethereum Mainnet
- **Phí cho 1 lượt cộng điểm (giao dịch):**
  $$\text{Phí 1 Tx (ETH)} = 20.000 \times 20 \times 10^{-9} = 0,0004\text{ ETH}$$
  $$\text{Phí 1 Tx (USD)} = 0,0004 \times 3.000\text{ USD} = 1,20\text{ USD}$$
- **Tổng chi phí 1 tháng ($1.000$ lượt):**
  $$\text{Tổng phí tháng (ETH)} = 1.000 \times 0,0004\text{ ETH} = 0,4\text{ ETH}$$
  $$\text{Tổng phí tháng (USD)} = 1.000 \times 1,20\text{ USD} = \mathbf{1.200\text{ USD}}\text{/tháng}\; (\sim 30.000.000\text{ VNĐ})$$

---

### b. Chi phí khi chuyển sang mạng Layer 2 (Rẻ hơn 100 lần)
- **Phí cho 1 lượt cộng điểm trên Layer 2:**
  $$\text{Phí 1 Tx L2 (ETH)} = \frac{0,0004\text{ ETH}}{100} = 0,000004\text{ ETH}$$
  $$\text{Phí 1 Tx L2 (USD)} = \frac{1,20\text{ USD}}{100} = 0,012\text{ USD}\; (\sim 300\text{ VNĐ})$$
- **Tổng chi phí 1 tháng trên Layer 2 ($1.000$ lượt):**
  $$\text{Tổng phí tháng L2 (ETH)} = \frac{0,4\text{ ETH}}{100} = 0,004\text{ ETH}$$
  $$\text{Tổng phí tháng L2 (USD)} = \frac{1.200\text{ USD}}{100} = \mathbf{12\text{ USD}}\text{/tháng}\; (\sim 300.000\text{ VNĐ})$$

---

### 📊 Bảng so sánh chi phí chi tiết

| Hạng mục chi phí | Ethereum Mainnet | Layer 2 (Arbitrum / Optimism / Base) | Chênh lệch / Tiết kiệm |
| :--- | :---: | :---: | :---: |
| **Lượng gas tiêu thụ / lượt** | $20.000\text{ gas}$ | $20.000\text{ gas}$ | $0\text{ gas}$ |
| **Đơn giá Gas quy đổi** | $20\text{ Gwei}$ | $0,2\text{ Gwei}$ (tương đương) | Giảm $100$ lần |
| **Phí 1 giao dịch (ETH)** | **$0,000400\text{ ETH}$** | **$0,000004\text{ ETH}$** | Tiết kiệm $0,000396\text{ ETH}$ |
| **Phí 1 giao dịch (USD)** | **$1,2000\text{ USD}$** | **$0,0120\text{ USD}$** ($\sim 300\text{ VNĐ}$) | Tiết kiệm $1,1880\text{ USD}$ |
| **Tổng chi phí 1 tháng (ETH)** | **$0,400000\text{ ETH}$** | **$0,004000\text{ ETH}$** | Tiết kiệm $0,396000\text{ ETH}$ |
| **Tổng chi phí 1 tháng (USD)** | **$1.200,00\text{ USD}$** | **$12,00\text{ USD}$** | **Tiết kiệm $1.188,00\text{ USD}$ ($99,0\%$)** |

---

### c. Ai trả khoản này? Phân tích mức độ chấp nhận và tính thực tế
1. **Trường hợp sinh viên tự trả phí:**
   - **Trên Mainnet (~1,20 USD $\approx$ 30.000 VNĐ / lượt):** **Sinh viên chắc chắn KHÔNG chấp nhận**. Mỗi lần cộng điểm thưởng học tập/hoạt động chỉ mang lại ưu đãi nhỏ (vài nghìn đồng), việc bắt sinh viên trả 30.000 VNĐ phí gas là nghịch lý kinh tế (phí gas đắt hơn giá trị nhận được).
   - **Trên Layer 2 (~0,012 USD $\approx$ 300 VNĐ / lượt):** **Sinh viên DỄ DÀNG chấp nhận**. Mức phí 300 VNĐ là rất nhỏ (tương đương 1 tin nhắn SMS), có thể khấu trừ nhẹ vào quyền lợi điểm thưởng.

2. **Trường hợp Câu lạc bộ tài trợ phí:**
   - **Trên Mainnet ($1.200 USD/tháng $\approx$ 30 triệu VNĐ/tháng $\rightarrow$ 360 triệu VNĐ/năm):** **Hoàn toàn phi thực tế** đối với ngân sách một câu lạc bộ sinh viên.
   - **Trên Layer 2 ($12 USD/tháng $\approx$ 300.000 VNĐ/tháng $\rightarrow$ 3,6 triệu VNĐ/năm):** **Cực kỳ thực tế và khả thi**. CLB có thể trích từ quỹ thường niên hoặc xin tài trợ để chi trả thông qua cơ chế *Paymaster* (ERC-4337 - Tài khoản trừu tượng), giúp sinh viên nhận điểm hoàn toàn miễn phí (*Gasless Transaction*).

---

### d. Kết luận về tính khả thi
- **Ethereum Mainnet:** **BẤT KHẢ THI (Infeasible)** về cả mặt tài chính lẫn trải nghiệm người dùng. Chi phí vận hành cao gấp nhiều lần giá trị thực tế của nghiệp vụ.
- **Mạng Layer 2:** **KHẢ THI TUYỆT ĐỐI (Highly Feasible)**. Đây là nền tảng bắt buộc để ứng dụng thẻ tích điểm sinh viên có thể vận hành ổn định, mở rộng quy mô và ứng dụng vào thực tế.

---

## 3. Mở rộng cho ý tưởng đồ án nhóm

Áp dụng khung tính toán trên cho ý tưởng đồ án **"Két ký quỹ mua bán đồ cũ KTX / Đặt cọc mượn thiết bị CLB"**:
- **Tần suất dự kiến:** $200$ hợp đồng ký quỹ / tháng.
- **Các thao tác chính trong chu trình:**
  1. Người mua nạp cọc (`deposit` / `fund`): $\sim 45.000\text{ gas}$.
  2. Người mua xác nhận nhận hàng (`confirmReceived` - chuyển tiền cho người bán): $\sim 35.000\text{ gas}$.
  - Tổng gas tiêu thụ cho 1 chu trình hoàn chỉnh: $\sim 80.000\text{ gas}$.
- **Ước tính chi phí hàng tháng:**
  - **Trên Mainnet (20 Gwei, 3.000 USD/ETH):**
    $$\text{Phí 1 chu trình} = 80.000 \times 20 \times 10^{-9} \times 3.000 = 4,80\text{ USD}$$
    $$\text{Tổng tháng (200 ca)} = 200 \times 4,80 = \mathbf{960\text{ USD/tháng}}\; (\text{Bất khả thi})$$
  - **Trên Layer 2 (Rẻ hơn 100 lần):**
    $$\text{Phí 1 chu trình L2} = \frac{4,80\text{ USD}}{100} = 0,048\text{ USD}\; (\sim 1.200\text{ VNĐ})$$
    $$\text{Tổng tháng L2 (200 ca)} = \mathbf{9,60\text{ USD/tháng}}\; (\sim 240.000\text{ VNĐ/tháng})\; \rightarrow \mathbf{Khả\; thi\; cao}$$
- **Quyết định kiến trúc của nhóm:** Toàn bộ Smart Contract của đồ án nhóm sẽ được định hướng triển khai trên các mạng Layer 2 (Arbitrum/Optimism/Base) để đảm bảo phí giao dịch dưới 2.000 VNĐ/giao dịch.
