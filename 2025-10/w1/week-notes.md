# D004 · 10-04 · Markdown 5 语法 + 推上 GitHub

## 必学的 5 个 markdown 语法

在 GitHub 上打开任何 .md 文件，右上角有 Preview 按钮可以预览效果。

| 语法 | 写法 | 效果 |
|---|---|---|
| 标题 | `# 一级标题` / `## 二级标题` | 字号递减的标题 |
| 列表 | `- 项目一`（或 `1. 第一`） | 圆点 / 数字列表 |
| 粗体斜体 | `**重要**` / `*强调*` | **重要** / *强调* |
| 代码 | 反引号包住 `` `print()` `` | 行内代码 |
| 链接 | `[文字](https://github.com)` | [文字](https://github.com) |

## push：把本地提交同步到 GitHub

```bash
git push          # 把本地的提交全部推到 GitHub
```

推送后打开 https://github.com/gentlebreezeys/learning-log 就能看到。
从今天起，每天提交完顺手 push 一次。

## 今日任务

用上面 5 个语法，把下面的周笔记模板填完（就写在本文件下方），然后提交 + push：

```markdown
## 第一周笔记（10-01 ~ 10-04）

- 本周完成：**列出你做完的东西**
- 学会了：*最重要的 3 个概念*
- 卡在哪里：`写下具体报错或不懂的概念`
- 相关链接：[学习计划](https://github.com/gentlebreezeys/learning-log)
```

提交：`git add . && git commit -m "D004: 第一周笔记" && git push`
