class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """买卖股票的最佳时机III
        dp[i][k][s]表示第i天结束后卖出k次后进行s操作后可获得的最大利润, 
            k=0表示卖出了0次, k=1表示卖出了1次, k=2表示卖出了2次
            s=0表示持仓, s=1表示不持仓
        dp[i][0][0] = max(dp[i-1][0][0], -prices[i])
        dp[i][0][1] = 0
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]-prices[i])
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]+prices[i])
        dp[i][2][0] = -float('inf')
        dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0]+prices[i])
        """
        n = len(prices)
        dp = [[[0 for i in range(2)] for j in range(3)] for k in range(n)]
        # init
        dp[0][0][0], dp[0][0][1] = -prices[0], 0
        dp[0][1][0], dp[0][1][1], dp[0][2][0], dp[0][2][1] = -float('inf'), -float('inf'), -float('inf'), -float('inf')
        # dp
        for i in range(1, n):
            dp[i][0][0] = max(dp[i-1][0][0], -prices[i])
            dp[i][0][1] = 0
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]-prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]+prices[i])
            dp[i][2][0] = -float('inf')
            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0]+prices[i])
        return max(0, dp[n-1][1][1], dp[n-1][2][1])