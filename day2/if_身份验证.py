# coding=utf-8

username = raw_input('请输入用户名：')
password = raw_input('请输入密码：')
# input 是python3的语法，本机上是python2.7 使用可能会报错
# 改为使用raw_input即可 或者 用到了input框，当我们在输入想输入的字符串时 在那个字符串外层加上" "或者' '
# 如："office"
if username == 'admin' and password == '123456':
    print ('登录成功')
else:
    print ('登录失败')
