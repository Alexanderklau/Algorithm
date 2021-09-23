# coding: utf-8

__author__ = 'Yemilice_lau'


"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，

计算小孩有多少种上楼梯的方式。结果可能很大，

你需要对结果模1000000007。

示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
"""


class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 1

        if n == 2:
            return 2

        if n == 3:
            return 4

        a = 1
        b = 2
        c = 4
        sums = 0
        for i in range(3, n):
            sums = a + b + c
            sums = sums % 1000000007
            a = b
            b = c
            c = sums
        return sums