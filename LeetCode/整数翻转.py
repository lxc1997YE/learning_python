"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""
class Solution:
    def reverse(self, x):
        flag = 1 if x >= 0 else -1
        abs_x = abs(x)
        reversed_str = str(abs_x)
        reversed_x = reversed_str[::-1]
        reversed_int = int(reversed_x) * flag
        if -2 ** 31 <= reversed_int <= 2 ** 31 - 1:
            return reversed_int
        else:
            return 0


if __name__ == '__main__':
    x = 123456
    y = -123456
    a = Solution().reverse(x)
    b = Solution().reverse(y)
    print(a)
    print(b)
