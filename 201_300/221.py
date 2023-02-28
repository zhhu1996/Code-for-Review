class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """最大正方形
        1. dp
        dp[i][j]表示从(0,0)到(i,j)的包含1的最大正方形的边长, matrix[i][j]必须取
        i.  matrix[i][j] = 0
        dp[i][j] = 0
        ii. matrix[i][j] = 1
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res = max(res, dp[i][j])
        return res**2