# coding: utf-8

__author__ = 'Yemilice_lau'


"""
A 和 B 在一个 3 x 3 的网格上玩井字棋。

井字棋游戏的规则如下：

玩家轮流将棋子放在空方格 (" ") 上。
第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
"X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
如果所有方块都放满棋子（不为空），游戏也会结束。
游戏结束后，棋子无法再进行任何移动。
给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。

如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。

 
示例 1：

输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
输出："A"
解释："A" 获胜，他总是先走。
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
示例 2：

输入：moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
输出："B"
解释："B" 获胜。
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "
示例 3：

输入：moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
输出："Draw"
输出：由于没有办法再行动，游戏以平局结束。
"XXO"
"OOX"
"XOX"

"""

"""
这个题。。。非常考验你的想象力

它是个坐标轴

0 1 2

1

2


第一步，都TM是左上角的0, 第一步是A下的，下到左上角就是0,0
第二步， B开始下，随便下，假设下到左下角，就是，0，2
第三步，A继续下，假设下到第一步旁边，就是0，1
"""

class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        a,c=[],[]
        for i in range(len(moves)):
            if i%2==0:
                a.append(moves[i])
                if (([0,0] in a) and ([1,1] in a) and ([2,2] in a)) or (([0,2] in a) and ([1,1] in a) and ([2,0] in a)) or (([0,0] in a) and ([0,1] in a) and ([0,2] in a)) or (([1,0] in a) and ([1,1] in a) and ([1,2] in a)) or (([2,0] in a) and ([2,1] in a) and ([2,2] in a)) or (([0,0] in a) and ([1,0] in a) and ([2,0] in a)) or (([0,1] in a) and ([1,1] in a) and ([2,1] in a)) or (([0,2] in a) and ([1,2] in a) and ([2,2] in a)):
                    return "A"
            else:
                c.append(moves[i])
                if (([0,0] in c) and ([1,1] in c) and ([2,2] in c)) or (([0,2] in c) and ([1,1] in c) and ([2,0] in c)) or (([0,0] in c) and ([0,1] in c) and ([0,2] in c)) or (([1,0] in c) and ([1,1] in c) and ([1,2] in c)) or (([2,0] in c) and ([2,1] in c) and ([2,2] in c)) or (([0,0] in c) and ([1,0] in c) and ([2,0] in c)) or (([0,1] in c) and ([1,1] in c) and ([2,1] in c)) or (([0,2] in c) and ([1,2] in c) and ([2,2] in c)):
                    return "B"
        if len(moves)!=9:
            return "Pending"
        else:
            return "Draw"
