# -*- coding: utf-8 -*-
# D023 · 10-23（上）· 作用域 5 题：先猜后验
#
# 【讲义】
# 1. 函数内部创建的变量是"局部变量"，函数一结束就消失，外面看不见
# 2. 函数外面的变量是"全局变量"，函数里可以"读"它
# 3. 但函数里一旦给同名变量赋值，Python 就认为你在创建新的局部变量，
#    全局那个根本不会被改动——这就是 90% 作用域困惑的来源
# 4. 所以规则很简单：函数要数据，从参数拿；函数出数据，用 return。
#    （global 关键字存在，但今天先当它不存在）
#
# 【玩法】每题先在 EXPECT 里填你的预测（None 的地方），
# 运行 python3 scope-quiz.py 对答案。5 题全对说明你真的懂了。

EXPECT = {
    "q1": None,  # TODO: 例如 (2, 1)
    "q2": None,
    "q3": None,
    "q4": None,
    "q5": None,
}

x = 1

def f1():
    x = 2          # f1 自己的 x，跟外面的 x 没关系
    return x

def q1():
    return (f1(), x)   # f1() 返回什么？外面的 x 现在是几？


name = "全局变量"

def f2():
    return name    # 只读不赋值，能看到全局

def q2():
    return f2()


def f3(n):
    n = n * 2      # 参数也是局部变量
    return n

def q3():
    m = 5
    return f3(m)


def f4a():
    v = 1
    return v

def f4b():
    v = 99          # 另一个函数的同名变量，互不相干
    return v

def q4():
    return (f4a(), f4b())


count = 0

def bump():
    return count + 1   # 读了全局并 +1，但全局本身变了吗？

def q5():
    return (bump(), count)


# ========== 对答案（不要改） ==========

if __name__ == "__main__":
    for qname in ["q1", "q2", "q3", "q4", "q5"]:
        actual = globals()[qname]()
        guess = EXPECT[qname]
        if guess is None:
            print("还没填预测 |", qname, "实际是:", repr(actual))
        elif guess == actual:
            print("PASS", qname, "猜对了:", repr(actual))
        else:
            print("FAIL", qname, "| 你猜:", repr(guess), "| 实际:", repr(actual))
