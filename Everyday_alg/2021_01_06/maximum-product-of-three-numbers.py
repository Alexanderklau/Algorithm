# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24

特殊情况：
[-100,-98,-1,2,3,4]

"""

a = [1,2,3,4]

a.sort(reverse=True)

print(a)

print(max(a[0] * a[1] * a[2], a[0] * a[-1] * a[-2]))

