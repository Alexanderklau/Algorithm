# coding: utf-8

__author__ = 'Yemilice_lau'


"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

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
        tree_lists = []
        tree = [root]
        while tree:
            tree_lists.append([node.val for node in tree])
            temp = []
            for node in tree:
                temp.extend([node.left, node.right])
            tree = [leaf for leaf in temp if leaf]
        return tree_lists
