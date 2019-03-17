# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(len(prices)-1):
            maxprofit = maxprofit + max(0, prices[i+1]-prices[i])
        return maxprofit