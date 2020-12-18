# coding: utf-8

__author__ = 'Yemilice_lau'

from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        return next((Counter(t)-Counter(s)).elements())



v = Solution()
print(v.findTheDifference("ae","aea"))