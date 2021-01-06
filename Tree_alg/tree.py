# coding: utf-8

__author__ = 'Yemilice_lau'



# 创建一个二叉树
def CreateTree(r):
    return [r, [], []]

# 插入左子树
def insertLeft(root, newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root

# 插入右子树
def insertRight(root, newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root

