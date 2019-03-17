# Time: O(log_10^{n})
# Space: O(1)

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i, j, result= 0, len(str(x))-1, True
        while i < j and result == True:
            if str(x)[i] == str(x)[j]:
                i += 1
                j -= 1
            else:
                result = False
        
        return result