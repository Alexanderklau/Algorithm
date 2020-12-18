# coding: utf-8

__author__ = 'Yemilice_lau'

lists = [1, 2, 3, 4, 5, 6]

def listsum(lists_all):
    if len(lists_all) == 1:
        return lists_all[0]
    else:
        return lists_all[0] + listsum(lists_all[1:])

print(listsum(lists))