# coding: utf-8

__author__ = 'Yemilice_lau'


"""
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

示例 1：


输入：points = [[1,1],[2,2],[3,3]]
输出：3

输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
 
提示：
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同
通过次数30,656提交次数105,894
"""

"""
[1,1][2,1][3,1][4,1]

[1,1][1,2][1,3][1,4]

[1,1][2,2][3,3][4,4]

[1,4][2,3][3,2][4,1]

[3,1][4,2][5,3]

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

z [1.1 2.3 3.2 4.1 5.3]

z [1.4 2.3 3.2 4.1 5.3]

z [4.1 3.2 2.3 1.4]

z [4.1 3.2 5.3 1.4]

z [4.1 3.2 5.3 1.4]

规律 x 全一致，[4,3,2,1]，[1，1,1,1],[1,2,3,4]

规律 y        [1,2,3,4],[1,2,3,4]  [4,3,2,1]
                        [4,3,2,1]

"""

class Solution:

    def is_same(self,slope1,slope2): # 判断斜率是否相同
        if slope1[1] == 0 and slope2[1] == 0 and slope2[0]!=0: #如果两个斜率均为正无穷（竖着的直线）并且第二个点不是第i个点
            return True
        elif slope1[1] == 0 or slope2[1] == 0:                 #如果有一个斜率为正无穷，那么直接返回False
            return False
        else:
            if slope1[0]/slope1[1] == slope2[0]/slope2[1]:     #斜率相同返回True
                return True
            else:
                return False

    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)      #length为点的个数
        if length == 1:           #如果只有一个点，直接返回1
            return 1
        slope = [[[0,0]for i in range(length)]for i in range(length)]  # 存储斜率 [x,y] 斜率 x/y
        for i in range(length):
            for j in range(i+1,length):
                slope[i][j][0] = points[j][0] - points[i][0]
                slope[i][j][1] = points[j][1] - points[i][1]
                # 获取斜率  [x,y] x = x1 - x0,  y = y1 - y0  ，slope[i][j]表示从点i到点j的斜率

        set = 1
        for i in range(length):  # i到j的斜率和j到i的斜率相同，把表填写完整
            for j in range(set):
                slope[i][j] = slope[j][i]
            set += 1


        #接下来就是查找每行出现最多相同斜率的个数即可，就是本题答案
        count = 0
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                else:
                    flag = 1
                    for k in range(length):
                        if self.is_same(slope[i][j],slope[i][k]):
                            flag += 1
                    if flag > count:
                        count = flag
        return count