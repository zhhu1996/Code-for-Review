class Solution:
    def integerBreak(self, n: int) -> int:
        """整数拆分
        1. 矩阵dp, 时间复杂度O(n^2)
        dp[i][j]表示和为i的j个正整数的最大乘积
        dp[i][j] = max(k*dp[i-k][j-1]), 1<=k<n

        2. 单串dp
        dp[i]表示将i拆分为至少2个正整数的最大乘积
        dp[i] = max(j*(i-j), j*dp[i-j]), 1<=j<i
        """
        # # 1.
        # dp = [[0 for i in range(1+n)] for j in range(1+n)]
        # # dp
        # for i in range(1, n+1):
        #     for j in range(1, i+1):
        #         if j == 1 and i != n:
        #             dp[i][j] = i
        #             continue
        #         for k in range(1, i):
        #             dp[i][j] = max(dp[i][j], k*dp[i-k][j-1])
        # return max(dp[n])

        # 2.
        dp = [0 for i in range(1+n)]
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]