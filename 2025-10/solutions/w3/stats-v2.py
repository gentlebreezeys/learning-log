# -*- coding: utf-8 -*-
# D016 参考答案

def min_max(nums):
    lo = hi = nums[0]              # 一开始既是最小也是最大
    for x in nums:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi                  # 返回元组，括号可省


def stats_all(nums):
    s = 0
    for x in nums:
        s += x
    lo, hi = min_max(nums)         # 解包接收 min_max 的结果
    return s, s / len(nums), hi, lo


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("min_max", min_max([3, 1, 2]), (1, 3))
    _check("stats_all", stats_all([1, 2, 3, 4]), (10, 2.5, 4, 1))
    low, high = min_max([5, 2, 8])
    _check("解包", (low, high), (2, 8))
