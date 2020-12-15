# coding: utf-8

__author__ = 'Yemilice_lau'


# 实现一个栈

class Stack:

    def __init__(self):
        self.stack = []

    def addnum(self, num):
        self.stack.append(num)

    def delnum(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []


if __name__ == '__main__':
    z = Stack()
    z.addnum("123")
    z.addnum("456")
    print(z.peek())
    z.delnum()
    print(z.peek())
    print(z.size())