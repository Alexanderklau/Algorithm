# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

"""


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        z = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                z.append(str(root.val) + "->" + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                z.append(str(root.val) + "->" + i)
        return z
