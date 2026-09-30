# -*- coding: utf-8 -*-
# D007 · 10-07 · 输入与运算
#
# 【讲义】
# 1. input() 返回的永远是字符串！"3" 不等于 3
#    要做数学必须先转换：price = float(input("单价？"))
# 2. 算术运算符：+ - * /
#    7 / 2 → 3.5（真除法，永远得 float）
#    7 // 2 → 3（地板除，扔掉小数）
#    7 % 2 → 1（取余数，判断奇偶全靠它：n % 2 == 0 就是偶数）
# 3. 数字格式化：f"{x:.2f}" 保留两位小数（金额常用）
#
# 【运行】
#   python3 receipt.py        → 自检
#   python3 receipt.py play   → 模拟买奶茶

def total(price, count):
    """TODO 1：总价 = 单价 x 数量
    例如 total(3.5, 4) → 14.0"""
    pass


def pay(amount, given):
    """TODO 2：找零 = 给的钱 - 应付金额
    例如 pay(14, 20) → 6"""
    pass


def make_receipt():
    """TODO 3（play 模式用）：依次问单价、数量、付了多少钱，
    打印一张小票：总价（两位小数）和找零"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        make_receipt()
    else:
        _check("total", total(3.5, 4), 14.0)
        _check("pay", pay(14, 20), 6)
        print("--- 全部 PASS 就可以提交 D007 了 ---")
