# -*- coding: utf-8 -*-
# D011 · 10-11 · 基本功日（for + range + 取余）
#
# 【讲义】
# 1. for i in range(1, 10)：i 依次取 1..9（右边取不到！range(5) 是 0..4）
# 2. 嵌套循环：外层走一步、内层走一整圈（乘法表就是这么打印的）
# 3. n % 2 == 0 → 偶数；n % 3 == 0 → 是 3 的倍数（FizzBuzz 的核心）
# 4. 往列表收集结果：result = []，循环里 result.append(x)
#
# 【运行】
#   python3 drills.py        → 自检
#   python3 drills.py play   → 打印完整 99 乘法表


def fizzbuzz(n):
    """TODO 1：返回 1..n 每个数的对应字符串组成的列表
    规则：3 的倍数 → "Fizz"；5 的倍数 → "Buzz"；
         既是 3 又是 5 的倍数 → "FizzBuzz"（先判断这个！）；其他 → 数字本身
    例如 fizzbuzz(5) → ["1", "2", "Fizz", "4", "Buzz"]
    提示：其他情况返回 str(数字)"""
    pass


def table_lines():
    """TODO 2：返回 99 乘法表（下三角）的 9 行字符串
    第 i 行格式：把 i x 1=积、i x 2=积 ... i x i=积 用空格连起来
    例如第 3 行是 "3x1=3 3x2=6 3x3=9"（用 ASCII 字母 x，别用乘号）
    提示：外层 for i in range(1, 10)，内层 for j in range(1, i + 1)"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        for line in table_lines():
            print(line)
    else:
        _check("fizzbuzz(5)", fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        _check("fizzbuzz(15) 末项", fizzbuzz(15)[-1], "FizzBuzz")
        _check("乘法表行数", len(table_lines()), 9)
        _check("乘法表第3行", table_lines()[2], "3x1=3 3x2=6 3x3=9")
        print("--- 全部 PASS 就可以提交 D011 了 ---")
