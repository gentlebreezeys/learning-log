# -*- coding: utf-8 -*-
# D018 参考答案

STUDENTS = [
    {"name": "甲", "scores": {"语文": 90, "数学": 80}},
    {"name": "乙", "scores": {"语文": 70, "数学": 90}},
]


def subject_average(students, subject):
    total = 0
    for s in students:
        total += s["scores"].get(subject, 0)
    return total / len(students)


def all_averages(students):
    totals = {}                    # 每科总分
    counts = {}                    # 每科人数
    for s in students:
        for subject, score in s["scores"].items():
            totals[subject] = totals.get(subject, 0) + score
            counts[subject] = counts.get(subject, 0) + 1
    result = {}
    for subject in totals:
        result[subject] = totals[subject] / counts[subject]
    return result


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("语文平均", subject_average(STUDENTS, "语文"), 80.0)
    _check("数学平均", subject_average(STUDENTS, "数学"), 85.0)
    _check("全科平均", all_averages(STUDENTS), {"语文": 80.0, "数学": 85.0})
