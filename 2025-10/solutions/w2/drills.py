# -*- coding: utf-8 -*-
# D011 参考答案

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:            # 必须先判断 15，不然 3 的分支会截胡
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def table_lines():
    lines = []
    for i in range(1, 10):
        parts = []
        for j in range(1, i + 1):  # 内层只走到 i：下三角
            parts.append(f"{i}x{j}={i * j}")
        lines.append(" ".join(parts))
    return lines


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        for line in table_lines():
            print(line)
    else:
        def _check(name, got, want):
            if got == want:
                print("PASS", name)
            else:
                print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
        _check("fizzbuzz(5)", fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        _check("fizzbuzz(15) 末项", fizzbuzz(15)[-1], "FizzBuzz")
        _check("乘法表行数", len(table_lines()), 9)
        _check("乘法表第3行", table_lines()[2], "3x1=3 3x2=6 3x3=9")
