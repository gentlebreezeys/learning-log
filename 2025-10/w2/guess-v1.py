# -*- coding: utf-8 -*-
# D009 · 10-09 · 猜数字 v1（条件语句）
#
# 【讲义】
# 1. if / elif / else：
#    if score >= 90:      # 冒号 + 缩进 4 格，缩进就是 Python 的花括号
#        print("A")
#    elif score >= 60:
#        print("及格")
#    else:
#        print("不及格")
# 2. 比较运算符：== != > < >= <=（注意 = 是赋值，== 才是比较）
# 3. 逻辑运算：and 或 or 非 not（例：60 <= s and s < 90）
#
# 【运行】
#   python3 guess-v1.py        → 自检
#   python3 guess-v1.py play   → 玩猜数字（答案写死在代码里）

SECRET = 42  # v1 的答案就写死在这，v2 会换成随机的


def check(guess, answer):
    """TODO 1：比较猜的数和答案
    猜大了 → "大了"；猜小了 → "小了"；相等 → "猜对了"
    例如 check(50, 42) → "大了"；check(42, 42) → "猜对了" """
    pass


def grade(score):
    """TODO 2：分数 → 等级
    >=90 → "A"；>=80 → "B"；>=70 → "C"；>=60 → "D"；否则 → "不及格"
    注意 elif 的顺序：从高往低判断"""
    pass


def main():
    print(f"我想好了一个 1-100 的数（偷偷告诉你，藏在代码里），猜猜看")
    while True:
        guess = int(input("你的猜测："))
        result = check(guess, SECRET)
        print(result)
        if result == "猜对了":
            break


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        main()
    else:
        _check("check大了", check(50, 42), "大了")
        _check("check小了", check(10, 42), "小了")
        _check("check对了", check(42, 42), "猜对了")
        _check("grade A", grade(95), "A")
        _check("grade B", grade(85), "B")
        _check("grade D", grade(60), "D")
        _check("grade不及格", grade(50), "不及格")
        print("--- 全部 PASS 后 play 一局，然后提交 D009 ---")
