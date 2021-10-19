# coding: utf-8

__author__ = 'Yemilice'


"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.work(root.left, root.right)

    def work(self, rootleft, rootright):
        if rootleft == rootright:
            return True

        if rootleft == None or rootright == None:
            return False

        return ((rootleft.val == rootright.val) and self.work(rootleft.left, rootright.right) and self.work(
            rootleft.right, rootright.left))