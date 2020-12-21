# coding: utf-8

__author__ = 'Yemilice_lau'

"""
汉诺塔
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，

所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。

移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

你需要原地修改栈。

"""

"""
算法最擅长的其实就是不说人话

你想一下，三个柱子就是三个列表

你要从列表A移动一个顶端盘子到列表B，放到列表B底层，然后继续这个步骤，移动列表B中的盘子到列表C

公式：2^n - 1

"""

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    def move(self, n, A_lists, B_lists, C_lists):
        if n == 1:
            C_lists.append(A_lists[-1])
            A_lists.pop()
        else:
            self.move(n - 1, A_lists, C_lists, B_lists)
            C_lists.append(A_lists[-1])
            A_lists.pop()
            self.move(n - 1, B_lists, A_lists, C_lists)