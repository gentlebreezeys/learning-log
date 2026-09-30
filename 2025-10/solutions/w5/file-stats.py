# -*- coding: utf-8 -*-
# D027 参考答案

import os

SAMPLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.txt")


def count_lines(path):
    with open(path, encoding="utf-8") as f:
        return len(f.readlines())


def count_chars(path):
    with open(path, encoding="utf-8") as f:
        return len(f.read())


if __name__ == "__main__":
    def _check(name, got, want):
        if got == want:
            print("PASS", name)
        else:
            print("FAIL", name, "| 期望:", repr(want), "| 实际:", repr(got))
    _check("count_lines", count_lines(SAMPLE), 4)
    _check("count_chars", count_chars(SAMPLE), 28)
