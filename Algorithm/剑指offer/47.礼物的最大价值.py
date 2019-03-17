### 47.礼物的最大价值

# 这是一道典型的动态规划问题，而且还可以对储存进行优化。

class Solution:
    def MaxValue(self, matrix):
        if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
            return
        num_row = len(matrix)
        num_col = len(matrix[0])
        res = [0]*num_col # 用来保存每一步的结果
        for i in range(num_row):
            for j in range(num_col):
                if j == 0:
                    res[j] = res[j] + matrix[i][j]
                else:
                    res[j] = max(res[j-1],res[j])+matrix[i][j]
        return res[-1]

s = Solution()
s.MaxValue([[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]])