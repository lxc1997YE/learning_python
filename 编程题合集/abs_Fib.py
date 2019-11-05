"""
给定一个正整数n， 计算n与斐波那契数最小数差值（绝对值）

"""
n = int(input())
a = 0
b = 1
pre = min(abs(n-a),abs(n-b))
while True:
    c = a + b
    t = abs(n - c)
    if t > pre:
        print(pre)
        break
    else:
        pre = t
    a = b
    b = c
