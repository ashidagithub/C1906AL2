# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : （学员ID)

# 目的:
# 掌握字符串的一些常用变换方式
# 掌握字符串的简单运算和判断

#  -------------------------------
# 练习一
s = input("输入一串全部小写的英语：")
print("全部转化为大写后：%s\n" % (s.upper()))            # 把所有字符中的小写字母转换成大写字母

s = input("输入一串全部大写的英语：")
print("全部转化为大写后：%s\n" % (s.lower()))            # 把所有字符中的大写字母转换成小写字母

s = input("输入一串全部小写的英语句子：")
print("首字母转化为大写后：%s\n" % (s.capitalize()))     # 把第一个字母转化为大写字母，其余小写

s = input("输入一串全部小写的英语句子（必须带空格）：")
print("每个单词首字母转化为大写后：%s\n" % (s.title()))   # 把每个单词的第一个字母转化为大写，其余小写


# 练习二
print("-----华丽分割线-----")
s = input("请任意输入一串英语句子：")
print(s.islower()) # 判断所有字符都是小写

# print(s.isalnum()) # 判断所有字符都是数字或者字母
# print(s.isalpha()) # 判断所有字符都是字母
# print(s.isdigit()) # 判断所有字符都是数字
# print(s.islower()) # 判断所有字符都是小写
# print(s.isupper()) # 判断所有字符都是大写
# print(s.istitle()) # 判断所有单词都是首字母大写，像标题
# print(s.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

# 练习三
print("-----华丽分割线-----")
# 用户输入两串文字后合并输出
# 注：input() 返回一个字符串
text1 = input('输入第一串文本：')
text2 = input('输入第二串文本：')

# 求和
text3 = text1 + text2

# 显示计算结果
print ('新的字符串相加结果为：')
print (text3)
