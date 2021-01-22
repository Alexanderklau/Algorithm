# coding: utf-8

__author__ = 'Yemilice_lau'


"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，

输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1

示例 2：

输入：[2,2,2,0,1]
输出：0
"""

"""
说的很那啥，其实就是找出数组里面的最小值

这个可以直接min获取，但是人家一般不会这么简单，要用二分的处理逻辑
"""


def work():

    num = [3,4,5,1,2]

    left = 0

    right = len(num) - 1

    while left <= right:
        mid = (right + left) // 2
        if num[mid] < num[right]:
            right = mid
        elif num[mid] > num[right]:
            left = mid + 1
        else:
            right -= 1

    return num[left]


print(work())