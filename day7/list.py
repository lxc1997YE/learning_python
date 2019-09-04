"""
列表数据结构
"""
list1 = [1,3,5,7,100]
list2 = ['hello']*5
print(list1)
print(list2)
print(len(list1))   #计算list1的长度 5
print(list1[0])     #下标索引运算 1
print(list1[4])     #下标索引运算 100
#print(list1[5])     #报错 IndexError: list index out of range
print(list1[-1])    #100
print(list1[-2])    #7
list1[2] = 300
print(list1)        #[1, 3, 300, 7, 100]
list1.append(200)   #列表尾部加入200
list1.insert(1, 400)    #insert方法指定位置插入对象 第一个参数：指定的位置 第二个参数：传入的对象
list1 += (1000, 2000)   #等同append方法 尾部加上1000，2000
print(list1)
list1.remove(300)
# print(list1)
if 2000 in list1:
    list1.remove(2000)
del list1[0]
print(list1)
list1.clear()
print(list1)