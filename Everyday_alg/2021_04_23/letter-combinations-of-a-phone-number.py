# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

输入：digits = "2"
输出：["a","b","c"]
"""

phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }



def DFS(dis):
    res = []
    stack = list(dis)
        # 当 stack 有值
    while stack:
        currentNode = phoneMap[stack.pop()]
        if not res:
            for i in currentNode:
                res.append(i)
        else:
            temp = res.copy()
            while temp:
                cur = temp.pop(0)
                res.pop(0)
                for i in currentNode:
                    res.append(cur + i)
    return res

print(DFS("23"))