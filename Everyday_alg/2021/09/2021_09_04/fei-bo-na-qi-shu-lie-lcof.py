# coding: utf-8

__author__ = "lau.wenbo"


"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5
"""


"""
基础做法行不通，肯定会超时timeout

用dp的方法较为合适
"""
# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return self.fibs(n)
#
#     def fibs(self, n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#
#         return self.fibs(n - 1) + self.fibs(n - 2)


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n] % 1000000007







