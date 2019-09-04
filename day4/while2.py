#coding=utf-8
"""
用while完成1-100之间偶数和
"""
sum, num = 0, 2
while num <= 100:
    sum += num
    num += 2
print(sum)