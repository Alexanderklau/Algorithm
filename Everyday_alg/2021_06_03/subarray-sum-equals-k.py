# coding: utf-8

__author__ = "lau.wenbo"


"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
"""

"""
前缀和的技巧

额外开辟一个前缀和数组进行预处理

求出所有的和，然后进行穷举
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        dicts = {0 : 1}
        ans = 0
        sums_i = 0
        for i in range(0, len(nums)):
            sums_i += nums[i]
            sums_j = sums_i - k
            if sums_j in dicts:
                ans += dicts[sums_j]
            dicts[sums_i] = dicts.get(sums_i, 0) + 1
        return ans