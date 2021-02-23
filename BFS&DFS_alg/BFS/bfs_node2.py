# coding: utf-8

__author__ = 'Yemilice_lau'


import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_tree(root):
    queue = collections.deque()
    queue.append((root.left, root.right))
    if not root:
        return
    while queue:
        left, right = queue.popleft()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append((left.left, right.right))
    return True

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)

    print(level_order_tree(tree))