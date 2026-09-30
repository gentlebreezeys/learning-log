# -*- coding: utf-8 -*-
# D024 · 10-24 · 待办 v3（异常处理）
#
# 【讲义】
# 1. 程序遇到意外会"抛异常"然后崩溃，比如：
#    int("abc") → ValueError
#    [1,2][5]   → IndexError
#    {}["不存在"] → KeyError
# 2. try / except 接住异常，程序继续活：
#    try:
#        n = int(s)
#    except ValueError:
#        n = None
# 3. 只接你预期的异常类型（ValueError），裸 except 会把 bug 也藏起来
# 4. 用户输入 = 不可信的边界，所有 int(input()) 都该包一层
#
# 【运行】
#   python3 todo-v3.py        → 自检
#   python3 todo-v3.py play   → 试试输 abc，程序不崩了

def parse_int(s):
    """TODO 1：把字符串转成 int；转不动返回 None
    例如 parse_int("42") → 42；parse_int("abc") → None；parse_int(" 7 ") → 7
    提示：int(" 7 ") 能容忍首尾空格，这是 int 的特性"""
    pass


def parse_choice(s):
    """TODO 2：返回用户输入的菜单数字（1/2/3）；
    输入不是这些数字（包括字母、0、99）返回 None
    例如 parse_choice("2") → 2；parse_choice("abc") → None；parse_choice("0") → None"""
    pass


def add_task(tasks, title):
    """TODO 3：同 v2——追加 {"title": title, "done": False}"""
    pass


def complete_task(tasks, title):
    """TODO 4：同 v2——标记完成返回 True，找不到返回 False"""
    pass


def to_lines(tasks):
    """TODO 5：同 v2——"1. [x] 标题" 格式"""
    pass


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
        _check("parse_int", parse_int("42"), 42)
        _check("parse_int空格", parse_int(" 7 "), 7)
        _check("parse_int字母", parse_int("abc"), None)
        _check("parse_int小数", parse_int("4.5"), None)
        _check("parse_choice", parse_choice("2"), 2)
        _check("parse_choice字母", parse_choice("abc"), None)
        _check("parse_choice越界", parse_choice("0"), None)
        print("--- 全部 PASS 后 play 模式乱输一通，提交 D024 ---")
