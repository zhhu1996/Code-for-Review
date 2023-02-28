class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """三角形最小路径和
        1. dp
        dp[i][j]表示到triangle[i][j]的最小路径和, 最小路径和为min(dp[-1])
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        """
        m = len(triangle)
        dp = [[float('inf') for i in range(m)] for j in range(m)]
        # init
        dp[0][0] = triangle[0][0] # i = 0
        for j in range(1, m):     # j = 0
            dp[j][0] = dp[j-1][0] + triangle[j][0]
        # dp
        for i in range(1, m):
            for j in range(1, len(triangle[i])):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[m-1])