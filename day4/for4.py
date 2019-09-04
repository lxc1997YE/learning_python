#coding=utf-8
"""
判断一个数是不是素数
Date:2019-9-1
"""
from math import sqrt
num = int(input('请输入一个数：'))
end = int(sqrt(num))
is_sushu = True
for x in range(2, end + 1):
    if num % x == 0:
        is_sushu = False
        break
if is_sushu and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)