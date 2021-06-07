# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        z = self.work(nums1, nums2)
        return self.length_work(z)

    def work(self, l1, l2):
        ins = 0
        ans = l1[:]
        for i in range(0, len(l2)):
            while ins < len(l1):
                if l2[i] < l1[ins]:
                    ans.insert(ins + i, l2[i])
                    break
                else:
                    ins += 1
            else:
                ans += l2[i:]
                break
        return ans

    def formatwork(self, num):
        return '%.6f' % num

    def length_work(self, nums):
        nums_count = len(nums)
        if nums_count == 0:
            return float(nums_count)

        if nums_count % 2 != 0:
            start_work = (nums_count // 2)
            return float(nums[start_work])
        else:
            start_work = (nums_count // 2)
            end_work = (nums_count) // 2 + 1
            minnum = nums[start_work - 1] + nums[end_work - 1]
            return float(minnum) / float(2)

