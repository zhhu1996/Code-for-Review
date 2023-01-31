class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """买卖股票的最佳时机II
        1. dp
        dp[i][s]表示第i天时进行s操作后的最大利润, s=0表示持仓, s=1表示不持仓
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        """
        n = len(prices)
        s = 2
        dp = [[0 for i in range(s)] for j in range(n)]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[n-1][1]