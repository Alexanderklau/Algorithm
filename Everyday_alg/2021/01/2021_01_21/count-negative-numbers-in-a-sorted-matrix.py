# coding: utf-8

__author__ = "lau.wenbo"


"""
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 

请你统计并返回 grid 中 负数 的数目。

示例 1：

输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。

示例 2：

输入：grid = [[3,2],[1,0]]
输出：0
"""

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        k = 0
        for i in grid:
            for z in i:
                if z < 0:
                    k += 1
        return k