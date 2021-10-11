# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        queue = deque([root])

        result = []

        while queue:
            tmp = deque()
            for i in range(len(queue)):
                node = queue.popleft()

                if len(result) % 2 == 0:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

            result.append(list(tmp))

        return result