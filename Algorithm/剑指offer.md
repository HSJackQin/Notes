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

> 10.斐波那契数列

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
            mid = (left + right) // 2
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
**之前一直死循环，是因为一个赋值的等号写成了'=='，编程基本语法上一定要仔细**

---

> 12.矩阵中的路径

1、二维矩阵常常采用数组形式存储，因此其元素对应的一维数组的下标转换不要出错

2、矩阵中的路线常可以利用回溯法求解

本题从初始点开始（初始点从全矩阵开始扫描），采用回溯法依次探索其上下左右是否满足条件，从而判断出
是否存在完整的匹配路线。

```python
class Solution:
    def hasPath(self, matrix, rows, cols, path): # path代表路径长度
        if matrix == [] or rows <= 0 or cols <= 0 or not path:
            return False
        lengthPath = 0            #表示此时匹配的是字符串的第几个元素，和下面的visited一样，都是要维护的全局变量
        visited = [0]*(rows*cols) #visited是长度为总元素个数的一维数组，存放表示元素是否已经被访问
        for row in range(rows):
            for col in range(cols): #这里遍历方式初始化起点
                if self.hasPathRecu(matrix, rows, cols, row, col, path, lengthPath, visited): #递归辅助函数，也是方法实现的主体
                    return True
        return False #默认返回False
    
    def hasPathRecu(self, matrix, rows, cols, row, col, path, lengthPath, visited):
        if lengthPath == len(path): #这里表示如果匹配到最后一个元素都是对的，以至下标出界，则返回True，是递归的终止条件
            return True
        hasFound = False #这里定义其为默认的False，为了后面表示方便
        if row >= 0 and col >= 0 and row < rows and col < cols and path[lengthPath] == matrix[row*cols + col] and not visited[row][col]:
            visited[row*cols + col] = 1
            lengthPath += 1
            hasFound = self.hasPathRecu(matrix, rows, cols, row-1, col, path, lengthPath, visited) \ #这里的设计保证了如果返回是False，就将全局变量lengthPath和visited复原
                    or self.hasPathRecu(matrix, rows, cols, row, col-1, path, lengthPath, visited) \
                    or self.hasPathRecu(matrix, rows, cols, row+1, col, path, lengthPath, visited) \
                    or self.hasPathRecu(matrix, rows, cols, row, col+1, path, lengthPath, visited)
            if not hasFound: #这里决定了上面的调用在返回False的时候是可以把全局变量lengthPath和visited复原的
                visited[row*cols + col] = 0
                lengthPath -= 1
        return hasFound
```
---

> 14.剪绳子

本题可以使用（1）动态规划；（2）贪心算法；求解。

（1）动态规划：注意自顶向下设计，自底向上实施

（2）贪心算法：注意背后的数学支撑

```python
#贪心算法
class Solution:
    def maxAfterCut(self, length): #length是绳子长度
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        #尽可能去剪长度为3的段
        timeOf3 = length // 3
        if length - 3*timeOf3 == 1:
            timeOf3 -= 1
        timeOf2 = (length - 3*timeOf3) // 2
        return pow(3,timeOf3)*(pow(2,timeOf2))
```

```python
#动态规划
class Solution:
    def maxAfterCut(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        products = [0]*(length+1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4,length+1,1):
            for j in range(1,(i//2)+1,1):
                products[i] = max(products[i], products[j]*products[i-j])
        return products[length]
```

---

> 15.二进制中1的个数

```python
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count
```

---

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

> 19.正则表达式匹配



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

注意输出的格式要求，以及python处理字符串的方法。

```python
class Solution:
    def Permutation(self, ss):
        if not ss: #边界条件
            return []
        if len(ss) == 1: #递归的基本情况
            return list(ss)
        res = [] #定义存放结果的空列表
        pStr = list(ss) #把传入的字符串转化为列表，方便操作
        pStr.sort() #对这个list进行排序
        for i in xrange(len(ss)):
            if i > 0 and pStr[i] == pStr[i-1]: #这里考虑到了字符串中重复字符的情况
                # 每当扫描到和上一个字符相重复的字符，就直接跳过，因为这些情况上一次已经考虑过了
                # 当然，这要在这个数组已经排过序的情况下
                continue
            temp = self.Permutation(''.join(pStr[:i]) + ''.join(pStr[i+1:]))
                # 这里是把切片的列表转换回字符串
            for j in temp:
                res.append(pStr[i] + j)
        return res
```

