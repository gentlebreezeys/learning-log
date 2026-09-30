# -*- coding: utf-8 -*-
# D028 参考答案

import os

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo-data.txt")


def to_text(tasks):
    if not tasks:                  # 空列表存成空文件
        return ""
    lines = []
    for t in tasks:
        mark = "x" if t["done"] else " "
        lines.append(f"[{mark}] {t['title']}")
    return "\n".join(lines) + "\n"


def from_text(text):
    tasks = []
    for line in text.split("\n"):
        if not line.strip():
            continue
        tasks.append({
            "done": line.startswith("[x]"),
            "title": line[4:],     # 跳过开头的 "[x] " 或 "[ ] "
        })
    return tasks


def save(tasks, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(to_text(tasks))


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return from_text(f.read())


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks


def to_lines(tasks):
    lines = []
    for i, t in enumerate(tasks, start=1):
        mark = "x" if t["done"] else " "
        lines.append(f"{i}. [{mark}] {t['title']}")
    return "\n".join(lines)


def main():
    tasks = load(DATA)
    print("待办 v4（add 标题 / done 标题 / list / q）")
    while True:
        cmd = input("> ").strip()
        if cmd == "q":
            save(tasks, DATA)
            print("已保存到", DATA)
            break
        if cmd == "list":
            print(to_lines(tasks))
        elif cmd.startswith("add "):
            add_task(tasks, cmd[4:])
        elif cmd.startswith("done "):
            found = False
            for t in tasks:
                if t["title"] == cmd[5:]:
                    t["done"], found = True, True
            print("完成！" if found else "没有这个任务")


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
        ts = [{"title": "买牛奶", "done": True}, {"title": "写作业", "done": False}]
        _check("to_text", to_text(ts), "[x] 买牛奶\n[ ] 写作业\n")
        _check("from_text", from_text("[x] 买牛奶\n[ ] 写作业\n"), ts)
        _check("from_text空行", from_text("[x] 买牛奶\n\n"), [{"title": "买牛奶", "done": True}])
        tmp = DATA.replace("todo-data", "_todo_test")
        save(ts, tmp)
        _check("存取往返", load(tmp), ts)
        os.remove(tmp)
