# -*- coding: utf-8 -*-
# D030 参考答案

import os
from datetime import date

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diary.txt")


def add_entry(path, text, day=None):
    day = day or date.today().isoformat()
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{day}\t{text}\n")


def load_entries(path):
    if not os.path.exists(path):
        return []
    entries = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            entries.append((parts[0], "\t".join(parts[1:])))   # 内容里再有 \t 也不怕
    return entries


def entries_on(path, day):
    result = []
    for d, text in load_entries(path):
        if d == day:
            result.append((d, text))
    return result


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


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        main()
    else:
        def _check(name, got, want):
            if got == want:
                print("PASS", name)
            else:
                print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
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
