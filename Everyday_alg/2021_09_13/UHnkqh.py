# coding: utf-8

__author__ = "lau.wenbo"

"""
给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。

 

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

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):

        if head == None:
            return head

        cur = None
        pre = head

        while pre:
            temp = pre.next
            pre.next = cur
            cur = pre
            pre = temp

        return cur