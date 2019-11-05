arr = [1, 2, 3, 4, 5, 6]

arr2 = list(map(lambda x: x + 1, arr))
# for i in arr2:
#     print(i)
#
# a = [i+1 for i in arr]
# print(a)
# print(arr2)
arr.append(7)
arr.pop(4)
print(arr)
# a = (1,2,"a")
# print(id(a))
# a = (1,2)
# print(id(a))
b = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7]
print(set(b))
for i, j in enumerate(arr):
    print(i,j)

