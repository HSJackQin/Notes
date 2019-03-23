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

结合书上的示例二叉树进行分析，可知：

共分为3种情况：

（1）该节点有右子树，那么下一个节点就是右子树的最左叶节点

（2）该节点没有右子树，且是父节点的左孩子，那么父节点就是下一个节点

（3）该节点没右子树，且是父节点的右孩子，这时需要一直向上寻找，直到找到一个是父节点的左孩子的节点，该节点的父节点即为所求；否则，没有下一个节点。

```python
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None
        pNext = None # 提前设好，这样下面的条件都不满足时可以直接返回pNext
        if pNode.right:
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left
            pNext = pRight
        else:
            if pNode.next:
                pCur = pNode # 这一步想清楚
                while pCur.next:
                    if pCur.next.left == pCur:
                        pNext = pCur.next
                        break # 注意循环退出，防止死循环
                    pCur = pCur.next
        return pNext
```

---

> 9.用两个栈实现队列

这题考察栈和队列的基本操作

```python
class Solution:
    stack1, stack2 = [], [] #在类中定义的全局变量，函数中引用时要加self
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2: # while完了之后要多一步判断是否stack2非空
                return self.stack2.pop()
            else:
                return
```

---

> 10.斐波那契额数列

应避免用递归，采用自底向上的方法。

```python
class Solution:
    def Fibonacci(self, n):
        res = [0, 1]
        if n < 2:
            return res[n]
        FibOne = 0
        FibTwo = 1
        Fib = 0
        for i in xrange(2, n+1):
            Fib = FibOne + FibTwo
            FibOne = FibTwo
            FibTwo = Fib
        return Fib
```

---

> 11.旋转数组的最小数字

二分查找的变种，注意特殊情况的考虑(1)数组未旋转(2)前中后三值相等，具体分析见书。

```python
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray == []:
            return 0
        left, right, mid = 0, len(rotateArray)-1, 0
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid == (left + right) // 2
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                return self.InOrder(rotateArray, left, right)
            if rotateArray[left] <= rotateArray[mid]:
                left = mid
            elif rotateArray[right] >= rotateArray[mid]:
                right = mid
        return rotateArray[mid]
    
    def InOrder(self, rotateArray, left, right):
        res = rotateArray[left]
        for i in xrange(left+1,right+1):
            if res > rotateArray[i]:
                res = rotateArray[i]
        return res
```
**代码执行有误，死循环**

---

> 12.矩阵中的路径

> 18.删除链表的节点

- (1)删除链表中指定的节点

由于单链表中不含有指向前一个节点的指针，所以常规删除操作需要从头遍历，但本题要求
时间复杂度O(1)，因此我们采用将要删除节点的下一个节点的值赋给待删除节点，然后删除该节点的下一个节点；
但如果待删除节点位于尾部，则只能采取从头遍历的方法删除。

```python
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
class Solution:
    def DeleteNode(self, pHead, pDelete):
        if pHead is None or pDelete is None:
            return 
        if pDelete.next: #一般情况，当要删除的节点不是尾节点时
            pDelete.val = pDelete.next.val
            pDelete.next = pDelete.next.next
        elif pHead is pDelete: #当链表只有一个节点时
            pHead = None
        else: #链表有多个节点，且要删除的节点是尾节点时
            pNode = pHead
            while pNode.next != pDelete:
                pNode = pNode.next
            pNode.next = None
        return pHead
```

- (2)删除链表中重复的节点

```python
class Solution:
    def DeleteDuplication(self, pHead):
        if pHead is None:
            return
        pPre, pNode = None, pHead
        toBeDeleted = False
        while pNode:
            if pNode.next and pNode.val == pNode.next.val:
                toBeDeleted = True
            if not toBeDeleted:
                pPre = pNode
                pNode = pNode.next
            else:
                value = pNode.val
                pDelete = pNode
                while pDelete and pDelete.val == value:
                    pDelete = pDelete.next
                if pPre is None:
                    pHead = pDelete
                else:
                    pPre.next = pDelete
                pNode = pDelete
        return pHead
```
**报错，待纠正**

> 21.调整数组顺序使奇数位于偶数前面

> 22.链表中倒数第K个节点

这里要注意特殊用例的情况，即保证每一个节点引用都是合法的。

```python
class Solution:
    def FindKthToTail(self, head, k):
        if head is None or k == 0:
            return None
        pBehind, pAhead = head, head
        for i in xrange(k-1):
            if pAhead.next:
                pAhead = pAhead.next
            else:
                return None
        while pAhead.next:
            pAhead = pAhead.next
            pBehind = pBehind.next
        return pBehind
```

---

> 23.链表中环的入口节点



> 24.反转链表



> 25.合并两个排序的链表

> 26.树的子结构

> 27.二叉树的镜像

> 28.对称的二叉树

> 32.从上到下打印二叉树

考察树的层次遍历。

树的层次遍历本质上就是图的广度优先搜索BFS，是用队列实现的。

```python
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot is None:
            return []
        stack = []
        res = []
        cur = []
        stack.append(pRoot)
        toBePrinted = 1
        nextLevel = 0
        while stack:
            pNode = stack.pop(0)
            cur.append(pNode.val)
            toBePrinted -= 1
            if pNode.left:
                stack.append(pNode.left)
                nextLevel += 1
            if pNode.right:
                stack.append(pNode.right)
                nextLevel += 1
            if toBePrinted == 0:
                res.append(cur)
                toBePrinted = nextLevel
                nextLevel = 0
                cur = []
        return res
```

---

> 33.二叉搜索树的后序遍历序列

> 34.二叉树中和为某一值的路径

> 36.二叉搜索树与双向链表

> 37.序列化二叉树

> 42.连续子数组的最大和



> 52.两个链表的第一个公共节点

思路简单，考察链表的编程能力

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None: #判断特殊用例
            return
        pNode1, pNode2 = pHead1, pHead2 #进行第一次遍历，得到两链表的长度
        len1, len2 = 1, 1
        while pNode1.next is not None:
            pNode1 = pNode1.next
            len1 += 1
        while pNode2.next is not None:
            pNode2 = pNode2.next
            len2 += 1
        pCur1, pCur2 = pHead1, pHead2 #进行第二次遍历，寻找公共节点
        if len1 > len2:
            for i in range(len1-len2):
                pCur1 = pCur1.next
        else:
            for j in range(len2-len1):
                pCur2 = pCur2.next
        while pCur1 and pCur2 and pCur1 != pCur2:
            pCur1 = pCur1.next
            pCur2 = pCur2.next
        if pCur1 is not None:
            return pCur1
        return None
```

            

> 54.二叉搜索树的第K大节点

> 55.二叉树的深度

考察二叉树的遍历

```python
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
```

> 55(2).平衡二叉树

只进行一次遍历，判断二叉树是不是平衡二叉树

要想只遍历一次，就要自底向上维护一个判断是否平衡的变量flag，类似二叉树的后序遍历。

```python
class Solution:
    flag = True
    def IsBalanced_Solution(self, pRoot):
        self.Depth(pRoot)
        return self.flag
    def Depth(self, pRoot):
        if pRoot is None:
            return 0
        left = self.Depth(pRoot.left)
        right = self.Depth(pRoot.right)
        if abs(left - right) > 1:
            self.flag = False
        return max(left, right) + 1
```

---

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

> 68.树中两个节点的最低公共祖先

