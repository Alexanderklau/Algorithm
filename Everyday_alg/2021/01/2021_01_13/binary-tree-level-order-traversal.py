# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        tree_lists, tree = [], [root]
        while tree:
            tree_lists.append([node.val for node in tree])
            temp = []
            for node in tree:
                temp.extend([node.left, node.right])
            tree = [leaf for leaf in temp if leaf]
        return tree_lists