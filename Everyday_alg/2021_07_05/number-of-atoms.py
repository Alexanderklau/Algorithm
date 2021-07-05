# coding: utf-8

__author__ = "lau.wenbo"


"""

给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式 formula ，返回所有原子的数量。格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

 

示例 1：

输入：formula = "H2O"
输出："H2O"
解释：
原子的数量是 {'H': 2, 'O': 1}。
示例 2：

输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释： 
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
示例 3：

输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
示例 4：

输入：formula = "Be32"
输出："Be32"
 

提示：

1 <= formula.length <= 1000
formula 由小写英文字母、数字 '(' 和 ')' 组成。
formula 是有效的化学式。
"""

import collections


class Solution:
    def countOfAtoms(self, s: str) -> str:
        stack = [1]
        i = len(s) - 1
        dic = collections.defaultdict(int)
        lower = count = ''
        while i > -1:
            if '0' <= s[i] <= '9':
                count = s[i] + count
            elif 'a' <= s[i] <= 'z':
                lower = s[i] + lower
            elif s[i] == ')':
                stack.append(stack[-1] * int(count or '1'))
                count = ''
            elif s[i] == '(':
                stack.pop()
            elif 'A' <= s[i] <= 'Z':
                dic[s[i] + lower] += stack[-1] * int(count or '1')
                count = ''
                lower = ''
            i -= 1
        ans = ''
        for k, v in sorted(dic.items()):
            if v == 1:
                ans += k
            else:
                ans += k + str(v)
        return ans