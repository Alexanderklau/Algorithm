# coding: utf-8

__author__ = 'Yemilice'


"""
对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。

例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
给你一个整数 num ，输出它的补数。

示例 1：

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2：

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
"""


"""
先取二进制

再把1变0,0变1

再转10进制
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        z = self.binwork(num)

        n = self.work(z)

        x = self.twowork(n)
        print(x)

        return x

    def binwork(self, n):
        return bin(n)

    def twowork(self, n):
        return int(n, 2)

    def work(self, z):
        v = ""
        n = z.split("0b")[1]
        for i in n:
            if i == "1":
                k = "0"
            elif i == "0":
                k = "1"
            else:
                k = str(i)
            v += k
        return "0b" + v