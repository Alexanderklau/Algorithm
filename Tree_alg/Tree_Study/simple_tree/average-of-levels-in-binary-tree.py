# coding: utf-8

__author__ = 'Yemilice'

"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

"""


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []

        queue = deque([root])

        res = []

        while queue:
            tmp = deque()
            for _ in range(len(queue)):
                node = queue.popleft()

                tmp.append(node.val)

                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

            z = len(list(tmp))
            sumz = sum(list(tmp))
            k = float(sumz) / float(z)
            res.append(k)
        return res
