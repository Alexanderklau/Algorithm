"""
 # @ Author: Yemilice_lau
 # @ Create Time: 2024-08-14 23:02:04
 # @ Modified by: Yemilice_lau
 # @ Modified time: 2024-08-14 23:31:04
 # @ Description: This is leetcode everyday_alg: isArraySpecial
 """


class Solution:
    def searchBreakPoints(self, nums: List[int]) -> List[int]:
        breakPoints = [i for i in range(len(nums))]
        for i in range(len(nums) - 1, 0, -1):
            if (nums[i - 1] + nums[i]) % 2 == 1:
                breakPoints[i - 1] = breakPoints[i]
        return breakPoints

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        breakPoints = self.searchBreakPoints(nums)
        answer = []
        for start, end in queries:
            answer.append(breakPoints[start] >= end)
        return answer
