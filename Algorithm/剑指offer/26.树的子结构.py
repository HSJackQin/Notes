### 26.树的子结构

##### 本解答其实是leetcode第572.另一个树的子树，和剑指offer上面的有一点小小的不同，只在isSame函数的if判断上有不同
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        result = False
        if s is not None and t is not None:
            if s.val == t.val:
                result = self.isSame(s,t)
            if not result:
                result = self.isSubtree(s.left, t)
            if not result:
                result = self.isSubtree(s.right, t)
        return result
    
    def isSame(self, big, small):
        if big is None and small is None:
            return True
        elif big is not None and small is not None:
            if big.val != small.val:
                return False
            else:
                return self.isSame(big.left, small.left) and self.isSame(big.right, small.right)
        else:
            return False