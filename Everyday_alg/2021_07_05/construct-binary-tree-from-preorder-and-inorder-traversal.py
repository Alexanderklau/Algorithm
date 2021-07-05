# coding: utf-8

__author__ = "lau.wenbo"


"""

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):

        if not preorder:
            return None

        t = preorder.pop(0)

        node = TreeNode(t)

        i = inorder.index(t)

        node.left = self.buildTree(preorder[:i], inorder[:i])
        node.right = self.buildTree(preorder[i:], inorder[i + 1:])
        return node



