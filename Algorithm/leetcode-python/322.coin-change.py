# Time: O(n*k) || n is the number of coins, k is the amount of money. 
# Space: O(k) || 需要从头维护k长的数组，每个里面存放当amount为index时的最小找零数

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7ffffff
        cur = [INF]*(amount+1)
        cur[0] = 0
        for i in range(amount+1):
            if cur[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        cur[i+coin] = min(cur[i+coin], cur[i] + 1)
        return cur[amount] if cur[amount] != INF else -1