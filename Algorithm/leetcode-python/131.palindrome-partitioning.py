# Time: O(2^n)
# Space: O(n)
# DFS + 回文检查

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.partitionRecu(result, [], s, 0)
        return result
    
    def partitionRecu(self, result, cur, s, i):
        if len(s) == i:
            result.append(list(cur))
        else:
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    cur.append(s[i:j+1])
                    self.partitionRecu(result, cur, s, j+1)
                    cur.pop()
                    
    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-(i+1)]:
                return False
        return True