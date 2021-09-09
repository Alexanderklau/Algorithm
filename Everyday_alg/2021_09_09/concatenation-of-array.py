# coding: utf-8

__author__ = 'Yemilice_lau'

"""
给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：

ans[i] == nums[i]
ans[i + n] == nums[i]
具体而言，ans 由两个 nums 数组 串联 形成。

返回数组 ans 。

 

示例 1：

输入：nums = [1,2,1]
输出：[1,2,1,1,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
示例 2：

输入：nums = [1,3,2,1]
输出：[1,3,2,1,1,3,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        srt, res, n, wl = 0, [], len(words), 0  # 指针srt指向最早的尚未处理下标，wl表示待处理单词的总长度
        for i, v in enumerate(words):  # 遍历并记录每个单词
            nwl, wn = len(v), i - srt  # 本单词长度nwl，前面累计未处理单词总数wn
            if nwl + wn + wl <= maxWidth: wl += nwl  # 本单词可以被放入该行内，记录暂不处理
            else:  # 本单词无法放入该行，必须处理后换行
                if wn==1: res.append(words[srt].ljust(maxWidth))  # 待处理单词后跟足够的空格
                else:
                    sep_len = (maxWidth - wl) // (wn - 1)  # 平均分配空格
                    for j in range(srt, srt + (maxWidth - wl) % (wn - 1)): words[j] += ' '  # 处理多余空格
                    res.append((' '*sep_len).join(words[srt:i]))  # 格式化处理字符串
                wl, srt = nwl, i  # 换行后作为下一行的第一个单词
        if srt<n: res.append((' '.join(words[srt:])).ljust(maxWidth))  # 剩余所有单词用空格隔开，并左对齐填充
        return res