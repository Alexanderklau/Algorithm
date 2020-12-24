# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

"""

words = ["at", "ball",  "car","dad"]

def dichotomy(lists, item):
    if len(lists) == 0:
        return False

    else:
        points = len(lists) // 2
        if lists[points] == item:
            return True
        else:
            if item < lists[points]:
                return dichotomy(lists[:points], item)
            else:
                return dichotomy(lists[points:], item)


print(dichotomy(words, "ta"))