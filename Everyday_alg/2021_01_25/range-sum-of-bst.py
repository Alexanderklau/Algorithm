# coding: utf-8

__author__ = "lau.wenbo"

"""
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32

输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)