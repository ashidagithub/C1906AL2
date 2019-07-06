# -*- coding: UTF-8 -*-

# Filename : 04-for.py
# author by : （学员ID)

# 目的:
# 掌握使用for语句

# 练习一
# 最简单的 for
for i in range(1, 10, 2) :
    print(i)

# 练习二
# 输出指定范围内的整数
# take input from the user
print("-----华丽分割线-----")
print("输出指定范围内所有整数：")
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
for num in range(lower, upper + 1):
    print(num)

练习三
# for 的基本结构

for i in range(1,10):
    # --- for body begin
    pass
    # --- for body end


for j in range(1,10):
    # --- for body begin
    print('No. %d times...' % (j) )
    # --- for body end

# 练习四
times = 3
for x in range(1,times):
    # --- for body begin
    print('x-No. %d times...' % (x) )
    for y in range(1,times):
        # --- for body begin
        print('\ty-No. %d times...' % (y) )
        for z in range(1,times):
            # --- for body begin
            print('\t\tz-No. %d times...' % (z  ) )
            print('\t\t\tx-y-z = %d-%d-%d ' % (x,y,z))
            # --- for body end
        # --- for body end
    # --- for body end
