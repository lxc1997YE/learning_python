"""
五种字符串切片方法

"""
from functools import reduce
# 方法一：字符串切片

result = s[::-1]

# 方法二：使用列表的reverse方法

s = input()
l = list(s)
l.reverse()
result = "".join(l)

# 方法三：使用reduce

result = reduce(lambda x, y: x + y, s)

# 方法四：使用递归函数

def fun(s):
    if len(s) < 1:
        return s
    return fun(s[1:]) + s[0]

result = fun(s)

# 方法五：使用栈结构

def fun(s):
    result = ""
    while len(l) > 0:
        result += l.pop()
    return result

result = fun(s)

# 方法六：for循环
def func(s):
    result = ""
    max_index = len(s)-1
    for index,value in enumerate(s):
        result += s[max_index-index]
    return result
result = func(s)
