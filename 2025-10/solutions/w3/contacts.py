# -*- coding: utf-8 -*-
# D017 参考答案

def add(contacts, name, phone):
    contacts[name] = phone         # 键不存在=新增，存在=覆盖
    return contacts


def find(contacts, name):
    return contacts.get(name)      # 不存在返回 None，不崩


def update(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return True
    return False                   # 不存在不新增


def delete(contacts, name):
    if name in contacts:
        del contacts[name]
        return True
    return False


def main():
    contacts = {}
    print("通讯录（add 名字 电话 / find 名字 / del 名字 / q）")
    while True:
        cmd = input("> ").strip()
        if cmd == "q":
            break
        parts = cmd.split()
        if len(parts) == 3 and parts[0] == "add":
            add(contacts, parts[1], parts[2])
        elif len(parts) == 2 and parts[0] == "find":
            print(find(contacts, parts[1]))
        elif len(parts) == 2 and parts[0] == "del":
            print("已删除" if delete(contacts, parts[1]) else "查无此人")
        else:
            print("格式：add 小明 138xxx / find 小明 / del 小明")


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
        c = {}
        add(c, "小明", "13800000000")
        _check("add", c, {"小明": "13800000000"})
        _check("find", find(c, "小明"), "13800000000")
        _check("find不存在", find(c, "小红"), None)
        _check("update成功", update(c, "小明", "13900000000"), True)
        _check("update生效", c["小明"], "13900000000")
        _check("update失败", update(c, "小红", "1"), False)
        _check("delete成功", delete(c, "小明"), True)
        _check("delete失败", delete(c, "小明"), False)
