"""
定义类，创建使用对象
关于类和对象：
类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有点像用概念在解释概念，
但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。在面向对
象编程的世界中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，
而且对象一定属于某个类（型）。当我们把一大堆拥有共同特征的对象的静态特征
（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。
"""


# 在Python中可以使用`class`关键字定义类，然后在类中通过之前学习过的函数来定义方法，
# 这样就可以将对象的动态特征描述出来，代码如下所示。
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看喜洋洋' % self.name)
        else:
            print('%s岛国爱情片' % self.name)


# > 写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。

# 创建使用对象
# 当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息
def main():
    stu1 = Student('雷笑尘', 22)
    stu1.study('python程序设计')
    stu1.watch_movie()
    stu2 = Student('刘亚凡', 16)
    stu2.study('软件测试')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
