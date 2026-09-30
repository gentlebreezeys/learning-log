# -*- coding: utf-8 -*-
# D030 · 10-30 · 小项目：命令行日记本（本月毕业作品）
#
# 【讲义】综合运用：文件读写 + 字符串处理 + 函数拆分 + 异常防御
# 1. datetime 模块拿今天日期：
#    from datetime import date
#    date.today().isoformat() → "2026-10-30"（isoformat 是国际标准格式）
# 2. 存储格式：每行 "2026-10-30\t今天学会了文件读写"
#    \t 是制表符（Tab），日期和内容之间用它分隔（内容里有逗号也不怕）
# 3. str.split("\\t") 切回两半；str.startswith("2026-10") 可以按月过滤
#
# 【运行】
#   python3 diary.py        → 自检
#   python3 diary.py play   → 写日记（存到同目录 diary.txt）

import os
from datetime import date

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diary.txt")


def add_entry(path, text, day=None):
    """TODO 1：追加一行 "日期\\t内容"（"a" 模式！day 不传就用今天）
    提示：day = day or date.today().isoformat()"""
    pass


def load_entries(path):
    """TODO 2：读出所有条目，返回 [(日期, 内容), ...] 的列表
    文件不存在返回 []；空行跳过"""
    pass


def entries_on(path, day):
    """TODO 3：返回某一天的所有条目 [(日期, 内容), ...]
    提示：复用 load_entries，再按日期过滤"""
    pass


def main():
    print("日记本（直接输入内容=写一篇 / list=看全部 / q=退出）")
    while True:
        line = input("> ").strip()
        if line == "q":
            break
        if line == "list":
            for day, text in load_entries(DATA):
                print(f"[{day}] {text}")
        elif line:
            add_entry(DATA, line)
            print("已记下")


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        main()
    else:
        tmp = DATA.replace("diary", "_diary_test")
        add_entry(tmp, "学会文件读写了", day="2026-10-28")
        add_entry(tmp, "日记本完成", day="2026-10-30")
        add_entry(tmp, "又写一篇", day="2026-10-30")
        _check("load", load_entries(tmp), [
            ("2026-10-28", "学会文件读写了"),
            ("2026-10-30", "日记本完成"),
            ("2026-10-30", "又写一篇"),
        ])
        _check("entries_on", entries_on(tmp, "2026-10-30"), [
            ("2026-10-30", "日记本完成"),
            ("2026-10-30", "又写一篇"),
        ])
        os.remove(tmp)
        print("--- 全部 PASS，恭喜完成第一个月！明天是月复盘 D031 ---")
