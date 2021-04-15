# coding: utf-8

__author__ = 'Yemilice_lau'

from collections import deque

class BinaryTree:
    def __init__(self, root, left=None, right=None):
        self.key = root
        self.left = left
        self.right = right

    # 插入右子节点
    def addright(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    # 插入左子节点
    def addleft(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    # 获取右子节点
    def getright(self):
        return self.right

    # 获取左子节点
    def getleft(self):
        return self.left

    # 获取根节点
    def setRootVal(self, obj):
        self.key = obj

    # 获取key值
    def getRootVal(self):
        return self.key

def preTraverse(root):
    if root == None:
        return
    print(root.key)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root):
    if root == None:
        return
    preTraverse(root.left)
    print(root.key)
    preTraverse(root.right)

def afterTraverse(root):
    if root == None:
        return
    preTraverse(root.left)
    preTraverse(root.right)
    print(root.key)

def BFS(root):
    if root == None:
        return

    # 队列化root
    queue = deque([root])

    result = []

    i = 0
    # 遍历root
    while queue:
        for _ in range(len(queue)):
        # 移去并且返回一个元素，queue 最左侧的那一个
            node = queue.popleft()
            # 获取node的详细情况
            result.append(node.key)
            # 访问左树
            left = node.left
            if left != None:
                queue.append(left)
            # 访问右树
            right = node.right
            if right != None:
                queue.append(right)
        i += 1
    return i


def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)

if __name__ == "__main__":
    visited = set()
    root = BinaryTree('A', BinaryTree('B', BinaryTree('D'), BinaryTree('E')),
                      BinaryTree('C', right=BinaryTree('F', left=BinaryTree("G"))))
    print(BFS(root))
