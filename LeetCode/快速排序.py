def sort(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr)//2]
    left = [x for x in arr if x < mid]
    middle = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]

    return sort(left) + middle + sort(right)
print(sort([3, 6, 8, 19, 1, 5]))

