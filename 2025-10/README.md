# 2025-10 · 学习材料总览

## 每天怎么用（4 步，约 1-2 小时）

1. **读讲义**：打开当天文件，顶部注释就是当天要学的概念和示例
2. **写练习**：把文件里标了 `TODO` 的函数写完（删掉那行 `pass`）
3. **跑自检**：终端运行 `python3 文件名.py`，看到全部 `PASS` 就算完成
4. **做提交**：`git add 文件` + `git commit -m "D0XX: 描述"`（D + 当天序号）

## 运行模式

- `python3 xxx.py` → 跑自检（看 PASS / FAIL）
- `python3 xxx.py play` → 交互模式（有 main 的程序才有效）
- `python3 mooncake.py` → 直接运行，弹出画布窗口（turtle 画图）

自检区（`不要改` 注释以下的部分）保持原样，它只认你写的函数对不对。

## 卡住了怎么办：20 分钟规则

一道题卡超过 20 分钟，去看 `solutions/` 里的同名文件，看懂后关掉、
自己重新写一遍再跑自检。看懂不等于会写。
（mooncake / banner / scope-quiz 没有答案文件：改着玩 / 运行即揭晓。）

## 本月文件地图

| Day | 日期 | 文件 | 主题 |
|---|---|---|---|
| D001 | 10-01 | w1/README-note.md | 开班（已完成） |
| D002 | 10-02 | w1/hello.py | print / input / f-string |
| D003 | 10-03 | w1/git-practice.md | git 三连（手册） |
| D004 | 10-04 | w1/week-notes.md | markdown 5 语法 + push（手册） |
| D005 | 10-05 | w1/exercises.py | 变量与类型 |
| D006 | 10-06 | w1/mooncake.py + banner.py | 中秋冲刺：turtle 画月饼 |
| D007 | 10-07 | w1/receipt.py | 输入与运算 |
| D008 | 10-08 | w1/name-format.py | 字符串方法 |
| D009 | 10-09 | w2/guess-v1.py | 条件语句 |
| D010 | 10-10 | w2/guess-v2.py | while 循环 + random |
| D011 | 10-11 | w2/drills.py | 99 乘法表 + FizzBuzz |
| D012 | 10-12 | w2/week-review.md | 周复盘（模板） |
| D013 | 10-13 | w3/shopping-list.py | 列表 |
| D014 | 10-14 | w3/stats.py | for 循环 |
| D015 | 10-15 | w3/rank.py | 排序 |
| D016 | 10-16 | w3/stats-v2.py | 元组与解包 |
| D017 | 10-17 | w3/contacts.py | 字典 |
| D018 | 10-18 | w3/report.py | 嵌套结构 |
| D019 | 10-19 | w3/todo-v1.py + week-review.md | 综合练习 |
| D020 | 10-20 | w4/stats-v3.py | 函数定义 |
| D021 | 10-21 | w4/todo-v2.py | 函数化重构 |
| D022 | 10-22 | （休整日） | 补欠账或休息 |
| D023 | 10-23 | w4/scope-quiz.py + rank-v2.py | 作用域 + enumerate |
| D024 | 10-24 | w4/todo-v3.py | 异常处理 |
| D025 | 10-25 | w4/word-count.py | 综合练习 |
| D026 | 10-26 | w4/week4-review.md | 周复盘（模板） |
| D027 | 10-27 | w5/file-stats.py + sample.txt | 文件读写 |
| D028 | 10-28 | w5/todo-v4.py | 持久化（txt） |
| D029 | 10-29 | w5/csv-demo.py + sample.csv | CSV |
| D030 | 10-30 | w5/diary.py | 小项目：命令行日记 |
