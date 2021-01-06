# coding: utf-8

__author__ = "lau.wenbo"

class BinaryTree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def getRight(self):
        return self.rightChild

    def getLeft(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

if __name__ == '__main__':
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    print(r.getRootVal())
    print(r.getRight())
    print(r.getLeft())