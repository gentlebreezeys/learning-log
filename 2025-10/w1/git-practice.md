# D003 · 10-03 · Git 三连：add / commit / log

## 为什么需要 Git

写代码就像存档打游戏：Git 给你的项目拍快照（提交），随时能回到任何一个存档点。
GitHub 是把这些存档同步到云端的仓库，别人（和一年后的你）都能看到。

## 三个基本命令

| 命令 | 作用 | 类比 |
|---|---|---|
| `git status` | 看当前哪些文件改了 | 检查背包里有什么新东西 |
| `git add 文件名` | 把文件放进"待拍快照"区 | 把东西摆进镜头 |
| `git commit -m "说明"` | 拍快照，附带说明 | 咔嚓拍照 |

外加一个看历史的：`git log --oneline`（一行一个快照）。

## 跟着做（在 learning-log 目录下）

```bash
git status                # 1. 看到 hello.py 是红色（未跟踪/已修改）
git add 2025-10/w1/hello.py
git status                # 2. 变成绿色（已进入待提交区）
git commit -m "D002: hello world 练习"
git log --oneline         # 3. 看到你的提交在最上面
```

## 常见坑

- **忘了 add 就 commit**：什么都没提交进去，先 `git status` 确认绿色
- **-m 后面忘写引号**：`git commit -m D002: 练习` 会报错，说明里有空格必须带引号
- **一次提交太多东西**：尽量一次提交 = 一天的工作，说明写清楚

## 今日任务

1. 把上面 4 条命令各跑一遍，读懂每条输出
2. 把 D002 的 hello.py 提交上去（如果昨天还没提交）
3. 把本文件也提交：`git add 2025-10/w1/git-practice.md && git commit -m "D003: git 三连练习"`
