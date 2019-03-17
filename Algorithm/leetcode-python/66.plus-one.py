# Time: O(n) n is the length of the list.
# Space: O(1)

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        cur = len(digits) - 1
        while cur >= 0:
            if digits[cur] == 9:
                digits[cur] = 0
                cur -= 1
            else:
                digits[cur] += 1
                break
        if cur < 0:
            return [1] + digits
        else:
            return digits