# -*- coding: utf-8 -*-
# D005 参考答案

def swap(a, b):
    a, b = b, a          # Python 特有的一行交换（其他语言要三行）
    return a, b


def bmi(weight, height):
    return round(weight / height ** 2, 1)   # ** 是幂，height ** 2 = 身高的平方


def introduce(name, age, city):
    return f"我叫{name}，今年{age}岁，住在{city}"


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("swap", swap(1, 2), (2, 1))
    _check("bmi", bmi(70, 1.75), 22.9)
    _check("introduce", introduce("小明", 30, "北京"), "我叫小明，今年30岁，住在北京")
