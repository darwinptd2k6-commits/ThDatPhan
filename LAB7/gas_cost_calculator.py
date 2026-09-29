#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DỰ ÁN ECO2432 — LAB 7: CÔNG CỤ TÍNH TOÁN & SO SÁNH CHI PHÍ VẬN HÀNH GAS ETHEREUM MAINNET VS LAYER 2
Mô tả: Phân tích chi phí vận hành cho ứng dụng thẻ tích điểm sinh viên.
Tuân thủ: AGENTS.md (camelCase, chú thích tiếng Việt rõ ràng, quy đổi đơn vị chuẩn xác).
"""

import sys

# Đảm bảo hiển thị ký tự tiếng Việt an toàn trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def calculateTransactionFeeEth(gasUsed, gasPriceGwei):
    """
    Tính phí gas cho 1 giao dịch theo đơn vị ETH.
    Công thức: Phí ETH = Gas tiêu thụ * Đơn giá Gwei * 10^(-9)
    """
    return gasUsed * gasPriceGwei * (10 ** -9)


def calculateTransactionFeeUsd(feeEth, ethPriceUsd):
    """
    Tính phí giao dịch quy đổi sang USD.
    """
    return feeEth * ethPriceUsd


def calculateMonthlyOperatingCost(monthlyTransactions, gasPerTx, gasPriceGwei, ethPriceUsd, l2ReductionRatio=100):
    """
    Tính toán chi phí vận hành hàng tháng trên Ethereum Mainnet và Layer 2.
    """
    # 1. Tính toán trên Ethereum Mainnet
    singleTxFeeEthMainnet = calculateTransactionFeeEth(gasPerTx, gasPriceGwei)
    singleTxFeeUsdMainnet = calculateTransactionFeeUsd(singleTxFeeEthMainnet, ethPriceUsd)

    monthlyFeeEthMainnet = singleTxFeeEthMainnet * monthlyTransactions
    monthlyFeeUsdMainnet = singleTxFeeUsdMainnet * monthlyTransactions

    # 2. Tính toán trên Layer 2 (Rẻ hơn l2ReductionRatio lần)
    singleTxFeeEthL2 = singleTxFeeEthMainnet / l2ReductionRatio
    singleTxFeeUsdL2 = singleTxFeeUsdMainnet / l2ReductionRatio

    monthlyFeeEthL2 = monthlyFeeEthMainnet / l2ReductionRatio
    monthlyFeeUsdL2 = monthlyFeeUsdMainnet / l2ReductionRatio

    # 3. Tiết kiệm ngân sách
    savedUsdMonthly = monthlyFeeUsdMainnet - monthlyFeeUsdL2
    savedPercentage = (savedUsdMonthly / monthlyFeeUsdMainnet) * 100

    return {
        "mainnet": {
            "singleTxEth": singleTxFeeEthMainnet,
            "singleTxUsd": singleTxFeeUsdMainnet,
            "monthlyEth": monthlyFeeEthMainnet,
            "monthlyUsd": monthlyFeeUsdMainnet,
        },
        "layer2": {
            "singleTxEth": singleTxFeeEthL2,
            "singleTxUsd": singleTxFeeUsdL2,
            "monthlyEth": monthlyFeeEthL2,
            "monthlyUsd": monthlyFeeUsdL2,
        },
        "savings": {
            "savedUsdMonthly": savedUsdMonthly,
            "savedPercentage": savedPercentage,
        }
    }


def printCostReport(results, monthlyTransactions, gasPerTx, gasPriceGwei, ethPriceUsd):
    """
    In báo cáo phân tích chi phí tài chính dưới dạng bảng chi tiết.
    """
    mainnet = results["mainnet"]
    l2 = results["layer2"]
    savings = results["savings"]

    print("=" * 80)
    print(" BÁO CÁO PHÂN TÍCH CHI PHÍ VẬN HÀNH THẺ TÍCH ĐIỂM SINH VIÊN (LAB 7)")
    print("=" * 80)
    print(f"[*] THAM SỐ ĐẦU VÀO:")
    print(f" - Số lượt cộng điểm hàng tháng: {monthlyTransactions:,} lượt")
    print(f" - Mức tiêu thụ Gas mỗi lượt    : {gasPerTx:,} gas")
    print(f" - Đơn giá Gas (Mainnet)        : {gasPriceGwei} Gwei")
    print(f" - Tỷ giá ETH tham chiếu        : {ethPriceUsd:,.2f} USD")
    print(f" - Hệ số tối ưu Layer 2         : Rẻ hơn Mainnet 100 lần")
    print("-" * 80)
    print(f"{'HẠNG MỤC CHI PHÍ':<35} | {'ETHEREUM MAINNET':<18} | {'LAYER 2 (L2)':<18}")
    print("-" * 80)
    print(f"{'Phí 1 giao dịch (ETH)':<35} | {mainnet['singleTxEth']:>14.6f} ETH | {l2['singleTxEth']:>14.6f} ETH")
    print(f"{'Phí 1 giao dịch (USD)':<35} | {mainnet['singleTxUsd']:>14.4f} USD | {l2['singleTxUsd']:>14.4f} USD")
    print(f"{'Tổng chi phí 1 tháng (ETH)':<35} | {mainnet['monthlyEth']:>14.6f} ETH | {l2['monthlyEth']:>14.6f} ETH")
    print(f"{'Tổng chi phí 1 tháng (USD)':<35} | {mainnet['monthlyUsd']:>14.2f} USD | {l2['monthlyUsd']:>14.2f} USD")
    print("-" * 80)
    print(f"[*] TỔNG KẾT HIỆU QUẢ KINH TẾ:")
    print(f" -> Mức chi phí tiết kiệm mỗi tháng: {savings['savedUsdMonthly']:,.2f} USD ({savings['savedPercentage']:.1f}%)")
    print("=" * 80)


def main():
    # Tham số đầu vào theo đề bài
    monthlyTransactions = 1000
    gasPerTx = 20000
    gasPriceGwei = 20
    ethPriceUsd = 3000.0

    costResults = calculateMonthlyOperatingCost(
        monthlyTransactions=monthlyTransactions,
        gasPerTx=gasPerTx,
        gasPriceGwei=gasPriceGwei,
        ethPriceUsd=ethPriceUsd,
        l2ReductionRatio=100
    )

    printCostReport(costResults, monthlyTransactions, gasPerTx, gasPriceGwei, ethPriceUsd)


if __name__ == "__main__":
    main()
