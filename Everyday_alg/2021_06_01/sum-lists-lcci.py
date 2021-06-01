# coding: utf-8

__author__ = "lau.wenbo"

"""

给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
"""


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