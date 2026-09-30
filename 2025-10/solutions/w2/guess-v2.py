# -*- coding: utf-8 -*-
# D010 参考答案

import random


def even_sum(n):
    result = 0
    for i in range(2, n + 1, 2):   # 从 2 开始、步长 2：只走偶数
        result += i
    return result


def main():
    answer = random.randint(1, 100)
    tries = 0
    print("1-100 随机数已生成，开始猜！")
    while True:
        tries += 1
        guess = int(input("第 %d 猜：" % tries))
        if guess > answer:
            print("大了")
        elif guess < answer:
            print("小了")
        else:
            print("猜对了！共用了 %d 次" % tries)
            break


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        main()
    else:
        def _check(name, got, want):
            if got == want:
                print("PASS", name)
            else:
                print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
        _check("even_sum(10)", even_sum(10), 30)
        _check("even_sum(1)", even_sum(1), 0)
