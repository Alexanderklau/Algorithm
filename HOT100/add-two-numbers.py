# coding: utf-8

__author__ = "lau.wenbo"

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""

"""
反转链表 相加 输出新
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_down_list = self.reverse(l1)
        l2_down_list = self.reverse(l2)
        l1_init = self.ListNodeToInt(l1_down_list)
        l2_init = self.ListNodeToInt(l2_down_list)
        l3_num = l1_init + l2_init
        return self.reverse(self.addListNode(l3_num))

    def reverse(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

    def addListNode(self, num):
        nums = map(int, str(num))
        head = ListNode(nums[0])
        p = head
        for i in range(1, len(nums)):
            p.next = ListNode(nums[i])
            p = p.next
        return head

    def ListNodeToInt(self, head):
        z = []
        while head != None:
            z.append(head.val)
            head = head.next

        lst1 = list(map(lambda x: str(x), z))

        str1 = ''.join(lst1)
        return int(str1)