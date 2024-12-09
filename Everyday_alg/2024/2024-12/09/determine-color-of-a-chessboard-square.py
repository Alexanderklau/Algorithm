"""
 # @ Author: Yemilice_lau
 # @ Create Time: 2024/12/9 22:37
 # @ Modified by: Yemilice_lau
 # @ Modified time: 2024/12/9 22:37
 # @ File: determine-color-of-a-chessboard-square.py
 # @ Description:
 """

"""
给你一个坐标 coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。

如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。
给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。

示例 1：

输入：coordinates = "a1"
输出：false
解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。
示例 2：

输入：coordinates = "h3"
输出：true
解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。
示例 3：

输入：coordinates = "c7"
输出：false
"""

"""
解题思路：
这个比较简单，有 a,b,c,d,e,f,g,h 8个底部，单数底对单数行为False，双数行对双数行为False，单数底对双数是True，双数对单数底是True

给定一个字典{a:1, b:2, c:3,d:4,e:5,f:6,g:7,h:8}

然后判定返回true或者false
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = coordinates[0]
        y = int(coordinates[1])
        return (ord(x) + y) % 2 != 0


