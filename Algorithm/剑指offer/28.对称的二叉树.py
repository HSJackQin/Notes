### 28.对称的二叉树

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymmetricalRecu(pRoot, pRoot)
    def isSymmetricalRecu(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.isSymmetricalRecu(pRoot1.left, pRoot2.right) and \
                   self.isSymmetricalRecu(pRoot1.right, pRoot2.left)
        if pRoot1.val != pRoot2.val:
            return False