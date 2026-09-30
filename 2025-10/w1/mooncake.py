# -*- coding: utf-8 -*-
# D006 · 10-06 · 中秋冲刺日（上）：turtle 画月饼
#
# 【讲义】turtle 是 Python 自带的画图模块，想象一只拿笔的乌龟听你指挥：
#   t.forward(100)  前进 100 步        t.circle(50)  画半径 50 的圆
#   t.penup()       抬笔（移动不留痕）  t.pendown()   落笔
#   t.color(边色, 填充色) + begin_fill()/end_fill()  给图形填色
#   t.goto(x, y)    去指定坐标          t.write("字")  在画布写字
#
# 【玩法】直接运行：python3 mooncake.py（会弹出画布窗口）
# 做完 3 个 TODO，截图存到 w1/ 目录（mooncake.png）一起提交！

import turtle

t = turtle.Turtle()
t.speed(0)

# 饼身：一个填色大圆
t.color("#8B5A00", "#E8A33D")     # TODO 1: 换成你喜欢的配色（边框色, 填充色）
t.begin_fill()
t.circle(100)
t.end_fill()

# 花纹：从中心出发，转一圈画小圆
t.color("#8B5A00")
petals = 8                         # TODO 2: 改成 12 看看效果
for i in range(petals):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 360 / petals)  # 每次转 360/petals 度
    t.forward(60)
    t.pendown()
    t.circle(18)

# 题字
t.penup()
t.goto(0, -130)
t.color("#8B5A00")
t.write("中秋快乐", align="center", font=("Arial", 24, "bold"))  # TODO 3: 改成你的祝福语

turtle.done()
