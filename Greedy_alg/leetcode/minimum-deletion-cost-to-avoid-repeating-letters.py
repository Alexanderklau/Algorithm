# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。

返回使字符串任意相邻两个字母不相同的最小删除成本。

请注意，删除一个字符后，删除其他字符的成本不会改变。


示例 1：

输入：s = "abaac", cost = [1,2,3,4,5]
输出：3
解释：删除字母 "a" 的成本为 3，然后得到 "abac"（字符串中相邻两个字母不相同）。
示例 2：

输入：s = "abc", cost = [1,2,3]
输出：0
解释：无需删除任何字母，因为字符串中不存在相邻两个字母相同的情况。
示例 3：

输入：s = "aabaa", cost = [1,2,3,4,1]
输出：2
解释：删除第一个和最后一个字母，得到字符串 ("aba") 。
"""

cost = [3,5,10,7,5,3,5,5,4,8,1]

s = "aaabbbabbbb"


class Solution(object):
    def minCost(self, s, cost):
        n = 0

        k = 0
        new_s = list(s)

        while n + 1 < len(cost):
            print(n)
            print(cost)
            print(new_s)
            print(new_s[n], new_s[n + 1])
            if new_s[n] == new_s[n + 1]:
                if cost[n] < cost[n + 1]:
                    k += cost[n]
                    new_s.pop(n)
                    cost.pop(n)
                    n -= 1
                else:
                    k += cost[n + 1]
                    new_s.pop(n + 1)
                    cost.pop(n + 1)
                    n -= 1
            n += 1
        return k

z = Solution()

print(z.minCost(s, cost))