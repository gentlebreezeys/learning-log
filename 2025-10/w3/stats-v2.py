# -*- coding: utf-8 -*-
# D016 · 10-16 · 元组与解包
#
# 【讲义】
# 1. 元组 tuple：(1, 2) —— 像列表但创建后不能改（不可变）
#    点坐标、RGB 颜色、"返回多个值"都爱用它
# 2. 多重赋值（解包）：a, b = 1, 2；a, b = b, a（一行交换！）
#    low, high = min_max([3, 1, 2])  ← 左边几个名字，右边就得有几个值
# 3. 函数返回多值：return (a, b) 括号可省略 → return a, b
# 4. 元组也支持 in / len / 切片 / for 遍历，就是不能 append
#
# 【运行】python3 stats-v2.py

def min_max(nums):
    """TODO 1：一次返回 (最小值, 最大值) 的元组（基于 D014 的思路）
    例如 min_max([3, 1, 2]) → (1, 3)"""
    pass


def stats_all(nums):
    """TODO 2：返回 (总和, 平均, 最大, 最小) 四个值
    例如 stats_all([1, 2, 3, 4]) → (10, 2.5, 4, 1)
    提示：可以直接调用你写的 min_max，再算 sum 和 avg"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("min_max", min_max([3, 1, 2]), (1, 3))
    _check("stats_all", stats_all([1, 2, 3, 4]), (10, 2.5, 4, 1))
    low, high = min_max([5, 2, 8])   # 解包的用法演示
    _check("解包", (low, high), (2, 8))
    print("--- 全部 PASS 就可以提交 D016 了 ---")
