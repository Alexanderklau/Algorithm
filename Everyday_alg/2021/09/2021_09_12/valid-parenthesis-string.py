# coding: utf-8

__author__ = "lau.wenbo"

"""
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True
注意:

字符串大小将在 [1，100] 范围内。

"""

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_stack, star_stack = [], []
        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while left_stack and star_stack and star_stack[-1] > left_stack[-1]:
            left_stack.pop()
            star_stack.pop()
        return len(left_stack) == 0