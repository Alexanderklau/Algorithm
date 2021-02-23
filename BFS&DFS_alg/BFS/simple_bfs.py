# coding: utf-8

__author__ = 'Yemilice_lau'

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def BFS(root):
    if root == None:
        return

    queue = deque([root])

    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)
        print(node.val)
        left = node.left
        if left != None:
            queue.append(left)
        right = node.right
        if right != None:
            queue.append(right)

    return result



if __name__ == "__main__":
    tree = TreeNode("A")
    tree.left = TreeNode("B")
    tree.right = TreeNode("C")
    tree.left.left = TreeNode("D")
    tree.right.right = TreeNode("E")
    tree.right.right.right = TreeNode("F")
    print(BFS(tree))

