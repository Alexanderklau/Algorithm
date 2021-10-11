# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

 

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

输入：head = [0,1,2], k = 4
输出：[2,0,1]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head


        nums = self.calculnum(head)
        k = k % nums
        c = 0

        fast = slow = head
        while c < k:
            fast = fast.next
            c += 1

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None
        return head



    def calculnum(self, head):
        z = 0
        while head != None:
            head = head.next
            z += 1
        return z