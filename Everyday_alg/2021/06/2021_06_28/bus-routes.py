# coding: utf-8

__author__ = "lau.wenbo"


"""

给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。

例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。
现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。

求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。

 

示例 1：

输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
输出：2
解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 
示例 2：

输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
输出：-1
"""

"""
最短路径问题

需要使用BFS算法
"""


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0

        n = len(routes)
        rmap = [[0] * n for _ in range(n)]

        start = set()
        end = set()

        for i, route in enumerate(routes):
            routes[i] = set(route)
            if source in routes[i]:
                start.add(i)
            if target in routes[i]:
                end.add(i)
            if start and start & end:
                return 1

        if not start or not end:
            return -1

        for i in range(n - 1):
            for j in range(i + 1, n):  # 构建邻接表
                if routes[i] & routes[j]:  # 如果两班线有公共站点
                    rmap[i][j] = rmap[j][i] = 1

        q = collections.deque([s for s in start])
        visit = Counter(start)  # 记录访问状态及路径长度的哈希表
        print(visit)
        while q:
            cur = q.popleft()
            cnt = visit[cur]
            if cur in end:  # 找到终点所在班线，停止
                return cnt
            for i in range(n):  # 放入当前班线可达且没访问过的班线
                if rmap[cur][i] and i not in visit:
                    q.append(i)
                    visit[i] = cnt + 1  # 并将其路径长度设为当前长度+1
        return -1