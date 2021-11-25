# coding: utf-8

__author__ = 'Yemilice'

"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root

        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

        return root