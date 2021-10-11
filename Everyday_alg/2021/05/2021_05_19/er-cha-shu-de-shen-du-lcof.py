# coding: utf-8

__author__ = "lau.wenbo"

"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        result = []

        queue = deque([root])

        while queue:
            tmp = deque()

            for i in range(len(queue)):
                node = queue.popleft()

                tmp.append(node.val)

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

            result.append(list(tmp))

        return len(result)