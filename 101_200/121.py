class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """买卖股票的最佳时机
        1. 暴力遍历, 时间复杂度O(n^2), 超时
        
        2. dp思路1, 时间复杂度O(n)
        dp[i]: 到第i天时的最大利润
        dp[i] = max(dp[i-1] + prices[i] - prices[i-1], prices[i] - prices[i-1])

        3. dp思路2, 时间复杂度O(n)
        dp[i][s]表示在第i天进行s操作后的最大利润, s=0表示持仓, s=1表示不持仓
        dp[i][0] = max(dp[i-1][0], -prices[i])
        dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])
        """
        # # 1.
        # profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j]-prices[i])
        # return profit

        # # 2.
        # n = len(prices)
        # if n <= 1: return 0
        # dp = [0]*n
        # for i in range(1, n):
        #     cand1 = dp[i-1] + prices[i] - prices[i-1]
        #     cand2 = prices[i] - prices[i-1]
        #     dp[i] = max(cand1, cand2)
        # return max(dp)

        # 3.
        n = len(prices)
        s = 2
        dp = [[0 for i in range(s)] for j in range(n)]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        return dp[n-1][1]