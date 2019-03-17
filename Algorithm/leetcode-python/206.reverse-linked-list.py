# Iterative solution

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
方法一：
利用了python多元赋值的特性：等号右边的值在赋值过程中不改变
代码简洁但步易读
'''
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        while head:
            res.next, res.next.next, head = head, res.next, head.next
        return res.next


'''
方法二：
标准的指针解法：
代码过程详细，参考https://blog.csdn.net/songyunli1111/article/details/79416684
'''
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        while head:
            last = pre.next
            pre.next = head
            temp = head
            head = head.next
            temp.next = last
        return pre.next

# Recursive solution
# Time: O(n^2)
# Space: O(n)
'''
时间复杂度垃圾，因为每次递归时都是尾部插入的，需要迭代至找到尾部，
应该还有更好的递归策略。
'''

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        newhead = self.reverseList(head.next)
        cur = newhead
        while cur.next:
            cur = cur.next
        cur.next = head
        head.next = None
        return newhead
            