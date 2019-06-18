# -*- coding: UTF-8 -*-

# Filename : 02-datetime.py
# author by : （学员ID)

# 目的:
# 掌握时间函数的概念
# 掌握集中不同的时间格式
# 掌握时间差的计算方式（加减乘除）
# 掌握将大尺度时间均转换为秒的方式

# 引入 datetime 模块
import datetime

now = datetime.datetime.now()
print("现在时间是：", end="")
print(now)
print("现在时间是：", end="")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 练习一
# 前后一小时
t1 = now - datetime.timedelta(hours=1)
print("之前1小时是：", t1)

t2 = now + datetime.timedelta(hours=1)
print("之后1小时是：", t2)

# 练习二
print("-----华丽分割线-----")
# 往后推任意天，小时，分钟，秒
now = datetime.datetime.now()
print("现在时间是：", now.ctime())
t2 = now - datetime.timedelta(days=0, hours=0, minutes=0, seconds=0)
print("调整后时间是：", t2.ctime())
print(t2.strftime("%Y-%m-%d %H:%S:%M"))

# 练习三
print("-----华丽分割线-----")
# 将时间转化为秒来计算
now = datetime.datetime.now()
future = now + datetime.timedelta(weeks=0, days=365, hours=0, minutes=0, seconds=0)
#future = now + datetime.timedelta(hours=1) * 2
#future = now + datetime.timedelta(days=365) * 80
interval = future - now  # 注意这里得出的结果是时间差， timedelta，而非秒
s = interval.total_seconds()
print("现在是：%s，将来是 %s" %(now, future))
print("现在将来相差 %0.2f 秒" %(s))
