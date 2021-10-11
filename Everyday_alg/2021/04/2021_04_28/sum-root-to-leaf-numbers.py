# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
"""

class Solution(object):
    def sumNumbers(self, root):

        def dfs(root, nodeval):
            if root == None:
                return 0

            total = nodeval * 10 + root.val

            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, nodeval) + dfs(root.right, nodeval)
        return dfs(root, 0)