---

> 40.最小的k个数

partition思想实现

```python
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput) or k <= 0:
            return []
        tinput = self.quick_sort(tinput)
        return tinput[:k]
    def quick_sort(self, tinput):
        if not tinput:
            return []
        pivot = tinput[0]
        left = self.quick_sort([x for x in tinput[1:] if x < pivot])
        right = self.quick_sort([x for x in tinput[1:] if x >= pivot])
        return left + [pivot] + right
```

---

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

> 43.1~n整数中1出现的次数

---

> 44.数字序列中某一位的数字

---

> 45.把数组排成最小的数

自定义大小规则 + 冒泡排序

```python
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None:
            return 
        str_num = [str(i) for i in numbers]
        for i in xrange(len(numbers)-1,0,-1):
            for j in xrange(i):
                if str_num[j] + str_num[j+1] > str_num[j+1]+str_num[j]:
                    str_num[j], str_num[j+1] = str_num[j+1], str_num[j]
        return ''.join(str_num)
```

---

> 47.礼物的最大价值

（1）第一步优化：基于循环而不是递归从而避免大量计算

```python
def get_max_value1(matrix)
```

（2）第二步优化：由维护二维数组变为维护一维数组

```python
def get_max_value2(matrix):
    if not isinstance(matrix,list) or len(matrix) == 0 or not isinstance(matrix[0],list) \
        or len(matrix[0]) == 0:
        return
    num_row = len(matrix)
    num_col = len(matrix[0])
    for row in matrix:
        if not isinstance(row,list) or len(row) != num_col:
            return
    max_value = [0]*num_col
    for i in range(num_row):
        for j in range(num_col):
            up, left = 0, 0
            if i > 0:
                up = max_value[j]
            if j > 0:
                left = max_value[j-1]
            max_value[j] = matrix[i][j] + max(up, left)
    return max_value[-1]
```

---

> Leetcode 62/63 不同路径

考察路径中加入障碍的情况

---

> 48.最长的不含重复字符的子字符串

```python
def longest_substring_without_duplication(string):
    if not isinstance(string,str) or len(string) == 0:
        return
    
    cur_length = 0
    max_length = 0
    position = [-1]*26 #用来记录每个字母上次出现的位置

    for i, ch in enumerate(string):
        if ord(ch) < ord("a") or ord(ch) > ord("z"):
            return
        index_of_ch = ord(ch) - a #用每个字母独特的位置表示该字母
        if position[i] == -1 or (i - position[index_of_ch]) > max_length:
            cur_length += 1
        else:
            cur_length = i - position(index_of_ch)
        if cur_length > max_length:
            max_length = cur_length
        position(index_of_ch) = i #将当前的字母出现位置记录下来

    return max_length
```

---

> Leetcode 131 分割回文串

---

> Leetcode 132 分割回文串II

---

> 50.第一个只出现一次的字符

（1）字符串中第一个只出现一次的字符

建立哈希表（字典）记录各字符出现的次数，比较简单。

（2）字符流中第一个只出现一次的字符

```python

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

> 53.在排序数组中查找数字

（1）数字在排序数组中出现的次数

```python

```

---

> 54.二叉搜索树的第K大节点

考察二叉树的中序遍历

```python
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or not k:
            return 
        res = []
        def traverse(node):
            if len(res) >= k or not node:
                return
            traverse(node.left)
            res.append(node)
            traverse(node.right)
        traverse(pRoot)
        if len(res) < k:
            return
        return res[k-1]
```

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

```python {.line-numbers}
Time: O(n)
Space: O(1)

def last_remain(n,m):
    if n < 1 or m < 1:
        return
    last = 0
    for i in range(1,n):
        last = (last + m) % (i + 1)
    return last
```

---

> 68.树中两个节点的最低公共祖先

（1）二叉搜索树的最低（深）公共祖先(Leetcode No.235)

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            root = root.left if root.val >= s else root.right
        return root
```

（2）二叉树的最低公共祖先(Leetcode No.236)

这是一个回溯法思想可以解决的问题。回溯问题一般可以利用递归的方式实现。

```python {.line-numbers}
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left, right = [self.lowestCommonAncestor(root, p, q) for root in (root.left, root.right)]
        return root if left and right else left or right
```
