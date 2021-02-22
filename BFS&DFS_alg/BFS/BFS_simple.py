# coding: utf-8

__author__ = "lau.wenbo"

"""
简单的终点逻辑

a - b - d - f
  \ | / |
    c   e

"""

from collections import deque
graph={
	'a':['b','c'],
	'b':['a','c','d'],
	'c':['a','b','d','e'],
	'd':['b','c','e','f'],
	'e':['c','d'],
	'f':['d']
}

def BFS(graph, s):
	queue = []
	queue.append(s)
	seen = set()
	seen.add(s)
	while(len(queue) > 0):
		v = queue.pop(0)
		nodes = graph[v]
		for w in nodes:
			if w not in seen:
				queue.append(w)
				seen.add(w)
		print(v)

BFS(graph, 'a')