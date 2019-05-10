# Time: O(m*n)
# Space: O(m+n)

'''
这道题是典型的动态规划(Dynamic Programming)问题，可以作为DP思想的
入门问题
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = grid[0]
        for i in range(1, len(grid[0])):
            dp[i] = dp[i] + dp[i-1]
        for j in range(1, len(grid)):
            dp[0] += grid[j][0]
            for h in range(1, len(dp)):
                dp[h] = min(dp[h-1], dp[h]) + grid[j][h]
        return dp[-1]

# 思考空间复杂度为什么可以优化为O(m+n)