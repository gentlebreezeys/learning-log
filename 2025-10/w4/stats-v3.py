# -*- coding: utf-8 -*-
# D020 · 10-20 · 函数（def / 参数 / 返回值 / docstring）
#
# 【讲义】
# 1. 函数 = 把一段逻辑打包起名字，随时复用：def add(a, b): return a + b
# 2. 参数可以有默认值：def average(nums, precision=2):
#    调用时 average([1,2]) 用默认 2 位；average([1,2], 1) 指定 1 位
# 3. 没写 return 的函数返回 None（这就是 TODO 没做时自检 FAIL 的原因）
# 4. 三引号 docstring：函数说明书，写在 def 下面第一行
# 5. 一个函数只做一件事，名字说清楚它做什么（动词开头）
#
# 【运行】python3 stats-v3.py

def average(nums, precision=2):
    """TODO 1：返回平均值，保留 precision 位小数；空列表返回 None
    例如 average([1, 2, 3], 1) → 2.0；average([1, 2]) → 1.5
    提示：round(总和 / 个数, precision)"""
    pass


def describe(nums):
    """TODO 2：返回一句话 "共 n 个数，平均 x.xx"
    例如 describe([1, 2]) → "共 2 个数，平均 1.50"
    提示：f"共 {len(nums)} 个数，平均 {average(nums):.2f}"（复用 TODO 1！）"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("average 1位", average([1, 2, 3], 1), 2.0)
    _check("average 默认", average([1, 2]), 1.5)
    _check("average 空", average([]), None)
    _check("describe", describe([1, 2]), "共 2 个数，平均 1.50")
    print("--- 全部 PASS 就可以提交 D020 了 ---")
