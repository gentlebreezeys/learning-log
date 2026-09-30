# -*- coding: utf-8 -*-
# D023（下）参考答案

STUDENTS = [
    {"name": "甲", "score": 90},
    {"name": "乙", "score": 78},
    {"name": "丙", "score": 85},
]


def ranked(students):
    ordered = sorted(students, key=lambda s: s["score"], reverse=True)
    result = []
    for rank, s in enumerate(ordered, start=1):   # enumerate 直接发名次
        result.append((rank, s["name"], s["score"]))
    return result


# zip 长这样（见识一下）：
# for name, score in zip(["甲", "乙"], [90, 78]):  →  ("甲", 90), ("乙", 78)

if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("ranked", ranked(STUDENTS), [(1, "甲", 90), (2, "丙", 85), (3, "乙", 78)])
