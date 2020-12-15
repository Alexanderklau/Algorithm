# coding: utf-8

__author__ = 'Yemilice_lau'



class Stack:
    def __init__(self):
        self.stack = []
    def addnum(self, num):
        self.stack.append(num)
    def delnum(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[len(self.stack) - 1]
    def peek2(self):
        return self.stack[len(self.stack) - 2]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.stack == []
    def all(self):
        return self.stack

class Solution:
    def calPoints(self, ops) -> int:
        s = Stack()
        index = 0
        while index < len(ops):
            i = ops[index]
            if i == "C":
                s.delnum()
            elif i == "D":
                z = s.peek()
                s.addnum(int(z) * 2)
            elif i == "+":
                a1 = s.peek()
                a2 = s.peek2()
                s.addnum(int(a1) + int(a2))
            else:
                s.addnum(int(i))
            index += 1

        return sum(s.all())


if __name__ == "__main__":
    ops = ["5","-2","4","C","D","9","+","+"]
    v = Solution()
    print(v.calPoints(ops))