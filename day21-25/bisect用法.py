import bisect

data = [2, 10, 6, 7, 9]
data.sort()
# insort返回插入数字之后列表的排序后结果，但比如确保之前列表已经是有序列表
bisect.insort(data, 0)
print(data)
# bisect.bisect返回的是插入数据的位置
bisect.bisect(data, 11)
print(bisect.bisect(data, 11))

# 利用bisect建立成绩查询表格
def grade(score, breapoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breapoints, score)
    return grades[i]
print([grade(score) for score in [33, 90, 77, 70, 89, 100]])
