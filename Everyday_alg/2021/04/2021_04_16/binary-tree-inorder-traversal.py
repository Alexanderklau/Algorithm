# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。


输入：root = [1,null,2,3]
输出：[1,3,2]

"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 搞个全局的列表
        z = []

        if root == None:
            return []

        # 这边写个递归
        def dfs(root):
            if root:
                dfs(root.left)
                z.append(root.val)
                dfs(root.right)

        dfs(root)

        return z