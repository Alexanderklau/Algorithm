# coding: utf-8

__author__ = "lau.wenbo"

# 实现一个链表

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newNext):
        self.next = newNext

    def repr_data(self):
        return str(self.data)

    def repr_next(self):
        return int(self.next)



class UnorderdList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)

        temp.setNext(self.head)

        self.head = temp

    def length(self):
        currnet = self.head
        count = 0
        while currnet != None:
            count += 1
            currnet = currnet.getNext()

        return count

    def getdata(self, item):
        current = self.head
        j = 0
        while current.getNext() and j < item:
            node = current.getNext()
            j += 1

        return node.data


    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def getIndex(self, item):
        j = 0
        if self.isEmpty():
            return

        node = self.head
        while node:
            if node.data == item:
                return j
            else:
                node = node.getNext()
            j += 1

        if j == self.length:
            return


    def addend(self):
        pass

z = UnorderdList()
z.add(123)
z.add(456)
z.add(789)
print(z.getIndex(789))
print(z.length())
print(z.getdata(789))