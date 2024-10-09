"""
 # @ Author: Yemilice_lau
 # @ Create Time: 2024-09-07 13:02:48
 # @ Modified by: Yemilice_lau
 # @ Modified time: 2024-09-07 13:03:18
 # @ Description:
 """

"""
给你一个数组 nums 和一个整数 k 。你需要找到 nums 的一个
子数组
 ，满足子数组中所有元素按位或运算 OR 的值与 k 的 绝对差 尽可能 小 。换言之，你需要选择一个子数组 nums[l..r] 满足 |k - (nums[l] OR nums[l + 1] ... OR nums[r])| 最小。

请你返回 最小 的绝对差值。

子数组 是数组中连续的 非空 元素序列。

示例 1：

输入：nums = [1,2,4,5], k = 3

输出：0
解释：
子数组 nums[0..1] 的按位 OR 运算值为 3 ，得到最小差值 |3 - 3| = 0 。
示例 2
输入：nums = [1,3,1,3], k = 2
输出：
解释
子数组 nums[1..1] 的按位 OR 运算值为 3 ，得到最小差值 |3 - 2| = 1 。
示例 3：
输入：nums = [1], k = 10
输出：9
解释：
只有一个子数组，按位 OR 运算值为 1 ，得到最小差值 |10 - 1| = 9 。
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 子数组的and有限
        # nums[j] -> j 到 i的子数组and和
        ans = inf
        for i, v in enumerate(nums):
            ans = min(ans, abs(v - k))
            j = i - 1
            while j >= 0 and nums[j] & v != nums[j]:
                nums[j] &= v
                ans = min(ans, abs(nums[j] - k))
                j -= 1
            # 若nums[j] & v == nums[j]
            # 则nums[j - 1] & v = nums[j] & v & original_nums[j - 1] == nums[j - 1]
            # 到此处后面都不会更改
        return ans