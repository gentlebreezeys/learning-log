# -*- coding: utf-8 -*-
# D019 · 10-19 · 综合练习：待办事项 v1（本周知识全用上）
#
# 【讲义】
# 一个任务 = {"title": "买牛奶", "done": False}（字典）
# 任务列表 = [{...}, {...}]（列表装字典，D018 刚学）
# 今天不学新东西，把 w3 的列表、字典、循环、排序拼成一个程序。
#
# 【运行】
#   python3 todo-v1.py        → 自检
#   python3 todo-v1.py play   → 用待办清单

def add_task(tasks, title):
    """TODO 1：追加一个未完成的任务 {"title": title, "done": False}，返回 tasks"""
    pass


def complete_task(tasks, title):
    """TODO 2：把 title 对应任务标记为 done=True，返回 True；
    找不到返回 False（不改动列表）"""
    pass


def pending(tasks):
    """TODO 3：返回所有未完成任务的标题列表
    例如 pending([{"title":"a","done":True},{"title":"b","done":False}]) → ["b"]"""
    pass


def to_lines(tasks):
    """TODO 4：返回多行字符串展示所有任务：
    第 n 个任务一行，格式 "n. [x] 标题"（完成）或 "n. [ ] 标题"（未完成）
    例如两个任务 → "1. [x] 买牛奶\n2. [ ] 写作业"
    提示：enumerate(tasks, start=1) 可以直接拿到从 1 开始的序号"""
    pass


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
        ts = []
        add_task(ts, "买牛奶")
        add_task(ts, "写作业")
        _check("add", ts, [{"title": "买牛奶", "done": False}, {"title": "写作业", "done": False}])
        _check("complete", complete_task(ts, "买牛奶"), True)
        _check("complete缺失", complete_task(ts, "睡觉"), False)
        _check("pending", pending(ts), ["写作业"])
        _check("to_lines", to_lines(ts), "1. [x] 买牛奶\n2. [ ] 写作业")
        print("--- 全部 PASS 后 play 一下再提交 D019 ---")
