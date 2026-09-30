# -*- coding: utf-8 -*-
# D025 · 10-25 · 单词计数器（本周综合练习）
#
# 【讲义】
# 1. split() 无参数：按任意空白切，"a  b\nc" → ["a", "b", "c"]
# 2. 计数的标准姿势（dict 累加）：
#    counts = {}
#    for w in words:
#        counts[w] = counts.get(w, 0) + 1
# 3. 按值排序：sorted(counts.items(), key=lambda kv: -kv[1])
#    items() 把 {"a": 2} 变成 [("a", 2)]；-kv[1] 表示按次数从多到少
# 4. 大小写归一：先 .lower() 再数，"The" 和 "the" 算一个词
#
# 【运行】python3 word-count.py

def count_words(text):
    """TODO 1：返回 {单词: 次数}，统计前先 lower()
    例如 count_words("A a b") → {"a": 2, "b": 1}"""
    pass


def top_words(text, n=10):
    """TODO 2：出现最多的 n 个词，返回 [(单词, 次数), ...] 按次数降序
    例如 top_words("the quick the lazy the end", 1) → [("the", 3)]
    提示：复用 TODO 1，再 sorted(counts.items(), key=lambda kv: -kv[1])[:n]"""
    pass


# ========== 自检区（不要改） ==========

def _check(name, got, want):
    if got == want:
        print("PASS", name)
    else:
        print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))


if __name__ == "__main__":
    _check("count_words", count_words("A a b"), {"a": 2, "b": 1})
    text = "the quick brown fox jumps over the lazy dog the end"
    _check("top1", top_words(text, 1), [("the", 3)])
    _check("top3", top_words(text, 3), [("the", 3), ("quick", 1), ("brown", 1)])
    print("--- 全部 PASS 就可以提交 D025 了 ---")
