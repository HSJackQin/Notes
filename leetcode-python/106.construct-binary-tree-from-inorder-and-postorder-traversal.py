# 本题和105题基本一样，就是把参照从前序遍历序列变成了后序遍历序列
# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, inorder, postorder, len(postorder), 0, len(inorder))
    
    def buildTreeRecu(self, lookup, inorder, postorder, post_end, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(postorder[post_end-1])
        i = lookup[postorder[post_end-1]]
        node.left = self.buildTreeRecu(lookup, inorder, postorder, post_end-1-(in_end-i-1), in_start, i)
        node.right = self.buildTreeRecu(lookup, inorder, postorder, post_end-1, i+1, in_end)
        return node