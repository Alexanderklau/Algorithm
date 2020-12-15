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

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []

class Solution:
    def isValid(self, s: str) -> bool:
        work = Stack()
        balance = True
        index = 0
        while index < len(s) and balance:
            z = s[index]
            if z in "([{<":
                work.addnum(z)
            else:
                if work.isEmpty():
                    balance = False
                else:
                    start = work.delnum()
                    if not Spec_work(start, z):
                        balance = False
            index += 1

        if balance and work.isEmpty():
            return True
        else:
            return False


def Spec_work(start, end):
    starts = "([{<"
    ends = ")]}>"

    return starts.index(start) == ends.index(end)


v = Solution()
print(v.isValid("()[]{}"))

