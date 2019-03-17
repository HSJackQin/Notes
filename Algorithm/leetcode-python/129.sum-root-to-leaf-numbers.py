# DFS
# Time: O(n)
# Space: O(h) h is height of binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbersRecu(root, 0)
    
    def sumNumbersRecu(self, root, parent):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return parent + root.val
        parent = (parent + root.val) * 10
        return self.sumNumbersRecu(root.left, parent) + self.sumNumbersRecu(root.right, parent)