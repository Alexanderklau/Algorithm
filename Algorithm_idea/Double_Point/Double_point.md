# 双指针问题

细化一下，一般双指针问题，都可以归类为以下两个大类

1. 快慢指针
2. 左右指针

快慢指针一般解决链表问题比较多

左右指针一般解决数组问题比较多


## 快慢指针

一般用来求链表问题，fast在前，slow在后

### 判断链表是否有环

力扣地址：

https://leetcode-cn.com/problems/linked-list-cycle/

```
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，

可以通过连续跟踪 next 指针再次到达，则链表中存在环。 

为了表示给定链表中的环，

我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 

如果 pos 是 -1，则在该链表中没有环。

注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。
```

解题方法：

这道题其实比较简单，搞清楚环形到底是个啥

首先定义两个参数，一个fast，一个slow

然后开始循环链表，当fast和fast.next都不为空的时候，就不跳出循环

当fast和slow相遇（相等）的时候，则有环形

当fast为null的时候，则没有环形

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
        
```

### 已知有环，找到那个环的起始位置

```
给定一个链表，返回链表开始入环的第一个节点。 

从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。如果链表无环，则返回 null。

为了表示给定链表中的环，

我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。

 如果 pos 是 -1，则在该链表中没有环。
 
 注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。


示例 1：


输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 
提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
 
进阶：是否可以使用 O(1) 空间解决此题？
```


```python
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        k = 0
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                k = 1
                break

        if k == 1:
            slow = head
            
            while slow != fast:
                fast = fast.next
                slow = slow.next
            
            return slow
        else:
            return
```