# coding: utf-8

__author__ = 'Yemilice_lau'


def work():
    nums = [-1,0,3,5,9,12]

    target = 9


    left = 0

    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left += 1
        elif nums[mid] > target:
            right -= 1
        elif nums[mid] == target:
            return mid

    return -1

print(work())