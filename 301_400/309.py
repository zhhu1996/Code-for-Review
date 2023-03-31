class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """最佳买卖股票时机含冷冻期
        1. dp
        带维度单串, 位置i必取, O(1)个子问题
        dp[i][0]: 到第i天持有股票的最大收益
        dp[i][1]: 到第i天持有现金且当天没卖出的最大收益
        dp[i][2]: 到第i天持有现金且当天卖出的最大收益
        """
        n = len(prices)
        if n <= 1: return 0
        dp = [[0]*3 for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = -prices[0], 0, 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0]+prices[i]
        return max(dp[n-1])