# -*- coding: utf-8 -*-
# D006 · 10-06 · 中秋冲刺日（下）：文字横幅
#
# 【讲义】
# 1. 字符串乘法："=" * 8 → "========"
# 2. 多行字符串：三引号 """...""" 可以原样保留换行
# 3. len("中秋快乐") → 4（中文字符也算 1 个）
#
# 【运行】
#   python3 banner.py        → 自检
#   python3 banner.py play   → 看效果


def banner(text):
    """TODO 1：返回三行字符串，例如 banner("中秋快乐")：
    ========
      中秋快乐
    ========
    提示：line = "=" * (len(text) + 4)，中间行前面空两格"""
    pass


def lantern():
    """TODO 2（play 模式用）：打印一个 ASCII 灯笼，随便发挥，print 几行就行，例如：
       (/
      ///
     |~~|
     |--|
     '--'
    """
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
        print(banner("中秋快乐"))
        lantern()
    else:
        _check("banner", banner("中秋快乐"), "========\n  中秋快乐\n========")
        print("--- 全部 PASS 后，运行 python3 banner.py play 看看效果 ---")
