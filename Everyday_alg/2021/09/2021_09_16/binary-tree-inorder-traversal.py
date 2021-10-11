# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

示例 1：

输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：

输入：root = [1,null,2]
输出：[1,2]
"""


class Solution(object):
    def __init__(self):
        self.num = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.num

    def dfs(self, root):
        z = []
        if root == None:
            return z

        if root.left != None:
            self.dfs(root.left)
        self.num.append(root.val)
        if root.right != None:
            self.dfs(root.right)