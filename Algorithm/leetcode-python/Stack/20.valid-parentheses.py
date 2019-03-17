# Time: O(n)
# Space: O(n)

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapping:
                last = stack.pop() if stack else '#'
                if last != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack