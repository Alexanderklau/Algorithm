# coding: utf-8

__author__ = "lau.wenbo"


"""
给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：

'A'：Absent，缺勤
'L'：Late，迟到
'P'：Present，到场
如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

按 总出勤 计，学生缺勤（'A'）严格 少于两天。
学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。
如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

 

示例 1：

输入：s = "PPALLP"
输出：true
解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。
示例 2：

输入：s = "PPALLL"
输出：false
解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        work = {}
        work["P"] = 0
        work["A"] = 0
        work["L"] = 0

        worklist = list(s)

        z = 0

        while z < len(worklist):
            if worklist[z] == "P":
                work["P"] += 1
            elif worklist[z] == "A":
                work["A"] += 1
                if work["A"] >= 2:
                    return False
            elif worklist[z] == "L":
                try:
                    if worklist[z] == "L" and worklist[z + 1]  == "L" and worklist[z + 2] == "L":
                        return False
                    else:
                        work["L"] = 0
                except:
                        work["L"] = 0
            z += 1
        return True