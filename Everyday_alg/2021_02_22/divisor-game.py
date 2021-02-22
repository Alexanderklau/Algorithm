# coding: utf-8

__author__ = 'Yemilice_lau'

"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False。假设两个玩家都以最佳状态参与游戏。

 

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
"""

"""
不说人话的题

我来翻译一下，有 a，b两个选手，有一个固定值N，

a，b岁随机选择数字x开始，数字必须大于0并且小于N，然后用N - x 替换 N为新的固定值

然后持续下去，直到无法选择x

这里其实可以直接黑科技，判断 N 是否是偶数，当N是偶数，a必胜，否则a必输

但是这里我用动态规划处理问题

"""



N1 = 80

# def work(N):
#     return N % 2 == 0
#
# print(work(N))

def work(N):
    target = [0 for i in range(N + 1)]
    target[1] = 0
    if N <= 1:
        return False
    else:
        target[2] = 1
        for i in range(3, N + 2):
            for j in range(1, i // 2):
                if i % j == 0 and target[i - j] == 0:
                    target[i] = 1
                    break
        return target[N] == 1

print(work(N1))


