# NHẬT KÝ LÀM VIỆC VỚI AI — LAB 6: SINH MÃ BẰNG AI VÀ KIỂM TRA KẾT QUẢ

---

## Lần 1: Giao đặc tả cho công cụ AI và rà soát lỗi

**Prompt:**
> Đọc tệp `SPEC.md` trong dự án và viết chương trình Python thực hiện đúng đặc tả đó. Tuân thủ các quy ước trong `AGENTS.md`. Trước khi viết mã, tóm tắt lại cách bạn hiểu yêu cầu để tôi xác nhận.

**AI trả về:**
> AI đã tóm tắt đầy đủ logic phân tích dòng tiền vào/ra, quy đổi đơn vị Wei sang ETH, cơ chế tính phí gas của giao dịch thất bại và đề xuất kiến trúc chương trình `wallet_flow_analyzer.py`.

**Đánh giá:** [Lưu ý] Phải sửa. Chương trình cơ bản đúng khung nhưng khi chạy kiểm tra 6 tiêu chí bắt buộc thì phát hiện các điểm sai sót cần can thiệp.

---

## Danh mục 2 lỗi phát hiện và cách sinh viên khắc phục (Theo mục B.3 & Chuẩn đầu ra Lab 6)

### Lỗi 1: Bỏ sót phí gas của các giao dịch gửi đi bị thất bại (Audit #4)
* **Chỗ sai:** Trong phiên bản mã nháp ban đầu, đoạn kiểm tra giao dịch `isError == "1"` bị bỏ qua (skip), dẫn đến việc số dư lũy kế không bị trừ khoản phí gas thực tế mà ví đã trả cho validator khi thực hiện giao dịch lỗi:
  ```python
  # MÃ SAI BAN ĐẦU:
  if isError == "1":
      continue  # Bỏ qua hoàn toàn giao dịch lỗi
  ```
* **Hậu quả:** Làm sai lệch số dư cuối kỳ và tổng dòng tiền ra (Outflow) của ví.
* **Cách sửa (Sinh viên đã làm):** Sửa lại logic tại hàm `analyzeCashFlow`: Nếu là giao dịch đi từ ví (`fromAddr == targetAddress`) mà bị lỗi thì gán `value = 0` nhưng vẫn ghi nhận `outflowAmount = gasFeeEth` và trừ phí gas vào `cumulativeBalance`:
  ```python
  # MÃ ĐÃ SỬA ĐÚNG:
  elif fromAddr == targetAddress:
      if not isFailedTx:
          outflowAmount = valueEth + gasFeeEth
      else:
          outflowAmount = gasFeeEth  # Vẫn tính phí gas của tx lỗi
      cumulativeBalance -= outflowAmount
  ```
* **Ai phát hiện:** **Sinh viên phát hiện** (thông qua đối chiếu với Quy tắc R4 trong `SPEC.md`).

---

### Lỗi 2: Nguy cơ Hardcode khóa API và thiếu kiểm tra HTTP Status Code (Audit #2 & #5)
* **Chỗ sai:** Đoạn mã mẫu ban đầu có xu hướng gán trực tiếp `API_KEY = "YourApiKeyHere"` trong mã nguồn và gọi thẳng `response.json()` mà không kiểm tra mã trạng thái `response.status_code == 200`:
  ```python
  # MÃ SAI BAN ĐẦU:
  API_KEY = "XYZ123ABC..."  # Vi phạm quy tắc bảo mật
  data = requests.get(url).json()  # Sẽ gây crash nếu mất mạng hoặc lỗi 4xx/5xx
  ```
* **Hậu quả:** Vi phạm nghiêm trọng quy tắc bảo mật của `AGENTS.md` (lộ khóa bí mật khi đẩy code lên GitHub) và chương trình bị dừng đột ngột (crash/exception) khi mất kết nối mạng.
* **Cách sửa (Sinh viên đã làm):** Đọc bắt buộc từ biến môi trường `os.getenv("ETHERSCAN_API_KEY")`, bọc trong khối `try-except requests.exceptions.RequestException` và kiểm tra tường minh `if response.status_code != 200`.
* **Ai phát hiện:** **Sinh viên phát hiện** (thông qua đối chiếu với Quy tắc 1 & 2 trong `AGENTS.md`).
