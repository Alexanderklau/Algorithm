# coding: utf-8

__author__ = 'Yemilice_lau'

"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。

可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），

和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed2 = [0] + flowerbed + [0]

        sumtotal = len(flowerbed2)

        for i in range(0, sumtotal - 1):
            if i == 0:
                if flowerbed[i] == flowerbed2[i + 1] == flowerbed2[i + 2] == 0:
                    flowerbed2[i + 1] = 1
                    n -= 1
            elif i == sumtotal - 1:
                if flowerbed[i] == flowerbed2[i - 1] == flowerbed2[i +- 2] == 0:
                    flowerbed2[i - 1] = 1
                    n -= 1
            elif flowerbed2[i - 1] == flowerbed2[i] == flowerbed2[i + 1] == 0:
                flowerbed2[i] = 1
                n -= 1


        if n > 0:
            return False

        return True
