"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数
"""


# 参数默认值
# def f1(a, b=5, c=10):
#     return a + b * 2 + c * 3
#
#
# print(f1(1, 2, 3))
# print(f1(100, 200))
# print(f1(100))
# print(f1(c=2, b=3, a=1))
def f2(**nike):
    if 'name' in nike:
        print('欢迎你%s' % nike['name'])
    elif 'tel' in nike:
        print('你的联系方式是%s' % nike['tel'])
    else:
        print('没找到个人信息')


parm = {'name': '雷笑尘', 'age': 22}
f2(**parm)
f2(name='雷笑尘', age=22, tel='17513301675')

f2(user='雷笑尘', age=22, mobile='17513301675')
