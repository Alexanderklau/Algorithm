# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，

找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，

其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。

同一个单元格内的字母在一个单词中不允许被重复使用。

输入：board = [
["o","a","a","n"],
["e","t","a","e"],
["i","h","k","r"],
["i","f","l","v"]
], 
words = ["oath","pea","eat","rain"]

输出：["eat","oath"]

输入：board = [["a","b"],["c","d"]], words = ["abcb"]

输出：[]

"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(word, idx, p, explored):
            if idx == len(word):
                return True
            if p in explored or p[0] < 0 or p[0] == m or p[1] < 0 or p[1] == n:
                return False
            if board[p[0]][p[1]] == word[idx]:
                explored.add(p)
                idx += 1
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    if dfs(word, idx, (p[0] + dx, p[1] + dy), explored):
                        return True
                explored.remove(p)
            return False

        m, n = len(board), len(board[0])
        cnts = Counter()
        for i in range(m):
            for j in range(n):
                cnts[board[i][j]] += 1
        ans = []
        for word in words:
            cur = Counter(word)
            canExists = True
            for c in cur:
                if cnts[c] < cur[c]:
                    canExists = False
                    break
            if not canExists:
                continue
            find = False
            for i in range(m):
                for j in range(n):
                    if dfs(word, 0, (i, j), set()):
                        ans.append(word)
                        find = True
                        break
                if find:
                    break
        return ans