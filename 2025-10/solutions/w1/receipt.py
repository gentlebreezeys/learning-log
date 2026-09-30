# -*- coding: utf-8 -*-
# D007 参考答案

def total(price, count):
    return price * count


def pay(amount, given):
    return given - amount


def make_receipt():
    price = float(input("单价？"))
    count = int(input("数量？"))
    amount = total(price, count)
    given = float(input("付了多少钱？"))
    print("====== 小票 ======")
    print(f"总价：{amount:.2f} 元")
    print(f"找零：{pay(amount, given):.2f} 元")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        make_receipt()
    else:
        def _check(name, got, want):
            if got == want:
                print("PASS", name)
            else:
                print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
        _check("total", total(3.5, 4), 14.0)
        _check("pay", pay(14, 20), 6)
