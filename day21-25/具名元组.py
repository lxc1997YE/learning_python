from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
NewYork = City('NewYork', 'USA', 36.996, (35.568, 139.69874))
print(NewYork)
print(NewYork.name)
print(NewYork.coordinates)
print(City.name)
# 元组属性和方法
print(City._fields)

bord = [['_']*3 for i in range(3)]
print(bord)
bord[0][2] = 'X'
print(bord)

l2 = [["_"]*3]*3
print(l2)
# 打印结果中3个指向同一个对象
l2[0][2] = 1
print(l2)

row = ['_']*3
bord1 = []
for i in range(3):
    bord1.append(row)
print(bord1)

bord2 = []
for i in range(3):
    row2 = ['_'] * 3
    bord2.append(row2)
print(bord2)
bord2[2][0] = "X"
print(bord2)