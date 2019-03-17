class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        value = 0
        
        for i in range(len(s)):
            if i and dic[s[i]] > dic[s[i-1]]:
                value += dic[s[i]] - 2 * dic[s[i-1]]
            else:
                value += dic[s[i]]
        
        return value