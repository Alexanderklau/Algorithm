# coding: utf-8

__author__ = 'Yemilice_lau'



# 硬币面值
a = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]

# 每个面值的硬币数量
b = [11, 11, 5, 2, 6, 8, 2]


# 总钱数
def Cashcount(casha, cashb):
    s = 0
    for i in range(0, len(a)):
        s += casha[i] * cashb[i]
    return s

# 开始计算

z = len(a)

