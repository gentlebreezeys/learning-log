# -*- coding: utf-8 -*-
# D014 参考答案

def total(nums):
    result = 0
    for x in nums:
        result += x
    return result                  # 对照：其实一行 return sum(nums) 就行


def average(nums):
    if len(nums) == 0:             # 空列表防御：len(nums) == 0 提前返回
        return None
    return total(nums) / len(nums)


def maximum(nums):
    if len(nums) == 0:
        return None
    best = nums[0]                 # 擂主是第一个，后来者逐个挑战
    for x in nums:
        if x > best:
            best = x
    return best                    # 对照：max(nums)


def minimum(nums):
    if len(nums) == 0:
        return None
    best = nums[0]
    for x in nums:
        if x < best:
            best = x
    return best                    # 对照：min(nums)


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("total", total([1, 2, 3]), 6)
    _check("total空", total([]), 0)
    _check("average", average([1, 2, 3]), 2.0)
    _check("average空", average([]), None)
    _check("maximum", maximum([3, 9, 2]), 9)
    _check("minimum", minimum([3, 9, 2]), 2)
    _check("maximum空", maximum([]), None)
