# coding: utf-8

__author__ = "lau.wenbo"

"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.defaultdict(int)
        for c in t:
            need[c]+=1

        needCnt=len(t)

        i=0
        res=(0,float('inf'))

        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:
                while True:
                    c=s[i]
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:
                    res=(i,j)
                need[s[i]]+=1
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]

