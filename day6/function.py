"""
函数的定义和使用 - 计算组合数C(7,3)
"""
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
# print(factorial(5))
print(factorial(7) // factorial(3) // factorial(4))