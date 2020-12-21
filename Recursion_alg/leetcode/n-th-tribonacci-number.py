# coding: utf-8

__author__ = 'Yemilice_lau'


"""
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

 

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2 and n > 0:
            return 1
        elif n == 0:
            return 0
        else:
            return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)

