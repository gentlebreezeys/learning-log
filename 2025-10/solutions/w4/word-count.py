# -*- coding: utf-8 -*-
# D025 参考答案

def count_words(text):
    counts = {}
    for w in text.lower().split():
        counts[w] = counts.get(w, 0) + 1
    return counts


def top_words(text, n=10):
    counts = count_words(text)
    return sorted(counts.items(), key=lambda kv: -kv[1])[:n]
    # counts.items() 把 {"a": 2} 变成 [("a", 2)]
    # key=lambda kv: -kv[1] 按次数取负 → 从多到少


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("count_words", count_words("A a b"), {"a": 2, "b": 1})
    text = "the quick brown fox jumps over the lazy dog the end"
    _check("top1", top_words(text, 1), [("the", 3)])
    _check("top3", top_words(text, 3), [("the", 3), ("quick", 1), ("brown", 1)])
