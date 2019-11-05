"""
利用生成器解决斐波那契数列的问题
yield关键字变为生成器函数

"""

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for i in fib(6):
    print(i)

