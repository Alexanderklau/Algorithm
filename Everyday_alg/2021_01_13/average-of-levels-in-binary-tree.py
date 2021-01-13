# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
"""


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        tree_lists, tree = [], [root]
        c = []
        while tree:
            work = [node.val for node in tree]
            c.append(self.midsum(work))
            temp = []
            for node in tree:
                temp.extend([node.left, node.right])
            tree = [leaf for leaf in temp if leaf]
        return c

    def midsum(self, lists):
        return float(sum(lists)) / float(len(lists))