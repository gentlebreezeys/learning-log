# -*- coding: utf-8 -*-
# D015 · 10-15 · 成绩排名器（排序）
#
# 【讲义】
# 1. sorted(列表) → 返回排好的新列表，原列表不变
#   列表.sort() → 原地排序，返回 None（新手大坑：x = items.sort() 得到 None）
# 2. 降序：sorted(nums, reverse=True)
# 3. 按什么排（key）：sorted(students, key=lambda s: s["score"])
#   lambda 是一次性小函数，lambda s: s["score"] 意思是"取 s 的 score 当排序依据"
#   （11 月会细讲 lambda，今天照着用就行）
# 4. 字典套在列表里：[{"name": "甲", "score": 90}, ...] 真实数据都长这样
#
# 【运行】python3 rank.py

STUDENTS = [
    {"name": "甲", "score": 90},
    {"name": "乙", "score": 78},
    {"name": "丙", "score": 85},
]


def sort_by_score(students):
    """TODO 1：按 score 从高到低排序，返回新列表（不改动原列表）
    提示：sorted(..., key=lambda s: s["score"], reverse=True)"""
    pass


def rank_students(students):
    """TODO 2：返回 [(名次, 名字, 分数), ...]，名次从 1 开始
    例如 [(1, "甲", 90), (2, "丙", 85), (3, "乙", 78)]
    提示：先排序，再用 n = 0 / for s in 排序结果 / n += 1 数名次"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("排序名字", [s["name"] for s in sort_by_score(STUDENTS)], ["甲", "丙", "乙"])
    _check("排名", rank_students(STUDENTS), [(1, "甲", 90), (2, "丙", 85), (3, "乙", 78)])
    print("--- 全部 PASS 就可以提交 D015 了 ---")
