# coding: utf-8

__author__ = "lau.wenbo"


"""
有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，

表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，

你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，

并返回该价格。 如果不存在这样的路线，则输出 -1。
"""

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        now=[float('inf')]*n
        now[src]=0
        ans=float('inf')
        for _ in range(k+1):
            aft=[float('inf')]*n
            for i,j,cost in flights:
                aft[j]=min(aft[j],now[i]+cost)
            now=aft
            ans=min(ans,now[dst])
        return -1 if ans==float('inf') else ans