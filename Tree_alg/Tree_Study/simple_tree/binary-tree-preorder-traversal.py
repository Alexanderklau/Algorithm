# coding: utf-8

__author__ = 'Yemilice'

"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution(object):
    def __init__(self):
        self.z = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.work(root)
        return self.z

    def work(self, root):
        if root == None:
            return

        self.z.append(root.val)
        self.work(root.left)
        self.work(root.right)