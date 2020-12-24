# coding: utf-8

__author__ = 'Yemilice_lau'

# 二分法 search


def dichotomy(lists, item):
    if len(lists) == 0:
        return False

    else:
        points = len(lists) // 2
        if lists[points] == item:
            return True
        else:
            if item < points:
                return dichotomy(lists[:points], item)
            else:
                return dichotomy(lists[points:], item)


print(dichotomy([1,2,3,4,5,6,7,78,10], 10))