# coding: utf-8

__author__ = 'Yemilice_lau'


"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

 
示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

"""

"""
先反转链表

在遍历链表的值

组成新链表输出
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # j = 0
        # newlistnode = ListNode()
        # lists = self.getkthlist(head, k)
        # for i in lists:

        # return newlistnode
        fast, slow = head, head

        while fast and k > 0:
            fast, k = fast.next, k - 1
        while fast:
            fast, slow = fast.next, slow.next

        return slow