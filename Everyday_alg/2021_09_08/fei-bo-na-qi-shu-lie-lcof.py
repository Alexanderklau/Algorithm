# coding: utf-8

__author__ = "lau.wenbo"


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1]
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n] % 1000000007