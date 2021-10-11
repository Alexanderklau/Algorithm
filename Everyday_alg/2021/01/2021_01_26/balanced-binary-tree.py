# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。


输入：root = [3,9,20,null,null,15,7]
输出：true

输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.depath(root.left) - self.depath(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def depath(self, root):
        if not root:
            return 0
        return max(self.depath(root.left), self.depath(root.right)) + 1