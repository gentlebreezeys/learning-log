# -*- coding: utf-8 -*-
# D013 · 10-13 · 购物清单（列表）
#
# 【讲义】
# 1. 列表 list：有序、可增删改。items = []、items.append("牛奶")
# 2. "牛奶" in items → True/False（判断存在）
# 3. items.remove("牛奶") 删除第一个匹配项；不存在会直接报错 → 先用 in 检查
# 4. items.index("牛奶") 返回下标（从 0 开始）；不存在会报错
# 5. 本文件的结构是本月所有命令行程序的模板：
#    逻辑写成函数（能自检）+ main() 负责交互（play 模式体验）
#
# 【运行】
#   python3 shopping-list.py        → 自检
#   python3 shopping-list.py play   → 玩清单管理


def add_item(items, name):
    """TODO 1：把 name 加进 items（append），返回 items"""
    pass


def remove_item(items, name):
    """TODO 2：name 在列表里就删掉它；不在就原样返回（不许报错！）
    提示：先 if name in items: 再 remove"""
    pass


def find_item(items, name):
    """TODO 3：返回 name 的下标，不存在返回 -1
    提示：用 index() 的话要 try/except（D024 才学），今天自己写循环数下标"""
    pass


def list_items(items):
    """TODO 4：返回多行字符串，每行 "- 名字"
    例如 ["牛奶", "面包"] → "- 牛奶\n- 面包"
    提示："\n".join("- " + x for x in items) 或循环拼接"""
    pass


def main():
    items = []
    print("购物清单管理（add/del/find/q）")
    while True:
        print("\n当前清单:", items)
        cmd = input("> ").strip()
        if cmd == "q":
            break
        parts = cmd.split(" ", 1)   # 只切第一刀，名字里可以带空格
        if len(parts) != 2:
            print("格式：add 牛奶 / del 牛奶 / find 牛奶")
            continue
        op, name = parts
        if op == "add":
            add_item(items, name)
        elif op == "del":
            remove_item(items, name)
        elif op == "find":
            print("下标:", find_item(items, name))
        else:
            print("不认识的命令")


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
        _check("add", add_item([], "牛奶"), ["牛奶"])
        _check("remove", remove_item(["牛奶", "面包"], "牛奶"), ["面包"])
        _check("remove不存在", remove_item(["牛奶"], "啤酒"), ["牛奶"])
        _check("find", find_item(["牛奶", "面包"], "面包"), 1)
        _check("find不存在", find_item(["牛奶"], "啤酒"), -1)
        _check("list", list_items(["牛奶", "面包"]), "- 牛奶\n- 面包")
        print("--- 全部 PASS 后 play 一下再提交 D013 ---")
