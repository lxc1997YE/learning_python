#coding=utf=8
"""
掷骰子决定做什么事情

Date：2019-9-1
"""
from random import randint
face = randint(1,6)
if face == 1:
    things = "打架"
elif face == 2:
    things = "跳舞"
elif face == 3:
    things = "说唱"
elif face == 4:
    things = "100米跑"
elif face == 5:
    things = "大冒险"
else:
    things = "真心话"
print(things)