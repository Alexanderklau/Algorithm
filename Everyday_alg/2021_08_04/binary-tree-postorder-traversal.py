# coding: utf-8

__author__ = "lau.wenbo"


"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


class Solution(object):
    def __init__(self):
        self.nums = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.work(root)
        return self.nums

    def work(self, root):
        if root == None:
            return

        self.work(root.left)
        self.work(root.right)
        self.nums.append(root.val)