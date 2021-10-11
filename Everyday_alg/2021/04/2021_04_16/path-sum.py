# coding: utf-8

__author__ = "lau.wenbo"

"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。


输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
"""

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if root:
            stack = [root]
            stack_val = [root.val]
            # 当 stack 有值
            while stack:
                currentNode = stack.pop()
                temp = stack_val.pop()
                if not currentNode.left and not currentNode.right:
                    if temp == targetSum:
                        return True
                    continue
                if currentNode.right:
                    stack.append(currentNode.right)
                    stack_val.append(currentNode.right.val + temp)
                if currentNode.left:
                    stack.append(currentNode.left)
                    stack_val.append(currentNode.left.val + temp)
        return False