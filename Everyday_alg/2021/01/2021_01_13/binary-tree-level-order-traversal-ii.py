# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]

"""

"""
后序遍历

主要是涉及到层级遍历

这个就很那啥。
"""


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        tree_list = []
        tree = [root]
        while tree:
            tree_list.append([node.val for node in tree])
            temp = []
            for node in tree:
                temp.extend([node.left, node.right])
            tree = [leaf for leaf in temp if leaf]
        tree_list.reverse()
        return tree_list