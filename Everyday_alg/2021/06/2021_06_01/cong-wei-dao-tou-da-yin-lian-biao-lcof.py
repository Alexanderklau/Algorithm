# coding: utf-8

__author__ = 'Yemilice_lau'


"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]

"""


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        return self.ListNodeToList(self.reverse(head))

    def reverse(self, head):
        if head == None:
            return None
        if head.next == None:
            return head

        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last

    def ListNodeToList(self, head):
        z = []
        while head != None:
            z.append(head.val)
            head = head.next
        return z

"""
class Solution(object):
    def reversePrint(self, head):
        ans = []
        next_ = None
        pre = None
        while head is not None:
            next_ = head.next
            head.next = pre
            pre = head
            head = next_
        
        while pre is not None:
            ans.append(pre.val)
            pre = pre.next
        return ans
"""
