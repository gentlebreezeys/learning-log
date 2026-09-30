# -*- coding: utf-8 -*-
# D018 · 10-18 · 成绩单（列表套字典）
#
# 【讲义】
# 1. 真实数据结构：列表装着一堆字典
#    students = [{"name": "甲", "scores": {"语文": 90, "数学": 80}}, ...]
# 2. 取值链：students[0]["scores"]["语文"] → 90
# 3. 遍历嵌套：外层 for s in students:，内层 for subject, score in s["scores"].items()
#    items() 把字典变成 (键, 值) 对，一次拿两个变量（又是解包！）
# 4. 聚合统计的标准姿势：
#    totals = {}
#    for s in students:
#        for subject, score in s["scores"].items():
#            totals[subject] = totals.get(subject, 0) + score
#
# 【运行】python3 report.py

STUDENTS = [
    {"name": "甲", "scores": {"语文": 90, "数学": 80}},
    {"name": "乙", "scores": {"语文": 70, "数学": 90}},
]


def subject_average(students, subject):
    """TODO 1：某一科的全班平均分
    例如 subject_average(STUDENTS, "语文") → 80.0
    提示：累加每个学生 s["scores"].get(subject, 0)，再除以人数"""
    pass


def all_averages(students):
    """TODO 2：返回 {科目: 平均分} 字典（有几科算几科）
    例如 all_averages(STUDENTS) → {"语文": 80.0, "数学": 85.0}
    提示：先累加每科总分和人数（两个字典），最后相除"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("语文平均", subject_average(STUDENTS, "语文"), 80.0)
    _check("数学平均", subject_average(STUDENTS, "数学"), 85.0)
    _check("全科平均", all_averages(STUDENTS), {"语文": 80.0, "数学": 85.0})
    print("--- 全部 PASS 就可以提交 D018 了 ---")
