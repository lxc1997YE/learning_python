"""
斐波那契数列的几种求法
"""
# 第一种
# a = 0
# b = 1
# while b < 1000:
#     print(b)
#     a, b = b, a+b
# 递归


# 递归方式实现 生成前20项
lis = []
for i in range(20):
    if i == 0 or i == 1:  # 第1,2项 都为1
        lis.append(1)
    else:
        lis.append(lis[i - 2] + lis[i - 1])  # 从第3项开始每项值为前两项值之和

print(lis)


def fib(n):

    return 1 and n <= 2 or fib(n - 1) +fib(n - 2)
print(fib(10))