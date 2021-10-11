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
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100

"""


class Solution(object):
    def __init__(self):
        self.kk = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traverse(root)
        return self.kk

    def traverse(self, root):
        if root == None:
            return
        self.traverse(root.left)
        self.kk.append(root.val)
        self.traverse(root.right)
