#coding=utf-8
'''
英制单位英寸和公制单位厘米之间转换

Date：2019-9-1
'''

value = float(input("请输入长度:"))
unit = input("请输入单位:")
if unit == 'in' or unit == '英寸':
    print('%f英寸=%f厘米' % (value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%厘米=%f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')