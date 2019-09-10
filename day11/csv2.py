"""
写入csv文件
"""
import csv

class Players(object):
    def __init__(self, name, age, position):
        self._name=name
        self._age=age
        self._position=position

    def name(self):
        return self._name
    def age(self):
        return  self._age
    def position(self):
        return self._position

filename='player.csv'
player=[Players('雷笑尘',22,'控球后卫'),Players('科比',40,'得分后卫'),Players('詹姆斯',36,'小前锋')]

try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for player in Players:
            writer.writerow([player.name, player.age, player.title])
except BaseException as e:
    print('无法写入文件:', filename)
else:
    print('保存数据完成!')
