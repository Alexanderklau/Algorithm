# coding: utf-8

__author__ = "lau.wenbo"


"""
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。

 

示例 1：

输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
示例 2：

输入：nums = [0,0,0,0,0], goal = 0
输出：15
 

提示：

1 <= nums.length <= 3 * 104
nums[i] 不是 0 就是 1
0 <= goal <= nums.length
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        presum = [0] + list(accumulate(nums))
        hashmap = defaultdict(int, {0:1})
        ans = 0
        for i in range(n):
            r = presum[i+1]
            l = r - goal
            ans += hashmap[l]
            hashmap[r] += 1
        return ans