# coding: utf-8

__author__ = "lau.wenbo"


"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        for c in s:
            if s.count(c) == 1:
                return c
        return " "


