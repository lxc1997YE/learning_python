import threading
import time
"""

def chi():
    print("%s 吃火锅开始：" % time.ctime())
    time.sleep(1)
    print("%s 吃火锅结束--" % time.ctime())

def heng():
    print("%s 哼着小曲开始:" % time.ctime())
    time.sleep(1)
    print("%s 哼着小曲结束--" % time.ctime())

if __name__ == "__main__":
    chi()
    heng()

单线程
"""
# # 多线程

#
# def chi():
#     print("%s 吃着火锅开始：" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：涮羊肉" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：涮牛肉" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：贡丸" % time.ctime())
#     time.sleep(1)
#     print("%s 吃火锅结束！" % time.ctime())
# def ting():
#     print("%s 哼着小曲1！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲2！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲3！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲4！" % time.ctime())
#     time.sleep(2)
#     print("%s 哼着小曲5！" % time.ctime())
#     time.sleep(2)
#
# threads = []
# t1 = threading.Thread(target=chi)
# threads.append(t1)
# t2 = threading.Thread(target=ting)
# threads.append(t2)
#
# if __name__ == '__main__':
#     for i in threads:
#         i.start()

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(),people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(),people))

class myThread(threading.Thread):
    def __init__(self, name, people):
        threading.Thread.__init__(self)
        self.threadname = name
        self.people = people
    def run(self):      # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadname)

        chiHuoGuo(self.people)  # 执行任务
        print("qq交流群：226296743")
        print("结束线程: " + self.name)

thread1 = myThread("xiaoming", "Thread1")
thread2 = myThread("xiaowang", "Thread2")

thread1.start()
thread2.start()

time.sleep(0.5)
print("退出主线程")