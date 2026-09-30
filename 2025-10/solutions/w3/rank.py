# -*- coding: utf-8 -*-
# D015 参考答案

STUDENTS = [
    {"name": "甲", "score": 90},
    {"name": "乙", "score": 78},
    {"name": "丙", "score": 85},
]


def sort_by_score(students):
    return sorted(students, key=lambda s: s["score"], reverse=True)


def rank_students(students):
    ordered = sort_by_score(students)
    result = []
    n = 0
    for s in ordered:
        n += 1
        result.append((n, s["name"], s["score"]))
    return result


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("排序名字", [s["name"] for s in sort_by_score(STUDENTS)], ["甲", "丙", "乙"])
    _check("排名", rank_students(STUDENTS), [(1, "甲", 90), (2, "丙", 85), (3, "乙", 78)])
