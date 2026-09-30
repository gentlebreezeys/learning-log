# -*- coding: utf-8 -*-
# D027 · 10-27 · 文件读写（配合同目录的 sample.txt）
#
# 【讲义】
# 1. 读文件的标准姿势（with 会自动关文件，忘不了）：
#    with open("sample.txt", "r", encoding="utf-8") as f:
#        content = f.read()          # 整个文件读成一个字符串
# 2. 别的读法：f.readlines() → 每行一个元素的列表（行尾带 \n）
#            逐行 for line in f:   （大文件友好）
# 3. 写文件："w" 模式覆盖重写（危险！），"a" 模式追加到末尾
#    with open("out.txt", "w", encoding="utf-8") as f:
#        f.write("你好\n")
# 4. 中文乱码九成是忘了 encoding="utf-8"
# 5. 找当前目录的文件：os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.txt")
#    意思是"和本文件同目录"，从哪里运行都能找到（本文件已帮你写好 SAMPLE）
#
# 【运行】python3 file-stats.py

import os

SAMPLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.txt")


def count_lines(path):
    """TODO 1：返回文件行数（提示：readlines() 后取 len）"""
    pass


def count_chars(path):
    """TODO 2：返回文件总字符数（提示：read() 后取 len，\n 也算字符）"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("count_lines", count_lines(SAMPLE), 4)
    _check("count_chars", count_chars(SAMPLE), 28)
    print("--- 全部 PASS 就可以提交 D027 了 ---")
