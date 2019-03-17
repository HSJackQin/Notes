'''
指针的运用：
本题中right指针的运用值得思考
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        last = pre
        if head is None:
            return None
        for i in range(m - 1):
            temp = last.next
            last.next = head
            head = head.next
            last.next.next = temp
            last = last.next
        right = head
        for j in range(n - m + 1):
            temp = last.next
            last.next = head
            head = head.next
            last.next.next = temp    
        right.next = head

        return pre.next