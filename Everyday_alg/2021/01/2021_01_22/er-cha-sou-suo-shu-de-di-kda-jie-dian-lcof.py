# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        self.nums = []
        self.mid(root)
        return self.nums[len(self.nums) - k]

    def mid(self, root):
        if not root:
            return
        self.mid(root.left)
        self.nums.append(root.val)
        self.mid(root.right)