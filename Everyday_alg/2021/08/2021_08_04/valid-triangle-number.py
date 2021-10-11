# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += k - j
        return ans
