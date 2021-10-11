# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个由 0 和 1 组成的非空二维数组 grid ，用来表示海洋岛屿地图。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        arrived = [[False for j in range(col)] for i in range(row)]
        ans = 0

        def DFS(x, y):
            if x >= 0 and x < row and y >= 0 and y < col and not arrived[x][y] and grid[x][y] == 1:
                arrived[x][y] = True
                return 1 + DFS(x - 1, y) + DFS(x + 1, y) + DFS(x, y - 1) + DFS(x, y + 1)
            else:
                return 0

        for i in range(row):
            for j in range(col):
                area = DFS(i, j)
                if area > ans:
                    ans = area
        return ans