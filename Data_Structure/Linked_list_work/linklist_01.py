# coding: utf-8

__author__ = "lau.wenbo"

# 实现一个链表

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

    def isEmpty(self):
        return self.data == 0