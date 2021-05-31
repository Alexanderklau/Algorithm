# coding: utf-8

__author__ = "lau.wenbo"

"""

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head)

    def reverse(self, head):
        if head == None:
            return None
        if head.next == None:
            return head

        last = self.reverse(head.next)
        head.next.next = head