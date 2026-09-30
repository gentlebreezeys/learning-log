# -*- coding: utf-8 -*-
# D028 · 10-28 · 待办 v4（持久化：关掉程序数据不丢）
#
# 【讲义】
# 1. 之前的程序一退出，内存里的数据就没了；存进文件才能"持久"
# 2. 存储格式自己设计：每行一个任务，"[x] 买牛奶" / "[ ] 写作业"
#    （这个格式 markdown 的任务列表也这么用，GitHub 能直接渲染）
# 3. 保存 = 数据变文本写入；加载 = 文本解析回数据
#    这对"序列化/反序列化"就是雏形（11 月会升级成 json，12 月再升级成数据库）
# 4. str.startswith("[x]") 判断完成状态；line[4:] 跳过开头的 "[x] " 取标题
#
# 【运行】
#   python3 todo-v4.py        → 自检
#   python3 todo-v4.py play   → 新增几个任务，退出再重开——还在！

import os

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo-data.txt")


def to_text(tasks):
    """TODO 1：任务列表 → 文本（每行 "[x] 标题" 或 "[ ] 标题"，行尾有 \n）
    例如 [{"title":"买牛奶","done":True}] → "[x] 买牛奶\\n" """
    pass


def from_text(text):
    """TODO 2：文本 → 任务列表（to_text 的逆运算）
    空行要跳过。例如 "[x] 买牛奶\\n[ ] 写作业\\n" → 两个任务的列表"""
    pass


def save(tasks, path):
    """TODO 3：把 to_text 的结果用 "w" 模式写入 path（记得 encoding="utf-8"）"""
    pass


def load(path):
    """TODO 4：读出整个文件（读不到就返回 []），交给 from_text
    提示：os.path.exists(path) 判断文件存在与否"""
    pass


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
        ts = [{"title": "买牛奶", "done": True}, {"title": "写作业", "done": False}]
        _check("to_text", to_text(ts), "[x] 买牛奶\n[ ] 写作业\n")
        _check("from_text", from_text("[x] 买牛奶\n[ ] 写作业\n"), ts)
        _check("from_text空行", from_text("[x] 买牛奶\n\n"), [{"title": "买牛奶", "done": True}])
        tmp = DATA.replace("todo-data", "_todo_test")
        save(ts, tmp)
        _check("存取往返", load(tmp), ts)
        os.remove(tmp)
        print("--- 全部 PASS 后 play 模式存两条，重开看看还在吗 ---")
