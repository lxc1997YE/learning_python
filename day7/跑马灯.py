"""
生成跑马灯效果文字

"""
import os
import time

def mani():
    content = '欢迎来到德莱联盟......'
    while True:
        # 清屏
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    mani()
