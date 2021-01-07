# coding: utf-8

__author__ = 'Yemilice_lau'


class tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getol(self):
        return self.key

def perorder(root):
    if root:
        print(root.getol())
        perorder(root.getleft())
        perorder(root.getright())
