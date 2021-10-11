# coding: utf-8

__author__ = "lau.wenbo"

"""

给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。

两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。

注意，s 可能同时含有大写和小写字母。

如果 a 和 b 相似，返回 true ；否则，返回 false 。

 
示例 1：

输入：s = "book"
输出：true
解释：a = "bo" 且 b = "ok" 。a 中有 1 个元音，b 也有 1 个元音。所以，a 和 b 相似。

"""
yuan_list = ['a','e','i','o','u','A','E','I','O','U']

s = "AbCdEfGh"

i = 0

lists_s = list(s)

def check_work(lists):
    i = 0
    for z in lists:
        if z in yuan_list:
            i += 1
        else:
            continue
    return i

mid = len(s) // 2

start_work = lists_s[0:mid]

print(start_work)

end_work = lists_s[mid:len(s)]

print(end_work)
