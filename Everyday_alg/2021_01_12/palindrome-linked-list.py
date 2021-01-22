# coding: utf-8

__author__ = "lau.wenbo"

"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
"""

"""
这里，对比第一个和最后一个是否相等，然后逐渐回转，这里应该是双指针
"""


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        z = []
        node = head
        while node:
            z.append(node.val)
            node = node.next

        start = 0
        end = len(z) - 1

        while start < end:
            if z[start] != z[end]:
                return False
            start += 1
            end -= 1
        return True

