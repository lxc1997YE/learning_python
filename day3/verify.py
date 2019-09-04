#coding=utf-8
"""
验证登录信息
"""
username = input('请输入用户名')
password = input('请输入密码')
if username == 'admin' and password == '123456':
    print('登陆成功')
else:
    print('登录失败')
