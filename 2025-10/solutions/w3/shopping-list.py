# -*- coding: utf-8 -*-
# D013 参考答案

def add_item(items, name):
    items.append(name)
    return items


def remove_item(items, name):
    if name in items:              # 先确认存在再 remove，不会崩
        items.remove(name)
    return items


def find_item(items, name):
    for i, item in enumerate(items):
        if item == name:
            return i
    return -1


def list_items(items):
    return "\n".join("- " + x for x in items)


def main():
    items = []
    print("购物清单管理（add/del/find/q）")
    while True:
        print("\n当前清单:", items)
        cmd = input("> ").strip()
        if cmd == "q":
            break
        parts = cmd.split(" ", 1)
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
        _check("add", add_item([], "牛奶"), ["牛奶"])
        _check("remove", remove_item(["牛奶", "面包"], "牛奶"), ["面包"])
        _check("remove不存在", remove_item(["牛奶"], "啤酒"), ["牛奶"])
        _check("find", find_item(["牛奶", "面包"], "面包"), 1)
        _check("find不存在", find_item(["牛奶"], "啤酒"), -1)
        _check("list", list_items(["牛奶", "面包"]), "- 牛奶\n- 面包")
