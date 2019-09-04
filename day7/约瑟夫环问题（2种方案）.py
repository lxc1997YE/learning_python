"""
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将
其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人
开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9
的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于
难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。

"""
# 方案一
def main():
    persons = [True] * 30
    index, number, count = 0, 0, 0
    while count < 15:

        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                count += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')
if __name__ == '__main__':
    main()
# 方案二
"""
递归思路：
每次删除一个教徒我们就重新编号，难点就是找出删除前和删除后教徒编号的映射关系
人员30设为n 报到9自杀设为m
"""

#
# def f(n=30, m=9):
#     if n == 1:
#         return n
#     num = ''
#     num = (f(n - 1, m) + m - 1) % n + 1  # 返回存活士兵的编号
#     for nums in range(num):
#         print(nums)
#
#
# if __name__ == '__main__':
#     f()
