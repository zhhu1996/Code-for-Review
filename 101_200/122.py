class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        带维度单串, O(1)个子问题, 位置i必取
        dp[i][0]: 到第i天持有股票的最大利润
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
        dp[i][1]: 到第i天持有现金的最大利润
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])
        """
        n = len(prices)
        if n <= 1: return 0
        dp = [[0]*2 for _ in range(n)]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return max(dp[n-1])
