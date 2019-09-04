"""
运用@property
"""
class Person(object):
    def __init__(self,name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age=age
    def paly(self):
        if self._age <18:
            print('%s正看在喜洋洋' % self._name)
        else:
            print('%s正看在岛国爱情片' % self._name)

def main():
    person = Person('雷笑尘',15)
    person.paly()
    person.age = 18
    person.paly()
    # person.name = '李坤'      #  # AttributeError: can't set attribute

if __name__ == '__main__':
    main()