# Time: O(n)
# Space: O(h) h is height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive solution

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetricRecu(root.left, root.right)
    
    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is not None and right is not None:
            return left.val == right.val and self.isSymmetricRecu(left.left, right.right) \
                and self.isSymmetricRecu(left.right, right.left)
        return False

# iterative solution

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        while stack:
            p, q = stack.pop(), stack.pop()
            if p is None and q is None:
                continue
            if p is None or q is None or p.val != q.val:
                return False
            else:
                stack.append(p.left)
                stack.append(q.right)
                
                stack.append(p.right)
                stack.append(q.left)
        
        return True