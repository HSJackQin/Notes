# Time: O(n)
# Space: O(logn)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head
        # length
        current, length = head, 0
        while current:
            current, length = current.next, length+1
        
        return self.sortedListToBSTRecu(0,length)
    
    def sortedListToBSTRecu(self, start, end):
        if start == end:
            return None
        mid = (start + end) // 2
        left = self.sortedListToBSTRecu(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sortedListToBSTRecu(mid+1, end)
        return current