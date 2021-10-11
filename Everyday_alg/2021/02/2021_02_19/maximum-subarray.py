# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1
示例 5：

输入：nums = [-100000]
输出：-100000
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        z = 0
        for i in nums:
            if  z > 0:
                z += i
            else:
                z = i
            a = max(a, z)
        return a

nums = [-2,1,-3,4,-1,2,1,-5,4]
v = Solution()
print(v.maxSubArray(nums))
