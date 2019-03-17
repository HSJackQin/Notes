'''
头尾相连，顺便算出长度，然后根据k和length递推出需要断开的点的位置即可。
'''

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        if head == None or head.next == None:
            return head
        pre, cur = head, head
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head #连成一个环
        for i in range(length - (k % (length + 1))):
            pre = pre.next
        head = pre.next
        pre.next = None
        return head