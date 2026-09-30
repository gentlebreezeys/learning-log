# -*- coding: utf-8 -*-
# D008 · 10-08 · 字符串方法
#
# 【讲义】常用字符串方法（都不改变原字符串，而是返回新的）：
#   "  hi  ".strip()        → "hi"        去掉首尾空白
#   "a b".split(" ")        → ["a", "b"]  按分隔符切开 → 列表
#   "a".split() 无参数版：按任意空白切，连续空格也不怕
#   "-".join(["a", "b"])    → "a-b"       用 - 把列表连起来
#   "xiao ming".title()     → "Xiao Ming" 每个单词首字母大写
#   "HI".lower() / "hi".upper()
# 切片：s[0:3] 取前 3 个字符；s[-3:] 取最后 3 个（负数从后往前数）
#
# 【运行】python3 name-format.py

def normalize(name):
    """TODO 1：清洗名字 → 每段首字母大写、多余空格压缩成一个
    例如 normalize("  xiao   ming ") → "Xiao Ming"
    提示：先 split() 无参数切，再 title()，再 " ".join(...)"""
    pass


def initials(name):
    """TODO 2：返回每个单词首字母的大写组合
    例如 initials("xiao ming") → "XM"
    提示：for word in name.split(): 取 word[0]"""
    pass


def first_last3(s):
    """TODO 3：返回前 3 个和后 3 个字符组成的元组
    例如 first_last3("hello") → ("hel", "llo")（用切片）"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("normalize", normalize("  xiao   ming "), "Xiao Ming")
    _check("initials", initials("xiao ming"), "XM")
    _check("first_last3", first_last3("hello"), ("hel", "llo"))
    print("--- 全部 PASS 就可以提交 D008 了 ---")
