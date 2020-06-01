"""

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""


class Solution:
    def isPalindorme(self, x):
        # 方法一 转化字符串解法
        # if str(x) == str(x)[::-1]:
        #     return True
        # else:
        #     return False
        # 方法二 翻转数字
        if x < 0:
            return False
        m, n = x, 0
        while m:
            n = n * 10 + m % 10
            m = m // 10
        if x == n:
            return True
        else:
            return False


x = 123
print(Solution().isPalindorme(x))
