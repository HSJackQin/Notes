# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                if prices[i] - minprice > maxprofit:
                    maxprofit = prices[i] - minprice
        return maxprofit