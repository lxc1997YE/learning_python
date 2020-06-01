import numpy
# 对numpy.ndarray的行列进行基本操作
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = (3, 4)
print(a)
print(a[1])
print(a[:, 0])
print(a.transpose())