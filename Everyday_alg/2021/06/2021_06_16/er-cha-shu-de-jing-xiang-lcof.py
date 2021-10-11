# coding: utf-8

__author__ = "lau.wenbo"

"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""

"""
翻转二叉树？
"""

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        queue = [root]

        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root
