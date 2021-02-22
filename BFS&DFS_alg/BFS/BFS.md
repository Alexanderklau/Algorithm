# BFS（广度优先算法）笔记

## 什么是BFS算法

广度优先算法的逻辑其实很简单，举个例子，走迷宫的时候，广度优先算法会将所有的迷宫岔路都记下来，选择一个进入，然后记录路径的情况，然后再返回进入另外一个岔路，并且重复这样的操作。

用一个树来形容这个BFS算法

```
    A
   / \
  B   C
 /     \
D       E
         \
          F
```

如果用BFS算法，会从左到右遍历节点

遍历的过程是  A B D C E F


举个简单的例子

我们模拟一个走格子的游戏，现在要从1出发，移动到9

```
1 2 3
4 5 6
7 8 9
```

用BFS算法分析

第一步，从1出发，记录所有岔路口

```
0 1 0 
1 0 0
0 0 0
```

第二步，回到最上面的1处，继续记录能走的岔路口

```
0 1 2
1 2 0
2 0 0
```

第三步，以此类推

```
0 1 2
1 2 3
2 3 0
```

第四步

```
0 1 2
1 2 3
2 3 4
```
这就得出了移动到9的所有路径。

可以看出，广度优先算法主要是由近到远的方式来搜索，会先访问最近的点，然后一层层去寻找问题的答案。

用代码表示这个逻辑

```python
from collections import deque
def bsf_graph(root):
    if not root:
        return
    # queue和seen为一对好基友，同时出现
    queue = deque([root])
    # seen避免图遍历过程中重复访问的情况，导致无法跳出循环
    seen = set([root])
    while queue:
        head = queue.popleft()
        # do somethings with the head node
        # 将head的邻居都添加进来
        for neighbor in head.neighbors:
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)
    return xxx
```

此处是BFS的基础模版，其实网上的大多数都说的不是很清楚

