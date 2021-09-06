# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，

写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums)
        z = 0

        while z < end:
            mid = (start + end) // 2
            if nums[z] == target:
                return z
            if nums[z] < target:
                start = z
            if nums[z] > target:
                end = z
            z += 1
        return -1