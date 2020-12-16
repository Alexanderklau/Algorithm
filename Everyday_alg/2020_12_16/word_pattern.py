# coding: utf-8

__author__ = 'Yemilice_lau'

# 单词规律

"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        str1 = s.split(" ")

        if len(list(pattern)) != len(str1):
            return False

        print(len(set(zip(list(pattern), str1))), len(set(list(pattern))))
        if len(set(zip(list(pattern), str1))) == len(set(list(pattern))) == len(set(str1)):
            return True
        else:
            return False







a = "abba"
str1 = "dog cat cat dog"
v = Solution()
print(v.wordPattern(a, str1))