# coding: utf-8

__author__ = "lau.wenbo"


"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and root.right != None:
            return 1 + self.maxDepth(root.right)
        elif not root.right and root.left != None:
            return 1 + self.maxDepth(root.left)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))