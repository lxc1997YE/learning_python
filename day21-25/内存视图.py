import array
# 通过改变数组中的一个字节来更新数组里某个元素的值
numbers = array.array('h', [-2, -1, 0, 1, 2])
menv = memoryview(numbers)
print(len(menv))
print(menv[0])
