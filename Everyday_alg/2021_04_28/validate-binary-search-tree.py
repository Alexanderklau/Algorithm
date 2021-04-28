# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""

"""
判断

左子树小于根树

右子树大于根树

直接false


"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root, left, right):
            if not root:
                return True
            print(left, right)
            loft = root.val

            if loft <= left or loft >= right:
                return False

            if not dfs(root.right, loft, right):
                return False

            if not dfs(root.left, left, loft):
                return False

            return True

        return dfs(root, float('-inf'), float('inf'))