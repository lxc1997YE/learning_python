"""
使用集合
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算
"""
set1 = {1, 2, 3, 3, 3, 2}       #集合中不允许有重复的元素
print(set1)
print('length=', len(set1))
set2 = set(range(1, 10))
print(set2)
set1.add(4)     #add只能添加一个元素
set1.add(5)
set2.update([11, 12])       #update中可以添加入多个数到集合
print(set1)
print(set2)
set2.discard(5)     #若集合中没有5则会报错
print(set2)
for i in set2:
    print(i**2,end=' ')
print()
# 将元组转换成集合
set3 = set((1, 2, 3, 3, 2, 1))
print(set3.pop())
print(set3)
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))