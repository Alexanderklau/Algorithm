# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
"""

"""
判断 左树的左树等于右树的右树 and 左树 = 右树 and 左树的右树等于右树的左树

"""

class Solution(object):
    def isSymmetric(self, root):

        if root == None:
            return True


    def work(self, rootleft, rootright):
        if rootleft == rootright:
            return True

        if not rootright or not rootright:
            return False

        return (rootleft.val == rootright.val) and self.work(rootleft.left, rootright.right) and self.work(rootleft.right, rootright.left)