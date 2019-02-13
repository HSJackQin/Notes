# Time: O(n)
# Space: O(h)
# DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))
    
    def isValidBSTRecu(self, root, low, high):
        if root is None:
            return True
        return root.val > low and root.val < high and \
            self.isValidBSTRecu(root.left, low, root.val) and \
            self.isValidBSTRecu(root.right, root.val, high)