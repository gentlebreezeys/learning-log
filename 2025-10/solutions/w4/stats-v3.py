# -*- coding: utf-8 -*-
# D020 参考答案

def average(nums, precision=2):
    if len(nums) == 0:
        return None
    return round(sum(nums) / len(nums), precision)


def describe(nums):
    return f"共 {len(nums)} 个数，平均 {average(nums):.2f}"   # 复用 average，别抄一遍


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("average 1位", average([1, 2, 3], 1), 2.0)
    _check("average 默认", average([1, 2]), 1.5)
    _check("average 空", average([]), None)
    _check("describe", describe([1, 2]), "共 2 个数，平均 1.50")
