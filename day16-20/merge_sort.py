"""
归并排序（分治法）

"""


def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge_sort(left, right, comp)

print(merge_sort([10,50,100,1,2,3]))
