# -*- coding: utf-8 -*-
# D029 · 10-29 · CSV 表格文件（配合同目录的 sample.csv）
#
# 【讲义】
# 1. CSV = 逗号分隔的表格，Excel 能直接打开，最通用的数据交换格式
# 2. 为什么不用 "a,b,c".split(",")？因为字段里可能有逗号（"买,牛奶",3）
#    csv 模块帮你处理所有坑（引号、换行、中文）
# 3. 读：
#    import csv
#    with open(path, encoding="utf-8") as f:
#        rows = list(csv.DictReader(f))   # 第一行当表头，每行变字典
#    rows[0]["name"] → "甲"；rows[0]["score"] → "90"（注意：读进来是字符串！）
# 4. 写：
#    with open(path, "w", encoding="utf-8", newline="") as f:
#        writer = csv.DictWriter(f, fieldnames=["name", "score"])
#        writer.writeheader()
#        writer.writerows(rows)
#
# 【运行】python3 csv-demo.py

import csv
import os

SAMPLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.csv")


def load_students(path):
    """TODO 1：读 CSV → [{"name": "甲", "score": 90}, ...]
    注意把 score 转成 int（DictReader 读进来是字符串！）"""
    pass


def save_students(students, path):
    """TODO 2：写 CSV（表头 name,score），用 DictWriter，注意 newline="" """
    pass


def average_score(students):
    """TODO 3：全班平均分，保留 1 位小数
    例如 average_score(load_students(SAMPLE)) → 84.3"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
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
    print("--- 全部 PASS 就可以提交 D029 了 ---")
