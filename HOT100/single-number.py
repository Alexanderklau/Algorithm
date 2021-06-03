# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""

"""

这道题其实是位运算的题，但是我没搞明白
"""

import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        datas = collections.Counter(nums)
        for each in datas:
            if datas[each] == 1:
                return each




