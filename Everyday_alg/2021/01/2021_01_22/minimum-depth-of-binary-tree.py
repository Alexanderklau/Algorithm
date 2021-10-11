# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

输入：root = [3,9,20,null,null,15,7]
输出：2

"""


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and root.right != None:
            return 1 + self.minDepth(root.right)
        elif not root.right and root.left != None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))