# coding: utf-8

__author__ = "lau.wenbo"

"""
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 
限制：

1 <= s 的长度 <= 8
"""

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        self.res = []
        n = len(s)

        def backtrack(s, path):
            if not s:
                self.res.append(path)
            seen = set()
            for i in range(len(s)):
                if s[i] in seen: continue
                seen.add(s[i])
                backtrack(s[:i]+s[i+1:], path + s[i])

        backtrack(s, "")
        return self.res