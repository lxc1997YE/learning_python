"""
查找算法 1.顺序查找 2.折半查找
"""


def seq_search(items, key):
    """查找算法"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


print(seq_search([10, 20, 30, 40, 50], 10))


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


print(bin_search([10, 20, 30, 40, 50], 10))
