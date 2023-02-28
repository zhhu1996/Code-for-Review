class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """下降路径最小和
        1. dp
        dp[i][j]表示从第一行开始到(i,j)的最小下降路径和
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        i. i = 0
        dp[i][j] = matrix[i][j]
        ii. j = 0
        dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        iii. j = n-1
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]
        iv. else
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        """
        n = len(matrix)
        if n <= 1:
            return matrix[0][0]
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = matrix[i][j]
                elif j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        return min(dp[n-1])