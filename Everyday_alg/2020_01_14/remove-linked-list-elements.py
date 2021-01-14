# coding: utf-8

__author__ = 'Yemilice_lau'

"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""

"""
我的逻辑，加一个新的空节点放在头部，然后再去做循环和删除的操作。

链表的删除逻辑其实就是删除掉next，复制到下一个next去

哨兵节点
"""


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_node = ListNode(0)
        new_node.next = head

        prev, curr = new_node, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return new_node.next
