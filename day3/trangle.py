#coding=utf-8
"""
输入三角形三边的值，判断是否能构成三角形
如果可以 计算三角形的周长和面积

"""
#要用到math中的sqrt函数
import math


a = float(input("边长a:"))
b = float(input("边长b:"))
c = float(input("边长c:"))
if a+b>c and a+c>b and b+c> a:
    print('周长等于%.2f'% (a+b+c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积: %.2f' % (area))
else:
    print("三角形不成立")