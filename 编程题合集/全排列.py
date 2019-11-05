"""
全排列 用递归方法
全排列：
1、列表只有一个元素[a]，它的全排列只有a。
2、列表有两个元素[a, b]，它的全排列为[a, b], [b, a]：
    { 将第一个元素a固定，对b进行全排列得到[a, b]。
    将第一个元素与第二个元素交换得到[b, a]。
    将b固定，对a进行全排列，得到[b, a] }
3、列表有三个元素[a, b, c]
    { 将a固定，对bc进行全排列{ 将b固定，对c全排列[abc]。交换bc，将c固定对b进行全排列[acb] }
     交换ab，[b, a, c] 对ac进行全排列{ ... }
     ... ...}
4、列表有n个元素，将第一个元素固定，对剩下n - 1个元素进行全排列。
    将第一个元素依此与其他元素交换，对每次交换后剩下的n-1个元素进行全排列。
5、对剩下的n - 1个元素全排列，同上，固定后对n - 2排列。
6、直到数组数量为1，全排列就是它自己，完成一次排列。
j = begin
for i in range(begin, end):  # 对begin到end的数组进行i次交换。
    data[i], data[j] = data[j], data[i]  # 交换。
    perm(data, begin + 1, end)  # 交换后对剩下数组进行全排列。[begin + 1, end]
    data[i], data[j] = data[j], data[i]  # 全排列完成后，换回原来的顺序，回到for进行下一次交换。
"""


def per(arr, begin, end):
    if begin == end:
        print(arr)
    else:
        for i in range(begin, end):
            arr[i], arr[begin] = arr[begin], arr[i]
            per(arr, begin + 1, end)
            arr[i], arr[begin] = arr[begin], arr[i]


arr = [1, 2, 3]
per(arr, 0, len(arr))
