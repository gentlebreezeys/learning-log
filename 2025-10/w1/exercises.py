# -*- coding: utf-8 -*-
# D005 · 10-05 · 变量与类型
#
# 【讲义】
# 1. 变量 = 给数据贴名字标签：age = 30，之后用 age 就是指 30
# 2. 常见类型：
#    int 整数 3 / float 小数 3.14 / str 文本 "你好" / bool 真 True 假 False
# 3. type(x) 查类型：type(3) → <class 'int'>
# 4. f-string 格式化：
#    f"{price:.1f}"  保留 1 位小数（3.14159 → "3.1"）
#    f"{n:>5}"       右对齐占 5 格
# 5. 命名：小写字母+下划线（user_name），别用拼音缩写和 a/b（循环变量除外）
#
# 【运行】python3 exercises.py

def swap(a, b):
    """TODO 1：交换两个变量的值，返回 (b, a)
    例如 swap(1, 2) → (2, 1)
    提示：Python 可以直接 a, b = b, a"""
    pass


def bmi(weight, height):
    """TODO 2：计算 BMI = 体重kg / 身高m的平方，保留 1 位小数
    例如 bmi(70, 1.75) → 22.9（提示：round(数值, 1)）"""
    pass


def introduce(name, age, city):
    """TODO 3：返回自我介绍 "我叫xx，今年xx岁，住在xx"
    例如 introduce("小明", 30, "北京") → "我叫小明，今年30岁，住在北京" """
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("swap", swap(1, 2), (2, 1))
    _check("bmi", bmi(70, 1.75), 22.9)
    _check("introduce", introduce("小明", 30, "北京"), "我叫小明，今年30岁，住在北京")
    print("--- 全部 PASS 就可以提交 D005 了 ---")
