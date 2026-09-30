# -*- coding: utf-8 -*-
# D021 · 10-21 · 待办 v2（函数化重构）
#
# 【讲义】重构 = 在不改行为的前提下整理代码结构。
# 验证方法：自检（回归测试）必须和 v1 一模一样地全 PASS——
# 这就是"测试保护重构"，8 月会给整个产品做同样的事。
#
# 【任务】
# 1. 把 w3/todo-v1.py 的 4 个函数抄过来（自己重写一遍更好）
# 2. 把 main() 里每个分支抽成独立函数：handle_add / handle_done / handle_list
#    main 只负责读命令和分发，一眼能看懂整个程序的结构
#
# 【运行】
#   python3 todo-v2.py        → 自检（和 v1 相同的用例）
#   python3 todo-v2.py play   → 行为应与 v1 完全一致

def add_task(tasks, title):
    """TODO 1：同 v1——追加 {"title": title, "done": False}"""
    pass


def complete_task(tasks, title):
    """TODO 2：同 v1——标记完成返回 True，找不到返回 False"""
    pass


def pending(tasks):
    """TODO 3：同 v1——未完成任务标题列表"""
    pass


def to_lines(tasks):
    """TODO 4：同 v1——"1. [x] 标题" 格式的多行字符串"""
    pass


def handle_add(tasks, title):
    """TODO 5：调用 add_task 并打印反馈"""
    pass


def handle_done(tasks, title):
    """TODO 6：调用 complete_task，成功打印"完成！"，失败打印"没有这个任务" """
    pass


def handle_list(tasks):
    """TODO 7：调用 to_lines 打印（空列表打印"（空）"）"""
    pass


def main():
    tasks = []
    print("待办清单 v2（add 标题 / done 标题 / list / q）")
    while True:
        cmd = input("> ").strip()
        if cmd == "q":
            break
        if cmd == "list":
            handle_list(tasks)
        elif cmd.startswith("add "):
            handle_add(tasks, cmd[4:])
        elif cmd.startswith("done "):
            handle_done(tasks, cmd[5:])
        else:
            print("格式：add 买牛奶 / done 买牛奶 / list")


# ========== 自检区（不要改，与 v1 相同——重构不许改行为） ==========

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
        print("--- 和 v1 一样全 PASS？重构成功，提交 D021 ---")
