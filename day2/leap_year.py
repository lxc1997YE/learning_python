# coding=utf-8
'''
判断年份是否为闰年
闰年判定标准：4的倍数，正百数，必须是400的倍数

是闰年输出ture，否则false
'''
year = int(input('请输入年份:'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print is_leap
