# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

"""


"""
1. 整数转字符串
2. 反转字符串
3. 转整数
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        plus_minus = ""
        reverse_x = ""
        if x < 0:
            plus_minus = "-"
            x = -x
        for i in str(x):
            reverse_x = i + reverse_x
        reverse_x = plus_minus +reverse_x
        if int(reverse_x) > pow(2,31)-1 or int(reverse_x) < pow(-2,31):
            return 0
        return int(reverse_x)




