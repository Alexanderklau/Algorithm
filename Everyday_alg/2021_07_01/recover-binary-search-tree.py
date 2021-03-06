# coding: utf-8

__author__ = "lau.wenbo"

"""
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

 

示例 1：


输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
示例 2：


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.nums = []
    def recoverTree(self, root):
        """
        """
        x = None
        y = None
        pre = self.nums[0]

        for i in range(1, len(self.nums)):
            if pre.val > self.nums[i].val:
                y = self.nums[i]
                if not x:
                    x = pre
            pre = self.nums[i]

        if x and y:
            x.val, y.val = y.val, x.val




    def dfs(self, root):
        if root == None:
            return

        self.dfs(root.left)
        self.nums.append(root)
        self.dfs(root.right)