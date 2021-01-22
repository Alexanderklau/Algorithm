# coding: utf-8

__author__ = "lau.wenbo"

"""
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。


示例 2：

输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。


示例 3：

输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
"""

nums = [1,2,3,4]

n = 0

size = len(nums)

k = []

end = 0

while n < size:
    if n <= 0:
        end = nums[0]
        k.append(end)
    else:
        end = end + nums[n]
        k.append(end)
    n += 1

print(k)

