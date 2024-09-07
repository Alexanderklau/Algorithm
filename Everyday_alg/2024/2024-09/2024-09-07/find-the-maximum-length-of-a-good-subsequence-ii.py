"""
 # @ Author: Yemilice_lau
 # @ Create Time: 2024-09-07 13:02:48
 # @ Modified by: Yemilice_lau
 # @ Modified time: 2024-09-07 13:03:18
 # @ Description:
 """

"""
给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在范围下标范围 [0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，

那么我们称这个整数序列为 好 序列。
请你返回 nums 中 好 
子序列
 的最长长度

示例 1：

输入：nums = [1,2,1,1,3], k = 2

输出：4

解释：

最长好子序列为 [1,2,1,1,3] 。

示例 2：

输入：nums = [1,2,3,4,5,1], k = 0

输出：2

解释：

最长好子序列为 [1,2,3,4,5,1] 。
提示：

1 <= nums.length <= 5 * 103
1 <= nums[i] <= 109
0 <= k <= min(50, nums.length)
"""


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [defaultdict(int) for _ in range(k + 1)]
        res = [0] * (k + 1)
        for x in nums:
            for i in range(k, -1, -1):
                f[i][x] = max(f[i][x] + 1, res[i - 1] + 1 if i else 0)
                res[i] = max(res[i], f[i][x])
        return res[k]
