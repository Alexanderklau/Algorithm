# coding: utf-8

__author__ = 'Yemilice_lau'


"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内


示例 1:

n = 5

硬币可排列成以下几行:
¤
¤ ¤
¤ ¤

因为第三行不完整，所以返回2.

"""

n = 13

def agg(n):
    left = 0
    right = n
    while True:
        if left > right:
            return right
        mid = (left + right) // 2
        count = (1 + mid) * mid / 2
        if count == n:
            return mid
        elif count < n:
            left = mid + 1
        else:
            right = mid - 1

print(agg(13))