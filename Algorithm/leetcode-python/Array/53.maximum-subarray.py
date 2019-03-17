# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum, maxvalue = 0, nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxvalue:
                maxvalue = sum
            if sum < 0:
                sum = 0
        return maxvalue

# 参考：https://my.oschina.net/itblog/blog/267860
#      https://blog.csdn.net/abnerwang2014/article/details/36027747

# 分治法：效率不如上面的算法
# Time: O(nlogn)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSubSum(nums, 0, len(nums)-1)
    
    def maxSubSum(self, nums, left, right):
        if left == right:
            return nums[left]
        
        center = (left + right)//2
        leftmax = self.maxSubSum(nums, left, center)
        rightmax = self.maxSubSum(nums, center+1, right)
        
        maxleftborder = nums[center]
        leftsum = nums[center]
        for i in range(center-1, left-1, -1):
            leftsum = leftsum + nums[i]
            maxleftborder = max(maxleftborder, leftsum)
        
        maxrightborder = nums[center+1]
        rightsum = nums[center+1]
        for i in range(center+2, right+1, 1):
            rightsum = rightsum + nums[i]
            maxrightborder = max(maxrightborder, rightsum)
        
        return max(leftmax, rightmax, maxleftborder+maxrightborder)