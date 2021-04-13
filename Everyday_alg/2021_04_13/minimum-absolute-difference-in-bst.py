# coding: utf-8

__author__ = "lau.wenbo"

"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
"""

"""
两个方法

第一个，遍历树，添加列表，算差值

第二个，中序遍历二叉树，处理每个节点值
"""

class Solution:
    def getMinimumDifference(self, root) -> int:
        #初始化，最小值赋值为无穷大，last_value记录上一个节点的值
        min_value, last_value = float("inf"), -1
        def pengding_num(val):
            nonlocal min_value, last_value
            #第一个节点赋值给last_value
            if last_value == -1:
                last_value = val
            else:
                #每次求差的绝对值的最小值，更新
                min_value = min(min_value, abs(val - last_value))
                last_value = val
        #中序遍历
        def mid_order(root):
            nonlocal min_value, last_value
            if root:
                mid_order(root.left)
                #处理当前节点
                pengding_num(root.val)
                mid_order(root.right)
        mid_order(root)
        return min_value
