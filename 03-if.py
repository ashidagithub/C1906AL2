# -*- coding: UTF-8 -*-

# Filename : 05-if.py
# author by : （学员ID)

# 目的:
# 掌握使用 if 语句

# 简单 if 语句
num = float(input("输入一个数字: "))
if num>0:
    print("正数")
else:
    print("负数")

# 内嵌 if 语句
num = float(input("输入一个数字: "))
if num >= 0:
   if num == 0:
       print("零")
   else:
       print("正数")
else:
   print("负数")

# elif 的使用
# 用户输入数字
num = float(input("输入一个数字: "))
if num > 0:
   print("正数")
elif num == 0:
   print("零")
else:
   print("负数")
