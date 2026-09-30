# -*- coding: utf-8 -*-
# D024 参考答案

def parse_int(s):
    try:
        return int(s)              # int 容忍首尾空格，所以 " 7 " 也能转
    except ValueError:
        return None


def parse_choice(s):
    n = parse_int(s)
    if n in (1, 2, 3):
        return n
    return None


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks


def complete_task(tasks, title):
    for t in tasks:
        if t["title"] == title:
            t["done"] = True
            return True
    return False


def to_lines(tasks):
    lines = []
    for i, t in enumerate(tasks, start=1):
        if t["done"]:
            mark = "x"
        else:
            mark = " "
        lines.append(f"{i}. [{mark}] {t['title']}")
    return "\n".join(lines)


def main():
    tasks = []
    print("待办 v3（1.新增 2.完成 3.列表 q.退出）——放心乱输，不会崩")
    while True:
        choice = parse_choice(input("选择: ").strip())
        if choice == 1:
            add_task(tasks, input("标题: ").strip())
        elif choice == 2:
            print("完成！" if complete_task(tasks, input("标题: ").strip()) else "没有这个任务")
        elif choice == 3:
            print(to_lines(tasks))
        elif choice is None:
            print("请输入 1 / 2 / 3")


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
        _check("parse_int", parse_int("42"), 42)
        _check("parse_int空格", parse_int(" 7 "), 7)
        _check("parse_int字母", parse_int("abc"), None)
        _check("parse_int小数", parse_int("4.5"), None)
        _check("parse_choice", parse_choice("2"), 2)
        _check("parse_choice字母", parse_choice("abc"), None)
        _check("parse_choice越界", parse_choice("0"), None)
