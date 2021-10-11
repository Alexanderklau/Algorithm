# coding: utf-8

__author__ = "lau.wenbo"

"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

示例 1：

输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234
示例 2：

输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455
示例 3：

输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021
示例 4：

输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000
"""


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        i1 = len(num) - 1
        carry = 0

        while i1 >= 0 or k != 0:
            if i1 >= 0:
                x = num[i1]
            else:
                x = 0

            if k != 0:
                y = k % 10
            else:
                y = 0

            sum = x + y + carry
            res.append(sum % 10)
            carry = sum // 10

            i1 -= 1
            k //= 10
        if carry != 0:
            res.append(carry)
        return res[::-1]