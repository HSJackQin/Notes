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

- (2)删除链表中重复的节点（是指重复的都删去，而不是留一份）

```python
class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pPre, pNode = None, pHead
        while pNode:
            toBeDeleted = False
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

---

> 21.调整数组顺序使奇数位于偶数前面

> 22.链表中倒数第K个节点

定义快慢两个指针，快指针先走k步，然后快慢指针一起走，快指针到头时慢指针的位置就是
倒数第K个节点。这里要注意特殊用例的情况，即保证每一个节点引用都是合法的。

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

首先通过快慢指针判断是否有环，如果有，令fast指针回到原地，
slow和fast同速度，则相遇点就是环的入口节点。

```python
class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow, fast = pHead, pHead
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = pHead
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
```

---

> 24.反转链表

本题也可以使用递归和迭代两种思路求解，递归较容易，迭代考验操作。
想明白三指针（其实就是两个指针）的移动顺序，注意列表的暂存和续接。

（1）两指针

```python
class Solution:
    def ReverseList(self, pHead):
        pReverse = None
        pPre, pNode = None, pHead #定义两指针
        while pNode:
            pNext = pNode.next #这里要把pNode之后的链表暂存
            if not pNode.next:
                pReverse = pNode
            pNode.next = pPre #注意这里的顺序！！
            pPre = pNode
            pNode = pNext
        return pReverse
```
（2）递归

核心思想是从后往前，想明白每一步，得到部分反转的链表后，要遍历得到其尾节点。

```python
class Solution:
    def ReverseList(self, pHead):
        if not pHead:
            return None
        if not pHead.next:
            return pHead
        pReverse = self.ReverseList(pHead.next)
        cur = pReverse
        while cur.next:
            cur = cur.next
        cur.next = pHead
        pHead.next = None
        return pReverse
```

---

> 25.合并两个排序的链表

本题可以分析出两种解法，首先将合并过程从第一步开始考虑，第一步结束后的操作其实是
重复的，因此可以写成递归的形式。也可以直接利用指针的移动解题，更考验对链表和指针的操作。

（1）递归

```python
class Solution:
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        mergeNode = ListNode(0) #定义新的节点储存结果
        if pHead1.val < pHead2.val:
            mergeNode = pHead1
            mergeNode.next = self.Merge(pHead1.next, pHead2)
        else:
            mergeNode = pHead2
            mergeNode.next = self.Merge(pHead1, pHead2.next)
        return mergeNode
```

（2）常规写法

```python
class Solution:
    def Merge(self, pHead1, pHead2):
        mergeNode, pNode1, pNode2 = ListNode(0), pHead1, pHead2
        mergeCur = mergeNode
        while pNode1 and pNode2:
            while pNode1 and pNode1.val < pNode2.val:
                mergeCur.next = pNode1 #这里需要注意不能用mergeCur = pNode1，而要加next，保证mergeNode节点不是空的！
                pNode1 = pNode1.next
                mergeCur = mergeCur.next
            if pNode1:
                while pNode2 and pNode1.val >= pNode2.val:
                    mergeCur.next = pNode2
                    pNode2 = pNode2.next
                    mergeCur = mergeCur.next
        while pNode1:
            mergeCur.next = pNode1
            pNode1 = pNode1.next
            mergeCur = mergeCur.next
        while pNode2:
            mergeCur.next = pNode2
            pNode2 = pNode2.next
            mergeCur = mergeCur.next
        return mergeNode.next
