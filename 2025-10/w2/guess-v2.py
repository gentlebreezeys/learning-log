# -*- coding: utf-8 -*-
# D010 · 10-10 · 猜数字 v2（while 循环 + random）
#
# 【讲义】
# 1. while 循环三要素：初始（n = 0）、条件（while n < 10）、更新（n += 1）
#    忘了更新 → 死循环，Ctrl+C 强制停止
# 2. break 跳出整个循环；continue 跳过本轮进入下一轮
# 3. random 模块：
#    import random
#    random.randint(1, 100)  # 1 到 100 之间的随机整数（两头都包含）
#
# 【运行】
#   python3 guess-v2.py        → 自检
#   python3 guess-v2.py play   → 玩真·随机版猜数字

import random


def even_sum(n):
    """TODO 1：计算 1 到 n 之间所有偶数的和（用 while 或 for 都行）
    例如 even_sum(10) → 30（2+4+6+8+10）"""
    pass


def main():
    answer = random.randint(1, 100)   # TODO 2: 这行已写好，读懂它
    tries = 0
    print("1-100 随机数已生成，开始猜！")
    while True:
        guess = int(input("第 %d 猜：" % (tries + 1)))
        # TODO 3: 用 w2/guess-v1.py 里你写的同样逻辑判断大小，
        #         猜对就打印鼓励语（带上总次数）并 break
        pass


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
        _check("even_sum(10)", even_sum(10), 30)
        _check("even_sum(1)", even_sum(1), 0)
        print("--- PASS 后 play 一局（提示：二分猜最快）再提交 D010 ---")
