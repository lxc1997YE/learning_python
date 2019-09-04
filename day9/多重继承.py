"""
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系

"""
class Father(object):
    def __init__(self,name):
        self._name= name

    def majiang(self):
        print('%s在打篮球.' % self._name)

    def eat(self):
        print('%s在大吃大喝.' % self._name)
class Monk(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在吃斋.' % self._name)

    def chant(self):
        print('%s在念经.' % self._name)


class Rapper(object):

    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s吃吃喝喝.' % self._name)

    def play_piano(self):
        print('%s在唱饶舌.' % self._name)

# class Son(Father,Monk,Rapper):
# class Son(Rapper, Monk, Father):
class Son(Father, Monk, Rapper):

    def __init__(self, name):
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Rapper.__init__(self, name)


son = Son('雷笑尘')
son.majiang()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()