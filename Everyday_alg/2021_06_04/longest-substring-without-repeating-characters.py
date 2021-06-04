# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
"""

"""
这道题要用滑动窗口，我掌握的不好，需要回去继续复习

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        occ = set()

        n = len(s)

        ans = 0
        slow = -1

        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])

            while slow + 1 < n and s[slow + 1] not in occ:
                occ.add(s[slow + 1])
                slow += 1
            ans = max(ans, slow - i + 1)

        return ans

# fast = 1
# slow = 0
# z = []
# v = []
#
#
# while fast < len(s):
#     if s[slow] != s[fast] and s[fast] not in z:
#         z.append(s[slow])
#         slow += 1
#         fast += 1
#     elif s[slow] == s[fast]:
#         nums = len(z)
#         v.append(nums)
#         z.clear()
#         z.append(s[slow])
#         slow += 1
#         fast += 1
#     else:
#         slow += 1
#         fast += 1
#
# print(z)
# nums = len(z)
# v.append(nums)
#
#
# print(max(v))

