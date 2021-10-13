# coding: utf-8

__author__ = 'Yemilice_lau'


"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        z = []
        for i in range(1, n + 1):
            z.append(self.FIzzReturn(i))

        return z

    def FIzzReturn(self, i):
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0 and i % 5 != 0:
            return "Fizz"
        elif i % 3 != 0 and i % 5 == 0:
            return "Buzz"
        else:
            return str(i)