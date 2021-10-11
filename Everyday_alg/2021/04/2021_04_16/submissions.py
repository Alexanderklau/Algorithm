# coding: utf-8

__author__ = "lau.wenbo"


"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：


输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：


输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：


输入：p = [1,2,1], q = [1,1,2]
输出：false

"""


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.pre(p, q)

    def pre(self, root, root2):
        if not root and not root2:
            return True
        elif not root or not root2:
            return False
        elif root.val != root2.val:
            return False
        else:
            return self.pre(root.left, root2.left) and self.pre(root.right, root2.right)