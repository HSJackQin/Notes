# 链表的基本操作和快慢指针
# Time: O(n)
# Time: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next
        
        slow.next = slow.next.next
        
        return dummy.next