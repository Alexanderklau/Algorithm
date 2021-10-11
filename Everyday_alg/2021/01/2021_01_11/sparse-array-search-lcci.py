# coding: utf-8

__author__ = 'Yemilice_lau'


"""
面试题 10.05. 稀疏数组搜索
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
"""


def work():
    words = ["DirNnILhARNS hOYIFB", "SM ", "YSPBaovrZBS", "evMMBOf", "mCrS", "oRJfjw gwuo", "xOpSEXvfI"]

    s = "mCrS"

    left, right = 0, len(words) - 1
    while left <= right:
        mid = left + (right - left) // 2

        temp = mid  # 记录一下mid的位置，因为下面要移动mid来寻找非空串，如果查找失败需要用temp来恢复位置
        while words[mid] == '' and mid < right:  # 如果mid对应空串则向右寻找
            mid += 1
        if words[mid] == '':
            # 该情况发生在mid走到了right-1的位置，如果right仍对应空，则说明temp右侧都是空，所以将右边界进行改变
            right = temp - 1
            continue
        if words[mid] == s:  # 该情况发生在mid在右移的过程中发现了非空串，则进行正常的二分查找
            return mid
        elif s < words[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(work())