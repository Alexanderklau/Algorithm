# coding: utf-8

__author__ = 'Yemilice_lau'

"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。


在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。


示例 1:

输入: [0,1,3]
输出: 2

"""

# def missnumber(lists):
#     i = lists[0]
#     for z in lists:
#         if z != i:
#             return i
#         else:
#             i += 1
#             continue
#
# print(missnumber([0]))


def missnumber(lists):
    left = 0
    mid = 0
    right = len(lists)
    while (left < right):
        mid = left + ((right - left) // 2)
        if (lists[mid] == mid):
            left = mid + 1
        else:
            right = mid

    return left

print(missnumber([0,1,2,4]))