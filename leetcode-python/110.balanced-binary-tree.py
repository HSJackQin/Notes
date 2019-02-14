# Time: O(n)
# Space: O(h) h is height of binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(root):
            if root is None:
                return 0
            left_height = getHeight(root.left)
            right_height = getHeight(root.right)
            if left_height < 0 or right_height < 0 or \
                abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return (getHeight(root) >= 0)