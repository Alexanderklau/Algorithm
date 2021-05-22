# coding: utf-8

__author__ = "lau.wenbo"

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 
示例 1：

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        left = None
        right = head
        while right:
            tmp = right.next
            right.next = left
            left = right
            right = tmp
        return left