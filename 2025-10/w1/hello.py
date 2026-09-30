# -*- coding: utf-8 -*-
# D002 · 10-02 · Hello World（print / input / f-string）
#
# 【讲义】
# 1. print(...) 把内容打印到屏幕
# 2. input("提示语") 等用户输入一行，返回一个字符串（str）
# 3. f-string：f"你好，{name}" —— 花括号里可以放变量
# 4. 注释：# 后面的内容 Python 不执行，是写给人看的
#
# 【怎么用 VS Code】
# 用 VS Code 打开本文件夹 → 点开本文件 → 终端里 cd 到本目录 → python3 hello.py
#
# 【运行模式】
#   python3 hello.py        → 自检（看 PASS/FAIL）
#   python3 hello.py play   → 交互模式（体验 input）


# ========== 练习区（完成每个 TODO） ==========

def say_hello():
    """TODO 1：返回字符串 "Hello, World!"（注意是 return，不是 print）"""
    pass  # TODO: 删掉这行，写你的代码


def greet(name):
    """TODO 2：返回 "你好，{name}！"
    例如 greet("小明") → "你好，小明！"（提示：f-string）"""
    pass


def ask_and_greet():
    """TODO 3（play 模式用）：问用户名字，然后打印一句问候
    提示：name = input("你叫什么名字？")，然后 print(f"...")"""
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
        ask_and_greet()
    else:
        _check("say_hello", say_hello(), "Hello, World!")
        _check("greet", greet("小明"), "你好，小明！")
        print("--- 全部 PASS 就可以提交 D002 了 ---")
