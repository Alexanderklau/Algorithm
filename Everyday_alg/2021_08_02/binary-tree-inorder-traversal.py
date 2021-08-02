# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
"""


class Solution(object):

    def __init__(self):
        self.num = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.innercrash(root)
        return self.num

    def innercrash(self, root):
        if root == None:
            return None

        self.innercrash(root.left)
        self.num.append(root.val)
        self.innercrash(root.right)