"""
但是如果我们需要限定自定义类型的对象只能绑定某些属性，
可以通过在类中定义\_\_slots\_\_变量来进行限定。需要
注意的是\_\_slots\_\_的限定只对当前类的对象生效，对子类并不起任何作用。

"""
class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    person.play()
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True