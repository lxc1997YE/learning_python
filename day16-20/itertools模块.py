"""
迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools
a1 = itertools.permutations('ABCD')
a2 = itertools.combinations('ABCDE', 3)
a3 = itertools.product('ABCD', '123')
print(a1)
print(a2)
print(a3)