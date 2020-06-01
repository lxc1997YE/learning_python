from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
# 旋转会把最后的三个元素移到左边，如果是负值则左移右
dq.rotate(3)
print(dq)
dq.rotate(-3)
print(dq)
dq.appendleft(-1)
print(dq)
dq.append(10)
print(dq)
dq.extend([11, 12, 13])
print(dq)