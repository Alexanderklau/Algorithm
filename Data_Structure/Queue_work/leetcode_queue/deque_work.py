# coding: utf-8

__author__ = 'Yemilice_lau'


class MyCircularDeque(object):

    def __init__(self, k):
        self.queue = []
        self.k = k
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """

    def insertFront(self, value):
        """
           Adds an item at the front of Deque. Return true if the operation is successful.
           :type value: int
           :rtype: bool
           """
        if len(self.queue) + 1  < self.k:
            self.queue.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value):

        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.queue) + 1 < self.k:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.queue) != 0:
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.queue) != 0:
            self.queue.pop()
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if len(self.queue) == 0:
            return -1
        return self.queue[len(self.queue) - 1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.queue == []

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if len(self.queue) == self.k:
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
param_1 = obj.insertFront(1)
param_2 = obj.insertLast(10)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()