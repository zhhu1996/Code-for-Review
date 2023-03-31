class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """出界的路径数
        1. dp
        dp[i][j][k]: 在坐标(i, j)处经过k步刚好出界的路径数量
        dp[i][j][k] = dp[i-1][j][k-1] + dp[i][j-1][k-1] + dp[i+1][j][k-1] + dp[i][j+1][k-1]
        """
        dp = [[[0]*(n+2) for _ in range(m+2)] for _ in range(1+maxMove)]
        res = 0
        # k = 0
        for i in range(n+2):
            dp[0][0][i] = 1
            dp[0][m+1][i] = 1
        for j in range(m+2):
            dp[0][j][0] = 1
            dp[0][j][n+1] = 1
        # dp
        for k in range(1, maxMove+1):
            for i in range(1, m+1):
                for j in range(1, n+1):
                    dp[k][i][j] = dp[k-1][i-1][j] + dp[k-1][i][j-1] + \
                                  dp[k-1][i+1][j] + dp[k-1][i][j+1]
        # get res
        for k in range(1+maxMove):
            res += dp[k][startRow+1][startColumn+1]
        return res % (10**9 + 7)