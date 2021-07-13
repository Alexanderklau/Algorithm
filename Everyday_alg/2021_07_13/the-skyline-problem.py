# coding: utf-8

__author__ = "lau.wenbo"


"""
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。

关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

"""


def getSkyline(self, buildings):
    # 把左边界和右边界的坐标保留下来
    x = [i[0] for i in buildings] + [i[1] for i in buildings]
    # 排序
    x.sort()
    index = 0
    heap = []
    res = [[0, 0]]
    # 从小到大的顺序循环边界的值
    for i in x:
        # index表示的是建筑的编号，找到建筑左边界等于i的建筑放到大根堆
        while index < len(buildings) and buildings[index][0] == i:
            # 大根堆存放的是（高，右边界）
            heapq.heappush(heap, (-buildings[index][2], buildings[index][1]))
            # 建筑编号加1
            index += 1

        # 大根堆的堆顶元素即建筑的最高值，如果这栋建筑的右边界小于等于i，即该建筑已经遍历完了，不需要了，则从堆中移出
        while heap and heap[0][1] <= i:
            heapq.heappop(heap)
        # 如果堆里有值，把堆顶的元素的高取出来
        h = -heap[0][0] if heap else 0
        # 和结果中的高进行对比，如果不相同，说明不在一条直线上，把该值添加到res中
        if h != res[-1][1]:
            res.append([i, h])

    return res[1:]