# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = head
        while pre and pre.next:
            cur = pre.next
            while cur and cur.val == pre.val:
                cur = cur.next
            pre.next = cur
            pre = cur
        return head