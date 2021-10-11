# coding: utf-8

__author__ = "lau.wenbo"

"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

 

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
"""

class Solution:
    def findLength(self, A, B):
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        print(dp)
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans

z = Solution()
A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(z.findLength(A, B))