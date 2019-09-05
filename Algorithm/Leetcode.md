# LeetCode题解（Python）

## 热题 HOT 100

> 15.三数之和

排序，去重

```python
class Solution:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0 #排序
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i-1]:
                j, k = i+1, len(nums)-1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j+1, k-1
                        # 去重
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
            i += 1
        return result
```

> 5.最长回文子串

动态规划

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[0]*length for _ in range(length)]
        if length == 0 or length == 1:
            return s
        start = 0
        maxLen = 1
        for i in range(length):
            dp[i][i] = 1
            if i + 1 < length and s[i] == s[i+1]:
                dp[i][i+1] = 1
                start = i
                maxLen = 2
        # 至此，找到了所有长度为2的回文串，接下来递推长度为3的

        for l in range(3,length + 1):
            for i in range(0,length-l+1):
                j = i + l - 1
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    start = i
                    maxLen = l
        
        return s[start:(start + maxLen)]
```

> 139.单词拆分

动态规划：将原问题拆分成两个不相交的子问题

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [0]*(length+1)
        dp[0] = 1 #空字符属于任何字典
        for i in range(1, length+1):
            for j in range(0, i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                    break
        return dp[length]
```

> 198.打家劫舍

动态规划，容易得到递推公式

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0 or length == 1:
            return sum(nums)
        f_1 = nums[0]
        f_2 = max(nums[1], nums[0])
        for i in range(3,length+1):
            tmp = f_2
            f_2 = max(f_2, f_1 + nums[i-1])
            f_1 = tmp
        return f_2
```

> 221.最大正方形

要清楚从哪里递推（以右下角为基准点，而不是右上角）

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        maxValue = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    maxValue = max(maxValue, dp[i][j])
        return maxValue**2
```

> 279.完全平方数

动态规划，从初始化0开始，一点一点往前优化

```python
# python2 代码可以通过
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n + 1)
        for i in range(1,n+1):
            dp[i] = i
            for j in xrange(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j**2] + 1)
        return dp[n]

# 更好的python2 代码
class Solution(object):
    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num
        while len(num) <= n:
            num += min(num[-i*i] for i in xrange(1, int(len(num)**0.5+1))) + 1,
        return num[n]

test = Solution()
test.numSquares(7691)

# python3 想要通过，必须把数组的创建放在类中而不是函数中
class Solution(object):
    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num
        while len(num) <= n:
            num += min(num[-i*i] for i in range(1, int(len(num)**0.5+1))) + 1,
        return num[n]
```

> 309.最佳买卖股票时机含冷冻期

可参考leetcode解答，这一类题都可以用动态规划去解，关键是定义清楚所有情况，和转移状态。

```python
# 初始版本
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        length = len(prices)
        dp = [[0]*2 for _ in range(length+1)]
        # 规定初始状态
        dp[1][0], dp[1][1] = 0, -prices[0]
        dp[0][0], dp[0][1] = 0, -float('inf')
        
        for i in range(2, length+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])
        
        return dp[length][0]

test = Solution()
test.maxProfit([1,2,3,0,2])

# 优化空间复杂度版本
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        length = len(prices)
        # 初始化
        dp_1_0, dp_1_1 = 0, -prices[0]
        dp_pre_0 = 0

        for i in range(2,length+1):
            tmp = dp_1_0
            dp_1_0 = max(dp_1_0, dp_1_1 + prices[i-1])
            dp_1_1 = max(dp_1_1, dp_pre_0 - prices[i-1])
            dp_pre_0 = tmp
        
        return dp_1_0
```

> 647.回文子串

和5.最长回文子串一模一样

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        res = 0
        dp = [[0]*length for _ in range(length)]
        # dp[i][i] = 1
        for i in range(length):
            dp[i][i] = 1
            res += 1
        # dp[i][i+1]
        for i in range(length - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                res += 1
        # dp[i][i+2], ...,
        for l in range(3, length+1):
            for i in range(length - l + 1):
                j = i + l - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 1
                    res += 1
        
        return res
```

