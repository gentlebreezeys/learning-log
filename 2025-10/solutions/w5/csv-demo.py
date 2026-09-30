# -*- coding: utf-8 -*-
# D029 参考答案

import csv
import os

SAMPLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.csv")


def load_students(path):
    with open(path, encoding="utf-8") as f:
        rows = []
        for row in csv.DictReader(f):
            rows.append({"name": row["name"], "score": int(row["score"])})
        return rows


def save_students(students, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(students)


def average_score(students):
    total = 0
    for s in students:
        total += s["score"]
    return round(total / len(students), 1)


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    loaded = load_students(SAMPLE)
    _check("load", loaded, [
        {"name": "甲", "score": 90},
        {"name": "乙", "score": 78},
        {"name": "丙", "score": 85},
    ])
    _check("average", average_score(loaded), 84.3)
    tmp = SAMPLE.replace("sample", "_sample_test")
    save_students(loaded, tmp)
    _check("存取往返", load_students(tmp), loaded)
    os.remove(tmp)
