# coding: utf-8

__author__ = 'Yemilice_lau'

"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""

"""
这道题要用二分法，所以一般的逻辑就不可用
"""
#
num = 25
#
# num_sqrt = num ** 0.5
#
# print(int(num_sqrt))

left = 0

right = num

while left < right:
    mid = (left + right) // 2 + 1
    # print(mid)
    square = mid * mid
    # print(square)

    if square > num:
        right = mid - 1
    else:
        left = mid


print(left)