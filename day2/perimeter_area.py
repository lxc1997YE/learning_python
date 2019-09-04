# coding=utf-8
'''
输入圆的半径计算圆的周长和面积

'''
import math

radius = float(input('请输入半径:'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长为:%.2f' % perimeter)
print('面积为:%.2f' % area)
