# coding: utf-8

__author__ = 'Yemilice'


"""
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

 

示例 1:

输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
示例 2:

输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10
 

提示:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    visited[i][j] = 1
                    heapq.heappush(pq, (heightMap[i][j], i * n + j))

        res = 0
        dirs = [-1, 0, 1, 0, -1]
        while pq:
            height, position = heapq.heappop(pq)
            for k in range(4):
                nx, ny = position // n + dirs[k], position % n + dirs[k + 1]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and visited[nx][ny] == 0:
                    if height > heightMap[nx][ny]:
                        res += height - heightMap[nx][ny]
                    visited[nx][ny] = 1
                    heapq.heappush(pq, (max(height, heightMap[nx][ny]), nx * n + ny))
        return res
