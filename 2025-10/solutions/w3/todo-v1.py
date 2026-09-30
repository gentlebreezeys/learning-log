# -*- coding: utf-8 -*-
# D019 参考答案

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks


def complete_task(tasks, title):
    for t in tasks:
        if t["title"] == title:
            t["done"] = True
            return True
    return False


def pending(tasks):
    result = []
    for t in tasks:
        if not t["done"]:
            result.append(t["title"])
    return result


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
    print("待办清单（add 标题 / done 标题 / list / q）")
    while True:
        cmd = input("> ").strip()
        if cmd == "q":
            break
        if cmd == "list":
            print(to_lines(tasks))
        elif cmd.startswith("add "):
            add_task(tasks, cmd[4:])
        elif cmd.startswith("done "):
            print("完成！" if complete_task(tasks, cmd[5:]) else "没有这个任务")
        else:
            print("格式：add 买牛奶 / done 买牛奶 / list")


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
        ts = []
        add_task(ts, "买牛奶")
        add_task(ts, "写作业")
        _check("add", ts, [{"title": "买牛奶", "done": False}, {"title": "写作业", "done": False}])
        _check("complete", complete_task(ts, "买牛奶"), True)
        _check("complete缺失", complete_task(ts, "睡觉"), False)
        _check("pending", pending(ts), ["写作业"])
        _check("to_lines", to_lines(ts), "1. [x] 买牛奶\n2. [ ] 写作业")
