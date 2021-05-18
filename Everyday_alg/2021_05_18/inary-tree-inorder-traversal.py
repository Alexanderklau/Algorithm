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
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
"""

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        x = []
        def work(root):
            if root == None:
                return []

            left = work(root.left)
            x.append(root.val)
            right = work(root.right)
        work(root)
        return x