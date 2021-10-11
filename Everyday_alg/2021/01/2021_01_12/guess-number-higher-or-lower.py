# coding: utf-8

__author__ = "lau.wenbo"


"""
猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
 

示例 1：

输入：n = 10, pick = 6
输出：6
示例 2：

输入：n = 1, pick = 1
输出：1
"""

"""
经典二分题，二分算法，走你

但是这道题不讲人话，其实说白了，就是它有个内置函数，你每次获取到不同的参数，就自己来决定下标移动
"""


start = 0
end = 1
num = 1
while start <= end:
    mid = (end + start) // 2
    print(mid)
    if mid > num:
        end -= 1
    elif mid < num:
        start += 1
    elif mid == num:
        print(mid)

