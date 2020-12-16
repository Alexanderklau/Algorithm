# coding: utf-8

__author__ = 'Yemilice_lau'

# 滑动窗口

class Queue:

    def __init__(self):
        self.queue = []
    def addnum(self, num):
        self.queue.insert(0, num)
    def addend(self, num):
        self.queue.append(num)
    def delnum(self):
        self.queue.pop()
    def delstart(self):
        self.queue.pop(0)
    def isEmpty(self):
        return self.queue == []
    def size(self):
        return len(self.queue)
    def peek(self):
        return self.queue[len(self.queue) - 1]
    def all(self):
        return self.queue


class Solution:
    def maxSlidingWindow(self, nums ,k):
        startindex = 0
        endindex = k
        z = []
        if not nums:
            return z
        while endindex < len(nums) + 1:
            max_num = (max(nums[startindex:endindex]))
            z.append(max_num)
            startindex += 1
            endindex += 1
        return z

v = Solution()
print(v.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
