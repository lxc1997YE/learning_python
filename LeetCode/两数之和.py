"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum

"""

class Solution:


    # def twoSum(self, nums, target):
    # 方法一：暴力解法 找到num2 = target - num1是否也在nums里面
    # num2 in nums 如果是Ture说明有戏， nums.index(num2) 查找num2的索引
    # count()方法用来查找出现次数
    #     lens = len(nums)
    #     j = -1
    #     for i in range(lens):
    #         if (target - nums[i]) in nums:
    #             if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]): # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
    #                 continue
    #             else:
    #                 j = nums.index(target-nums[i], i+1)   # index(x,i+1)是从num1后的序列后找num2
    #                 break
    #     if j > 0:
    #         return [i, j]
    #     else:
    #         return []
    # def twoSum(self, nums, target):
        # 方法二：法一的优化，因为num2不需要每次都从num1中查找 只需要在num1之前或者之后即可
        # lens = len(nums)
        # j = -1
        # for i in range(lens):
        #     temp = nums[i:]
        #     if(target - nums[i]) in temp:
        #         j = temp.index(target - nums[i])
        #         break
        # if j >= 0:
        #     return [i,j]
    def twoSum(self, nums, target):
        # 方法三 利用哈希表 利用字典记录而不是list,更方便查找
        hasmap = {}
        for inx, num in enumerate(nums):
            hasmap[num] = inx
        for i, num in enumerate(nums):
            j = hasmap.get(target - num)
            if j is not None and i != j:
                return [i, j]




number = [2, 7, 11, 15]
target = 9
a = Solution()  # 实例化类
print(a.twoSum(number, target))
