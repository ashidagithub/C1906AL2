# -*- coding: UTF-8 -*-

# Filename : 02-math.py
# author by : （学员ID)

# 目的:
# 掌握使用数学函数库，巩固输入及输出方法

import math

# -------------------------------
# 练习一
# 已知三角形的底为10cm， 输入任意的高，求其面积
a = float(input("输入三角形的底："))
h = float(input("输入三角形的高："))
s = a * h * 0.5
print ("三角形的面积为：{0}", s)

# -------------------------------
# 练习二
# 依据海伦公式求任意三角形面积
# 已知三角形三边a,b,c,半周长p,则S＝ √[p(p - a)(p - b)(p - c)] （海伦公式）（p=(a+b+c)/2）
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))

# 计算半周长
p = (a + b + c) / 2

# 计算面积
# 掌握 python 开根号的写法
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('三角形面积为 %0.2f' % area)

# -------------------------------
# 练习三
# 输入三角形的两边长度及其夹角，求其面积
# 已知三角形两边a,b,这两边夹角C,则S＝ab sinC /2
a = float(input("输入三角形第一边长："))
b = float(input("输入三角形第二边长："))
C = math.pi / 2
area = a * b * math.sin(C) / 2
print('三角形面积为 %0.2f' % area)
