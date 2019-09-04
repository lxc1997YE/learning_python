"""
字典是另一种可变容器模型，类似于我们生活中使用的字典，它可以存储任意类型对象
与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和
值通过冒号分开。下面的代码演示了如何定义和使用字典。
"""
scores = {'eminem':95, 'kanye': 99, 'drake': 80}
print(scores['eminem'])
print(scores['kanye'])
for elm in scores:
    print('%s\t---->\t%d'% (elm, scores[elm]))
# print()
scores['jay-z'] = 92
scores['jcole'] = 91
scores.update(lxc=90, kobe=100)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())  #从最后一项开始删除
print(scores.popitem())
print(scores.pop('乔丹', 100))    #删除指定项
print(scores)
# 清空字典
scores.clear()
print(scores)