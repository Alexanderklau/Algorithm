# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

 

示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释： 
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"

"""

s = "cba"

pairs = [[0,1],[1,2]]




def exchange(strs, startindex, endindex):
    s = list(strs)
    s[startindex], s[endindex] = s[endindex], s[startindex]
    return "".join(s)

nums = len(pairs)

n = 0

while n < nums:
    s = exchange(s, pairs[n][0], pairs[n][1])
    print(s)
    n += 1

