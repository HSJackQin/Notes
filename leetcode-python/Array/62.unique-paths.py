# Time: 
# Space: 

# Solution1
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(self.factorial(m+n-2)/((self.factorial(m-1))*(self.factorial(n-1))))
    
    def factorial(self, num):
        result = 1
        while num > 1:
            result = num*result
            num -= 1
        return result

# Solution2