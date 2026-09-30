# -*- coding: utf-8 -*-
# D017 · 10-17 · 通讯录（字典）
#
# 【讲义】
# 1. 字典 dict：键值对，像真正的通讯录——按"名字"查"电话"
#    contacts = {"小明": "138xxx"}
# 2. 增改：contacts["小红"] = "139xxx"（键不存在=新增，存在=覆盖）
# 3. 查：contacts["小明"]（不存在会 KeyError 崩溃！）
#    安全查：contacts.get("小明") → 不存在返回 None
#    contacts.get("小明", "查无此人") → 不存在返回默认值
# 4. 删：del contacts["小明"] 或 contacts.pop("小明")（不存在会报错，先判断）
# 5. 判断键存在："小明" in contacts
#
# 【运行】
#   python3 contacts.py        → 自检
#   python3 contacts.py play   → 玩通讯录


def add(contacts, name, phone):
    """TODO 1：新增或覆盖一个联系人，返回 contacts"""
    pass


def find(contacts, name):
    """TODO 2：返回电话；不存在返回 None（用 get，不许崩溃）"""
    pass


def update(contacts, name, phone):
    """TODO 3：name 存在就改电话并返回 True；不存在返回 False（不要新增）"""
    pass


def delete(contacts, name):
    """TODO 4：name 存在就删除并返回 True；不存在返回 False"""
    pass


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
        print("--- 全部 PASS 后 play 一下再提交 D017 ---")
