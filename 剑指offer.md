# 剑指offer题解(Python)

> 3.数组中重复的数字

（1）原地修改数组

```python
Time: O(n)
Space: O(1)
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        length = len(numbers)
        if length <= 0:
            return False
        for i in xrange(length):
            while i != numbers[i]:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
        return False
```

（2）不修改数组

---

> 4.二维数组中的查找

```python
class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array)
        cols = len(array[0])
        if array is not None and rows > 0 and cols > 0:
            row = 0
            col = cols - 1
            while row < rows and col >= 0:
                if array[row][col] == target:
                    return True
                else:
                    if array[row][col] < target:
                        row += 1
                    else:
                        col -= 1
        return False
```

---

> 6.从尾到头打印链表

（1）显示利用栈，鲁棒性比直接递归要好
```python
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        stack, res = [], []
        pNode = listNode
        while pNode is not None:
            stack.append(pNode.val)
            pNode = pNode.next
        while stack:
            res.append(stack.pop())
        return res
```

---

> 7.重建二叉树
通过二叉树的前序和中序序列，还原二叉树。采用递归，注意如果追求更少的时间代价，应该将列表的切片操作替换成索引，以下给出的切片操作写起来更直观。
```python
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if pre == [] or tin == []:
            return None
        node = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        node.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        node.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return node
```

---
> 8.二叉树的下一个节点

> 62.圆圈中最后剩下的数字

约瑟夫环问题，可以利用环形链表模拟圆圈来解决，也可以由数学推导内在规律。

（1）环形链表解法

```python
Time: O(mn)
Space: O(n)

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def last_remain(n, m):
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
        return
    
    next = None
    for i in range(n-1, -1, -1):    #构造循环链表
        node = Node(value=i, next=next)
        if i == n-1:
            last = node
        next = node
    head = next    #保证链表循环
    last.next = head
    pre = last
    p = head
    while id(p) != id(p.next):    #逐个删除
        for j in range(m-1):
            pre = p
            p = p.next
        pre.next = p.next
        p = pre.next
    return p.value    #返回剩下的一个

if __name__ = "__main__":
    print(last_remain(5,3))
```

（2）数学方法求解


---



