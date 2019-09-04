"""
异常处理
"""


# def main():
#     f = None
#     try:
#         f = open('a.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('文件没有找到')
#     except LookupError:
#         print('指定了位置编码')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误')
#   finally 函数无论怎样都会执行 即使调用sys 模块exti（）函数退出python运行环境 也会执行
#     finally:
#         if f:
#             f.close()
# if __name__ == '__main__':
#     main()

def main():
    try:
    # """使用with关键字可以结束后自动释放资源，不需要在调用close（）函数"""
        with open('a.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('文件没有找到')

    except LookupError:
        print('指定了位置编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
if __name__ == '__main__':
    main()