```

---

> 26.树的子结构

本题不难，想清楚过程就好，方法是递归，注意数据类型如果是小数，为了
确保没问题，最后定义在一定误差范围内相等的函数作为相等的判断。

```python
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        if pRoot1 is None or pRoot2 is None:
            return False
        if self.Equal(pRoot1.val, pRoot2.val):
            res = self.IsSame(pRoot1, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.right, pRoot2)
        return res
    def IsSame(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if self.Equal(pRoot1.val, pRoot2.val):
            return self.IsSame(pRoot1.left, pRoot2.left) and \
                   self.IsSame(pRoot1.right, pRoot2.right)
        else:
            return False
    def Equal(self, num1, num2):
        if num1 - num2 > -0.0000001 and num1 - num2 < 0.0000001:
            return True
        else:
            return False
```

---

> 27.二叉树的镜像

递归解法

```python
class Solution:
    def Mirror(self, pRoot):
        if pRoot is None:
            return None
        if pRoot.left is not None or pRoot.right is not None:
            pRoot.left, pRoot.right = pRoot.right, pRoot.left
            pRoot.left = self.Mirror(pRoot.left)
            pRoot.right = self.Mirror(pRoot.right)
        return pRoot
```

---

> 28.对称的二叉树

可以转化为两棵树是不是互为镜像，递归地去比就好

```python
class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymmetricalRecu(pRoot, pRoot)
    def isSymmetricalRecu(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.isSymmetricalRecu(pRoot1.left, pRoot2.right) and \
                   self.isSymmetricalRecu(pRoot1.right, pRoot2.left)
        if pRoot1.val != pRoot2.val:
            return False
```

---

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

剑指offer的用例是不全的，[1,2,7,4,6,5,3]是不对的，但可以通过newcoder的测试！

```python
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        root = sequence[-1]
        length = len(sequence)
        for i in xrange(length):
            if sequence[i] > root:
                break
        for j in xrange(i, length):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if length - 2 > i:
            right = self.VerifySquenceOfBST(sequence[i:length-1])
        return left and right
```

---

> 34.二叉树中和为某一值的路径

递归，前序遍历

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, root, expectNumber):
        if not root or root.val > expectNumber:
            return []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        else:
            expectNumber -= root.val
            left = self.FindPath(root.left, expectNumber)
            right = self.FindPath(root.right, expectNumber)
            result = [[root.val]+i for i in left]
            for j in right:
                result += [[root.val]+j]
            return result
```

---

> 35.复杂链表的复制

```python
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def Clone(self, pHead):

```

> 36.二叉搜索树与双向链表

本题解法：中序遍历+递归，注意二叉搜索树和双向链表的关系（每个节点都是含有两个指针，可以相互转化）

```python
class Solution:
    def Convert(self, pRootofTree):
        if pRootofTree is None:
            return None
        if not pRootofTree.left and not pRootofTree.right:
            return pRootofTree
        
        self.Convert(pRootofTree.left)
        left = pRootofTree.left
        if left:
            while left.right:
                left = left.right
            left.right = pRootofTree
            pRootofTree.left = left
        
        self.Convert(pRootofTree.right)
        right = pRootofTree.right
        if right:
            while right.left:
                right = right.left
            pRootofTree.right = right
            right.left = pRootofTree
        if pRootofTree.left:
            pHead = pRootofTree.left
            while pHead.left:
                pHead = pHead.left
            pRootofTree = pHead
        return pRootofTree
```

> 37.序列化二叉树

通过带null的前序遍历序列，可以唯一确定一棵二叉树？

这里通过前序遍历还原树，主要是要清楚前序遍历需要栈，而递归正好是一个隐式栈结构，
类似的思想还有34题

```python
class Solution:
    def __init__(self):
        self.flag = -1  #初始化一个flag对象，并在全局进行计数更新
    def Serialize(self, root):
        res = []  #这里要返回一个字符串，不能是列表的形式！
        if not root:
            res.append('null')
            return res
        res.append(root.val)
        res += self.Serialize(root.left)
        res += self.Serialize(root.right)
        return res
    
    def Serialize(self, root):
        if not root:
            return '#,'
        return str(root.val)+','+self.Serialize(root.left)+self.Serialize(root.right)

    def Deserialize(self, s):
        self.flag += 1
        l = s.split(',')
        if self.flag >= len(l):
            return None
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
```

> 38.字符串的排列

> 42.连续子数组的最大和

从头开始遍历，并把当前的最大值暂存起来，这种思路和利用循环实现的动态规划是一样的

```python
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == []:
            return 0
        curSum = 0
        curMax = -float('inf')
        i = 0
        while i < len(array):
            curSum += array[i]
            if curSum > curMax:
                curMax = curSum
            if curSum < 0:
                curSum = 0
            i += 1
        return curMax
```

---

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

---

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

