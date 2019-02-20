'''
和上一题(141.linked-list-cycle)相比，本题
依旧是快慢指针相遇问题，只不过需要在相遇之后，
让fast指针回到原点，继续走直到两指针第二次相遇，
相遇点一定是入环点！
'''

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None