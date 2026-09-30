# -*- coding: utf-8 -*-
# D014 · 10-14 · 统计器（for 循环）
#
# 【讲义】
# 1. for 遍历列表：for x in [10, 20, 30]:   x 依次是 10、20、30
# 2. 手写累加的标准姿势：
#    total = 0
#    for x in nums:
#        total += x
# 3. 空列表防御：len(nums) == 0 时求平均会除零崩溃 → 先返回 None
# 4. 其实 Python 自带 sum(nums) / max(nums) / min(nums)，
#    但今天先手写（明天学排序时你会感谢今天的肌肉记忆），答案里有对照版
#
# 【运行】python3 stats.py

def total(nums):
    """TODO 1：手写循环求和。total([]) → 0"""
    pass


def average(nums):
    """TODO 2：平均值。空列表返回 None（不许崩溃）
    例如 average([1, 2, 3]) → 2.0"""
    pass


def maximum(nums):
    """TODO 3：手写循环找最大值。空列表返回 None
    提示：假设第一个最大，逐个挑战擂主"""
    pass


def minimum(nums):
    """TODO 4：手写循环找最小值。空列表返回 None"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("total", total([1, 2, 3]), 6)
    _check("total空", total([]), 0)
    _check("average", average([1, 2, 3]), 2.0)
    _check("average空", average([]), None)
    _check("maximum", maximum([3, 9, 2]), 9)
    _check("minimum", minimum([3, 9, 2]), 2)
    _check("maximum空", maximum([]), None)
    print("--- 全部 PASS 就可以提交 D014 了 ---")
