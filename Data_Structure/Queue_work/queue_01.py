# coding: utf-8

__author__ = 'Yemilice_lau'


class Queue:

    def __init__(self):
        self.queue = []

    def addnum(self, num):
        self.queue.insert(0, num)

    def delnum(self):
        self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[len(self.queue) - 1]

    def all(self):
        return self.queue



z = Queue()
z.addnum("1")

print(z.all())

z.addnum("2")

print(z.all())

z.delnum()

print(z.all())