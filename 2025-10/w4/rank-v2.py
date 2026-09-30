# -*- coding: utf-8 -*-
# D023 · 10-23（下）· rank-v2（enumerate + zip）
#
# 【讲义】
# 1. enumerate：for i, item in enumerate(列表, start=1):
#    一边拿下标一边拿元素，start=1 表示从 1 开始数
#    （自己维护 n += 1 也行，但 enumerate 更地道）
# 2. zip：for a, b in zip([1,2], ["x","y"]): → (1,"x"), (2,"y")
#    两个列表像拉链一样并排走（今天见识一下，答案里有示例）
#
# 【运行】python3 rank-v2.py

STUDENTS = [
    {"name": "甲", "score": 90},
    {"name": "乙", "score": 78},
    {"name": "丙", "score": 85},
]


def ranked(students):
    """TODO 1：按分数降序，返回 [(名次, 名字, 分数), ...]
    与 D015 结果相同，但这次必须用 enumerate 实现
    提示：先 sorted 拿到排序结果，再 for rank, s in enumerate(排序结果, start=1)"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("ranked", ranked(STUDENTS), [(1, "甲", 90), (2, "丙", 85), (3, "乙", 78)])
    print("--- 全部 PASS 就可以提交 D023 了 ---")
