# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""

"""
和前面的题一样，但是这里需要一个记录值，当深度为偶数的时候，翻转链表

"""



class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        tree_lists, tree = [], [root]
        n = 0
        while tree:
            n += 1
            work = [node.val for node in tree]
            if n % 2 != 0:
                work.reverse()
            tree_lists.append(work)
            temp = []
            for node in tree:
                temp.extend([node.right, node.left])
            tree = [leaf for leaf in temp if leaf]
        return tree_lists