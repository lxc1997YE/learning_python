"""
和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列
表中的一部分取出来创建出新的列表，代码如下所示。
"""
rappers = ['kanye', 'eminem', 'drake', 'jay-z']
rappers += ['migos', 'drdre', 'jcole']
for rapper in rappers:
    print(rapper.title(), end=' ')
print()
# print(len(rappers))
#列表切片
rappers2 = rappers[1:4]
print(rappers2)
# rappers3 = rappers  # 没有复制列表只创建了新的引用
# 可以通过完整切片操作来复制列表
rappers3 = rappers[:]
print(rappers3)
rappers4 = rappers[-3:-1]
print(rappers4)
rappers5 = rappers[::-1]  # 可以通过反向切片操作来获得倒转后的列表的拷贝
print(rappers5)
