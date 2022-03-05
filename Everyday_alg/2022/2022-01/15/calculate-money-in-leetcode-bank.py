# coding: utf-8

__author__ = 'Yemilice'


"""
Hercy 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。

最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。

给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。

 

示例 1：

输入：n = 4
输出：10
解释：第 4 天后，总额为 1 + 2 + 3 + 4 = 10 。
示例 2：

输入：n = 10
输出：37
解释：第 10 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37 。注意到第二个星期一，Hercy 存入 2 块钱。
示例 3：

输入：n = 20
输出：96
解释：第 20 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96 。
"""


class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = n / 7

        v = n - (a * 7)

        return self.othersum(a, v) + self.sumforma(a)

    def sumforma(self, n):
        sums = 0
        for z in range(0, n):
            a = [i + z for i in range(1, 8)]
            sums += sum(a)
        return sums

    def othersum(self, n, v):
        sums = 0
        if v == 0:
            return sums
        else:
            a = [n + i for i in range(1, v + 1)]
            sums += sum(a)
        return sums