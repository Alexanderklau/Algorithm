# coding: utf-8

__author__ = "lau.wenbo"

"""
给你两个字符串数组 word1 和 word2 。如果两个数组表示的字符串相同，返回 true ；否则，返回 false 。

数组表示的字符串 是由数组中的所有元素 按顺序 连接形成的字符串。

 

示例 1：

输入：word1 = ["ab", "c"], word2 = ["a", "bc"]
输出：true
解释：
word1 表示的字符串为 "ab" + "c" -> "abc"
word2 表示的字符串为 "a" + "bc" -> "abc"
两个字符串相同，返回 true
"""

word1 = ["abcddefg"]


def check(wordlists):
    num = 0
    while num < len(wordlists):
        if num == 0:
            k = wordlists[0]
        else:
            k = k + wordlists[num]
        num += 1
    return k

