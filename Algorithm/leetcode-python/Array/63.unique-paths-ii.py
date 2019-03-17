# Time: O(m*n)
# Space: O(n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        ls = [0]*n
        ls[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[j][i] == 1:
                    ls[j] = 0
                elif j > 0:
                    ls[j] += ls[j-1]
        
        return ls[-1]
        
s = Solution()
nums = [[0,0,0],[0,1,0],[0,0,0]]
s.uniquePathsWithObstacles(nums)