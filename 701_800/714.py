class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """买卖股票的最佳时机含手续费
        1. dp
        带维度单串, 位置i必取, O(1)个子问题
        dp[i][0]: 至第i天持仓的最大收益
        dp[i][1]: 至第i天空仓的最大收益
        """
        n = len(prices)
        if n <= 1: return 0
        dp = [[0]*2 for i in range(n)]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
        return dp[n-1][1]