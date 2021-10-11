# coding: utf-8

__author__ = "lau.wenbo"

"""
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

示例 1：

输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
示例 2：

输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
示例 3：

输入：arr = [10,11,12]
输出：66
"""


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        x = self.getList(arr)
        a = 0

        for v in x:
            a += self.work(arr, v)

        return a

    def work(self, arr, list_i):
        i = list_i
        l = list_i
        index = 0
        n = 0
        count = 0
        for k in range(len(arr)):
            n = arr[index:i]
            if len(n) != l:
                continue
            index += 1
            i += 1
            count += sum(n)
        return count

    def getList(self, arr):
        k = []
        for i in range(1, len(arr) + 1):
            if i % 2 != 0:
                k.append(i)
            else:
                continue
        return k