# coding: utf-8

__author__ = 'Yemilice_lau'


class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if A == None:
            return not B

        if B == None:
            return False

        return self.work(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def work(self, a, b):
        if b == None:
            return True

        if a == None and b != None:
            return False

        if a.val != b.val:
            return False

        return self.work(a.left, b.left) and self.work(a.right, b.right)