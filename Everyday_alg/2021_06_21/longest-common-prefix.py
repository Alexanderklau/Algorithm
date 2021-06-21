# coding: utf-8

__author__ = 'Yemilice_lau'

"""

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
 

提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        k = ""

        fast = 0

        slow = 1

        if len(strs) == 1:
            return strs[0]

        while slow <= len(strs) - 1:
            if fast == 0:
                str1 = strs[fast]
                str2 = strs[slow]
                k = self.get_work(str1, str2)
                fast += 1
                slow += 1
            else:
                str1 = k
                str2 = strs[slow]
                k = self.get_work(str1, str2)
                fast += 1
                slow += 1
        return k

    def get_work(self, str1, str2):
        v = ""
        nums = 0
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        while nums <= len(str2) - 1:
            if str1[nums] == str2[nums]:
                v += str2[nums]
                nums += 1
            else:
                return v
        return v