# coding: utf-8

__author__ = "lau.wenbo"

"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BFS(root):
    if root == None:
        return []

    queue = deque([root])

    result = []

    while queue:
        tmp = deque()
        for i in range(len(queue)):
            print(len(result))
            node = queue.popleft()
            if len(result) % 2:
                tmp.appendleft(node.val)
            else:
                tmp.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        result.append(list(tmp))
    return result

if __name__ == "__main__":
    tree = TreeNode("3")
    tree.left = TreeNode("9")
    tree.right = TreeNode("20")
    tree.right.left = TreeNode("15")
    tree.right.right = TreeNode("7")
    print(BFS(tree))
