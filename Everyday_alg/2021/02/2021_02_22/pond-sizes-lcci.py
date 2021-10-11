# coding: utf-8

__author__ = "lau.wenbo"

"""
你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。

若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。

编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

示例：

输入：
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
输出： [1,2,4]

"""

import collections

class Solution:
    def pondSizes(self, land):
        res = []
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col] == 0:
                    tmp = collections.deque()
                    tmp_count = 1
                    land[row][col] = -1  # 将访问的点标记进行标记
                    tmp.append([row, col])
                    while len(tmp) > 0:
                        x, y = tmp.popleft()
                        # 注意题目要求，斜向也要算，所以一共是 8 个方向
                        for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1],
                                             [x - 1, y - 1], [x - 1, y + 1], [x + 1, y + 1], [x + 1, y - 1]]:
                            if 0 <= new_x < len(land) and 0 <= new_y < len(land[0]) and land[new_x][new_y] == 0:
                                tmp_count += 1
                                land[new_x][new_y] = -1
                                tmp.append([new_x, new_y])
                    res.append(tmp_count)
        return sorted(res)