"""
 # @ Author: Yemilice_lau
 # @ Create Time: 2024-08-15 23:27:01
 # @ Modified by: Yemilice_lau
 # @ Modified time: 2024-08-15 23:27:04
 # @ Description:
 """

"""
给你一个由 正整数 组成、大小为 m x n 的矩阵 grid。

你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 c1 的单元格移动到值为 c2 的单元格的得分为 c2 - c1 。

你可以从 任一 单元格开始，并且必须至少移动一次。

返回你能得到的 最大 总得分。
"""


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-float("inf")] * n for _ in range(m)]
        ret = -float("inf")

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1], grid[i + 1][n - 1])
            ret = max(ret, dp[i][n - 1] - grid[i][n - 1])
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1], grid[m - 1][j + 1])
            ret = max(ret, dp[m - 1][j] - grid[m - 1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(
                    dp[i + 1][j], dp[i][j + 1], grid[i + 1][j], grid[i][j + 1]
                )
                ret = max(ret, dp[i][j] - grid[i][j])

        return ret
