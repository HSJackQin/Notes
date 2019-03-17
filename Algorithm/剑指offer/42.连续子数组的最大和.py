### 42.连续子数组的最大和

### 循环写法
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array is None:
            return 0
        cursum, curmax = 0, float('-inf')
        for num in array:
            if cursum <= 0:
                cursum = num
            else:
                cursum += num
            if cursum > curmax:
                curmax = cursum
        return curmax

### 动态规划写法
