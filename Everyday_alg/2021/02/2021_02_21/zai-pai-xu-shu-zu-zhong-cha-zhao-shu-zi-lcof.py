# coding: utf-8

__author__ = "lau.wenbo"

"""
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

"""

"""
直接二分法

首先找到mid 

然后找到mid对应的值比对target的大小
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = self.getleft(nums, target)
        right = self.getright(nums, target)
        res = right - left + 1
        return res

    def getleft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        return left

    def getright(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return right