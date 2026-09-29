#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DỰ ÁN ECO2432 — LAB 6: CÔNG CỤ PHÂN TÍCH DÒNG TIỀN VÍ ON-CHAIN
Mô tả: Kết nối Etherscan API (Mainnet & Sepolia) để lấy dữ liệu giao dịch 90 ngày gần nhất,
       tính toán dòng tiền vào/ra, số dư lũy kế và vẽ biểu đồ biến động số dư.
Tuân thủ: AGENTS.md (Đọc biến môi trường, kiểm tra mã phản hồi, chia 10^18, camelCase).
"""

import os
import sys
import time
from datetime import datetime, timezone, timedelta
import requests

# Đảm bảo terminal Windows hiển thị đúng ký tự tiếng Việt Unicode (tránh UnicodeEncodeError)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# Bọc kiểm tra thư viện vẽ đồ thị matplotlib an toàn
try:
    import matplotlib
    matplotlib.use("Agg")  # Chế độ headless an toàn, không phụ thuộc GUI
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    plt = None
    MATPLOTLIB_AVAILABLE = False


def convertWeiToEth(weiValue):
    """
    Chuyển đổi số nguyên đơn vị Wei sang số thực đơn vị ETH (chia cho 10^18).
    """
    try:
        return float(weiValue) / (10 ** 18)
    except (ValueError, TypeError):
        return 0.0


def validateWalletAddress(walletAddress):
    """
    Kiểm tra tính hợp lệ cơ bản của địa chỉ ví Ethereum (42 ký tự, bắt đầu bằng 0x).
    """
    if not walletAddress or not isinstance(walletAddress, str):
        return False
    trimmedAddress = walletAddress.strip()
    if len(trimmedAddress) != 42 or not trimmedAddress.startswith("0x"):
        return False
    return True


def getApiBaseUrl(network="sepolia"):
    """
    Trả về endpoint Etherscan API tương ứng với mạng đã chọn.
    """
    if network.lower() == "sepolia":
        return "https://api-sepolia.etherscan.io/api"
    return "https://api.etherscan.io/api"


def fetchTransactions(walletAddress, apiKey, network="sepolia", days=90):
    """
    Truy vấn toàn bộ giao dịch thông thường (normal transactions) của ví trong khoảng ngày quy định.
    Hỗ trợ cơ chế phân trang tự động nếu số lượng giao dịch vượt quá 10.000.
    """
    baseUrl = getApiBaseUrl(network)
    
    # Tính mốc thời gian bắt đầu (timezone UTC chuẩn Python 3.12+)
    startTimeStamp = int((datetime.now(timezone.utc) - timedelta(days=days)).timestamp())
    
    allTransactions = []
    page = 1
    offset = 10000  # Giới hạn tối đa một lần lấy của Etherscan API

    print(f"[*] Đang tải dữ liệu giao dịch cho ví: {walletAddress}")
    print(f"[*] Mạng lưới: {network.upper()} | Khoảng thời gian: {days} ngày gần nhất...")

    while True:
        params = {
            "module": "account",
            "action": "txlist",
            "address": walletAddress,
            "startblock": 0,
            "endblock": 99999999,
            "page": page,
            "offset": offset,
            "sort": "asc",
            "apikey": apiKey
        }

        try:
            response = requests.get(baseUrl, params=params, timeout=20)
        except requests.exceptions.RequestException as error:
            print(f"[!] Lỗi kết nối mạng: {error}")
            sys.exit(1)

        # 1. Kiểm tra mã trạng thái phản hồi HTTP
        if response.status_code != 200:
            print(f"[!] Lỗi HTTP từ máy chủ Etherscan (Mã trạng thái: {response.status_code})")
            sys.exit(1)

        try:
            data = response.json()
        except Exception as jsonErr:
            print(f"[!] Lỗi đọc định dạng JSON: {jsonErr}")
            sys.exit(1)

        status = data.get("status")
        message = data.get("message", "")
        result = data.get("result", [])

        # 2. Xử lý phản hồi từ Etherscan API
        if status != "1":
            if message == "No transactions found" or result == "No transactions found":
                print("[*] Thông báo: Không tìm thấy giao dịch nào trong lịch sử ví.")
                return []
            else:
                print(f"[!] Phản hồi từ Etherscan API: {result} (Thông báo: {message})")
                # Nếu sai API key hoặc vượt rate limit, báo lỗi và dừng an toàn
                if "NOTOK" in status or "Invalid" in str(result):
                    sys.exit(1)
                return []

        if not isinstance(result, list) or not result:
            break

        allTransactions.extend(result)

        # Nếu số lượng lấy về ít hơn offset nghĩa là đã hết trang
        if len(result) < offset:
            break

        page += 1
        time.sleep(0.25)  # Nghỉ nhẹ để tuân thủ giới hạn tốc độ API (rate limit)

    # Lọc các giao dịch phát sinh trong vòng 90 ngày gần nhất
    recentTransactions = [
        tx for tx in allTransactions
        if int(tx.get("timeStamp", 0)) >= startTimeStamp
    ]

    print(f"[✓] Đã thu thập thành công {len(recentTransactions)} giao dịch trong {days} ngày gần nhất.")
    return recentTransactions


def analyzeCashFlow(walletAddress, transactionList):
    """
    Phân tích dòng tiền vào/ra, tính phí gas và số dư lũy kế theo thời gian.
    Áp dụng toàn bộ quy tắc nghiệp vụ R1 - R7 trong SPEC.md.
    """
    targetAddress = walletAddress.lower().strip()
    
    # R6: Đảm bảo giao dịch sắp xếp tăng dần theo mốc thời gian
    sortedTransactions = sorted(transactionList, key=lambda tx: int(tx.get("timeStamp", 0)))

    analyzedRecords = []
    cumulativeBalance = 0.0
    totalInflow = 0.0
    totalOutflow = 0.0

    for tx in sortedTransactions:
        txHash = tx.get("hash", "")
        timeStamp = int(tx.get("timeStamp", 0))
        txTime = datetime.fromtimestamp(timeStamp, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        
        fromAddr = tx.get("from", "").lower().strip()
        toAddr = tx.get("to", "").lower().strip() if tx.get("to") else ""
        
        isError = tx.get("isError", "0") == "1"
        txReceiptStatus = tx.get("txreceipt_status", "1") == "0"
        isFailedTx = isError or txReceiptStatus

        # R5: Quy đổi Wei sang ETH
        valueEth = convertWeiToEth(tx.get("value", 0))
        gasUsed = float(tx.get("gasUsed", 0))
        gasPrice = float(tx.get("gasPrice", 0))
        gasFeeEth = (gasUsed * gasPrice) / (10 ** 18)

        # R7: Tự chuyển cho chính mình
        if fromAddr == targetAddress and toAddr == targetAddress:
            txType = "TỰ CHUYỂN"
            inflowAmount = 0.0
            outflowAmount = gasFeeEth
            cumulativeBalance -= gasFeeEth
            totalOutflow += gasFeeEth

        # R1: Dòng tiền vào
        elif toAddr == targetAddress:
            if not isFailedTx:
                txType = "VÀO"
                inflowAmount = valueEth
                outflowAmount = 0.0
                cumulativeBalance += valueEth
                totalInflow += valueEth
            else:
                txType = "VÀO (LỖI)"
                inflowAmount = 0.0
                outflowAmount = 0.0

        # R2, R3, R4: Dòng tiền ra (bao gồm cả contract creation khi toAddr rỗng)
        elif fromAddr == targetAddress:
            if not isFailedTx:
                txType = "RA"
                inflowAmount = 0.0
                outflowAmount = valueEth + gasFeeEth
                cumulativeBalance -= (valueEth + gasFeeEth)
                totalOutflow += (valueEth + gasFeeEth)
            else:
                # R4: Giao dịch gửi đi thất bại vẫn bị trừ phí gas
                txType = "RA (LỖI)"
                inflowAmount = 0.0
                outflowAmount = gasFeeEth
                cumulativeBalance -= gasFeeEth
                totalOutflow += gasFeeEth

        else:
            continue

        analyzedRecords.append({
            "time": txTime,
            "timeStamp": timeStamp,
            "hash": txHash,
            "type": txType,
            "value": valueEth,
            "fee": gasFeeEth,
            "inflow": inflowAmount,
            "outflow": outflowAmount,
            "balance": cumulativeBalance
        })

    summary = {
        "totalInflow": totalInflow,
        "totalOutflow": totalOutflow,
        "netChange": totalInflow - totalOutflow,
        "transactionCount": len(analyzedRecords)
    }

    return analyzedRecords, summary


def displayReport(analyzedRecords, summary):
    """
    Hiển thị bảng dữ liệu dòng tiền chi tiết và 3 chỉ số tài chính tổng hợp ra màn hình console.
    """
    print("\n" + "=" * 94)
    print("                      BẢNG PHÂN TÍCH DÒNG TIỀN VÍ CHI TIẾT (90 NGÀY)")
    print("=" * 94)
    print(f"{'Thời gian (UTC)':<20} | {'Tx Hash':<14} | {'Loại':<12} | {'Giá trị (ETH)':<14} | {'Phí Gas (ETH)':<14} | {'Lũy kế (ETH)':<14}")
    print("-" * 94)

    for item in analyzedRecords:
        shortHash = item['hash'][:6] + "..." + item['hash'][-4:] if len(item['hash']) > 10 else item['hash']
        print(f"{item['time']:<20} | {shortHash:<14} | {item['type']:<12} | {item['value']:<14.6f} | {item['fee']:<14.6f} | {item['balance']:<14.6f}")

    print("=" * 94)
    print("                           BÁO CÁO CHỈ SỐ TÀI CHÍNH TỔNG HỢP")
    print("=" * 94)
    print(f" 1. Tổng dòng tiền vào (Total Inflow):         +{summary['totalInflow']:.6f} ETH")
    print(f" 2. Tổng dòng tiền ra (Total Outflow):        -{summary['totalOutflow']:.6f} ETH")
    print(f" 3. Biến động số dư ròng trong kỳ:            {summary['netChange']:+.6f} ETH")
    print(f" 4. Tổng số giao dịch phân tích:              {summary['transactionCount']} giao dịch")
    print("=" * 94 + "\n")


def plotBalanceChart(analyzedRecords, walletAddress, outputPath="LAB6/balance_chart.png"):
    """
    Vẽ biểu đồ đường biểu diễn biến động số dư ví lũy kế theo thời gian và lưu thành tệp hình ảnh.
    """
    if not MATPLOTLIB_AVAILABLE or plt is None:
        print("[!] Thư viện matplotlib chưa sẵn sàng. Bỏ qua xuất biểu đồ hình ảnh.")
        return

    if not analyzedRecords:
        print("[!] Không có dữ liệu để vẽ biểu đồ.")
        return

    try:
        timeLabels = [datetime.fromtimestamp(item["timeStamp"], tz=timezone.utc) for item in analyzedRecords]
        balances = [item["balance"] for item in analyzedRecords]

        plt.figure(figsize=(11, 5.5), dpi=120)
        plt.plot(timeLabels, balances, marker="o", linestyle="-", color="#1E88E5", linewidth=2, markersize=4, label="Số dư lũy kế (ETH)")
        plt.axhline(0, color="gray", linestyle="--", alpha=0.6)

        shortAddress = walletAddress[:6] + "..." + walletAddress[-4:] if len(walletAddress) > 10 else walletAddress
        plt.title(f"Biểu Đồ Biến Động Số Dư Ví {shortAddress} (90 Ngày Gần Nhất)", fontsize=13, fontweight="bold", pad=12)
        plt.xlabel("Thời gian (UTC)", fontsize=10)
        plt.ylabel("Số dư ví (ETH)", fontsize=10)
        plt.grid(True, linestyle=":", alpha=0.6)
        plt.legend(loc="upper left")
        plt.gcf().autofmt_xdate()
        plt.tight_layout()

        # Tạo thư mục cha nếu chưa có
        os.makedirs(os.path.dirname(outputPath), exist_ok=True)
        plt.savefig(outputPath)
        plt.close()
        print(f"[✓] Đã xuất biểu đồ trực quan thành công tại: {outputPath}")
    except Exception as chartErr:
        print(f"[!] Không thể xuất tệp biểu đồ: {chartErr}")


def main():
    """
    Hàm thực thi chính của chương trình.
    """
    print("=" * 75)
    print(" CHƯƠNG TRÌNH PHÂN TÍCH DÒNG TIỀN VÍ ETHEREUM — ECO2432 (LAB 6)")
    print("=" * 75)

    # 1. Đọc khóa API từ biến môi trường (Quy tắc bắt buộc theo AGENTS.md)
    apiKey = os.getenv("ETHERSCAN_API_KEY", "").strip()
    if not apiKey:
        print("[*] Biến môi trường ETHERSCAN_API_KEY chưa được đặt.")
        apiKey = input("-> Nhập khóa Etherscan API của bạn (hoặc nhấn Enter để dùng mặc định): ").strip()
        if not apiKey:
            apiKey = "YourApiKeyToken"  # Dự phòng giá trị mặc định nếu người dùng chưa có key riêng

    # 2. Chọn mạng lưới phân tích (Sepolia hoặc Mainnet)
    print("\nChọn mạng lưới:")
    print(" 1. Sepolia Testnet (Mặc định cho các Lab 1, 2, 3)")
    print(" 2. Ethereum Mainnet")
    networkChoice = input("-> Nhập lựa chọn [1 hoặc 2, mặc định 1]: ").strip()
    selectedNetwork = "mainnet" if networkChoice == "2" else "sepolia"

    # 3. Nhập địa chỉ ví cần phân tích
    defaultAddress = "0xe65449A5a0f67e390ca250326c3f3F166463A899"
    inputAddress = input(f"\n-> Nhập địa chỉ ví Ethereum cần phân tích [Mặc định ví Lab 2: {defaultAddress}]: ").strip()
    targetWallet = inputAddress if inputAddress else defaultAddress

    # 4. Kiểm tra định dạng địa chỉ
    if not validateWalletAddress(targetWallet):
        print(f"[!] Địa chỉ ví không hợp lệ: '{targetWallet}'. Yêu cầu chuỗi 42 ký tự bắt đầu bằng '0x'.")
        sys.exit(1)

    # 5. Lấy dữ liệu và phân tích
    transactions = fetchTransactions(targetWallet, apiKey, network=selectedNetwork, days=90)
    
    if not transactions:
        print("[*] Kết luận: Ví không phát sinh giao dịch trong kỳ phân tích 90 ngày.")
        sys.exit(0)

    records, summary = analyzeCashFlow(targetWallet, transactions)

    # 6. Hiển thị báo cáo và xuất biểu đồ
    displayReport(records, summary)
    plotBalanceChart(records, targetWallet, outputPath="LAB6/balance_chart.png")


if __name__ == "__main__":
    main()
