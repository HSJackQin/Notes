# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        left_part, right_part = ListNode(0), ListNode(0)
        left, right = left_part, right_part
        cur = head
        while cur:
            if cur.val < x:
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next
            cur = cur.next
        left.next = right_part.next
        right.next = None  # 为什么不加这句就会超出时间限制？？
        return left_part.next