#coding=utf-8
"""
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E
"""

# grade = float(input("请输入成绩"))
# if grade>=90:
#     print("成绩不错为A")
# elif grade>=80:
#     print("成绩还行为B")
# elif grade>=70:
#     print("成绩一般为C")
# elif grade>=60:
#     print("成绩及格为D")
# else:
#     print("成绩不理想夏季继续努力E")
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)