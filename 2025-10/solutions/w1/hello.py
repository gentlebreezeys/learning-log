# -*- coding: utf-8 -*-
# D002 参考答案（先自己写，卡住 20 分钟再看）

def say_hello():
    return "Hello, World!"


def greet(name):
    return f"你好，{name}！"


def ask_and_greet():
    name = input("你叫什么名字？")
    print(f"你好，{name}！365 天之旅正式开始！")


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("say_hello", say_hello(), "Hello, World!")
    _check("greet", greet("小明"), "你好，小明！")
