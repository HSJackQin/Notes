'''
思路同96题，在96的基础上递归求出所有的树
仍然是让每个数轮流做根节点，分别递归求其左右子树，
这里递归的将左右子树的所有情况列举出来，符合
递归的定义。然后将左右子树和根节点i合并
'''

# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(4^n / n^(3/2)) ~= Catalan numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateTreesRecu(1, n)
    
    def generateTreesRecu(self, left, right):
        res = []
        if left > right:
            res.append(None)
        for i in range(left, right+1):
            left_part = self.generateTreesRecu(left, i-1)
            right_part = self.generateTreesRecu(i+1, right)
            for m in left_part:
                for j in right_part:
                    node = TreeNode(i)
                    node.left = m
                    node.right = j
                    res.append(node)
        return res