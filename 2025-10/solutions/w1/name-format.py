# -*- coding: utf-8 -*-
# D008 参考答案

def normalize(name):
    words = name.split()          # 无参数 split：任意空白切开，连续空格也不怕
    return " ".join(words).title()


def initials(name):
    result = ""
    for word in name.split():
        result += word[0].upper()
    return result


def first_last3(s):
    return (s[:3], s[-3:])        # s[-3:] 从倒数第 3 个取到末尾


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("normalize", normalize("  xiao   ming "), "Xiao Ming")
    _check("initials", initials("xiao ming"), "XM")
    _check("first_last3", first_last3("hello"), ("hel", "llo"))
