# -*- coding: utf-8 -*-
# D009 参考答案

SECRET = 42


def check(guess, answer):
    if guess > answer:
        return "大了"
    elif guess < answer:
        return "小了"
    else:
        return "猜对了"


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "不及格"


def main():
    print("我想好了一个 1-100 的数（偷偷告诉你，藏在代码里），猜猜看")
    while True:
        guess = int(input("你的猜测："))
        result = check(guess, SECRET)
        print(result)
        if result == "猜对了":
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
        _check("check大了", check(50, 42), "大了")
        _check("check小了", check(10, 42), "小了")
        _check("check对了", check(42, 42), "猜对了")
        _check("grade A", grade(95), "A")
        _check("grade B", grade(85), "B")
        _check("grade D", grade(60), "D")
        _check("grade不及格", grade(50), "不及格")
