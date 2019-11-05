"""
手撕冒泡排序和快速排序
"""


def bubbleSort(list):
    for i in range(len(list)):
        tem_res = False # 改进后的冒泡，设置一个交换标志位
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                tem_res = True # 这表示交换成功
        if not tem_res: # 这表示没有交换成功
            return list
    return list
list = [1,5,3,15,100,2]
bubbleSort(list)
for x in range(len(list)):
    print ("%d" %list[x])


