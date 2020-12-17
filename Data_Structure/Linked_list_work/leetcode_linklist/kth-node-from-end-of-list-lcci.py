# coding: utf-8

__author__ = 'Yemilice_lau'


# 面试题 02.02. 返回倒数第 k 个节点

## 1.翻转链表 2. 组成列表

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def setNext(self, newNext):
        self.next = newNext

    def getNext(self):
        return self.next

class Solution(object):

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = ListNode(item)

        temp.setNext(self.head)

        self.head = temp

    def kthToLast(self, k):
        print(self.head.val)
        print(self.head.next.val)


    def length(self):
        currnet = self.head
        count = 0
        while currnet != None:
            count += 1
            currnet = currnet.next

        return count

    def getdata(self, index):
        currnet = self.head
        j = 0
        while currnet != None and j < self.length():
            if j == self.length() - index:
                return currnet.val
            else:
                currnet = currnet.next
            j += 1

v = Solution()

v.add(5)
v.add(4)
v.add(3)
v.add(2)
v.add(1)

# v.kthToLast(2)
# print(v.getIndex(2))
print(v.getdata(3))
