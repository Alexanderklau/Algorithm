# coding: utf-8

__author__ = "lau.wenbo"


"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：

输入：[4,2,1]

输出：4

解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

示例 2：

输入：[2,3,10]

输出：8
"""

class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        z = 0
        for i in coins:
            z += self.work(i)
        return z


    def work(self, n):
        k = 0
        while n != 0:
            if n == 1:
                k += 1
                n = n - 1
            elif n == 2:
                k += 1
                n = n - 2
            elif n > 2:
                k += 1
                n = n - 2
        return k
