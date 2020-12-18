# coding: utf-8

__author__ = 'Yemilice_lau'

# Fibonacci数列

# 老问题了

import functools


@functools.lru_cache
def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

recur_fibo(37)


