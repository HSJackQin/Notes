# Solution 1
# 这种方法最容易想到，但其中涉及到的切片操作也需要时间复杂度，因此还有改进的空间（把切片换成索引）

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            mid=len(nums)//2
            tn=TreeNode(nums[mid])
            nums1=nums[0:mid]
            nums2=nums[mid+1:len(nums)]
            tn.left=self.sortedArrayToBST(nums1)
            tn.right=self.sortedArrayToBST(nums2)
        return tn

# Solution 2
# 这种方法是上一种方法的改进，将切片操作改为索引
# Time: O(n)
# Space: O(logn)

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.iterator = iter(nums)
        return self.sortedArrayToBSTRecu(0, len(nums))
    
    def sortedArrayToBSTRecu(self, start, end):
        if start == end:
            return None
        i = (start + end) // 2
        left = self.sortedArrayToBSTRecu(start, i)
        current = TreeNode(next(self.iterator))
        current.left = left
        current.right = self.sortedArrayToBSTRecu(i+1, end)
        return current