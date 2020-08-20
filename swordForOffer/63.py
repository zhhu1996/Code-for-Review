class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """股票的最大利润
        dp[i] = prices[i] - min(prices[:i])
        """
        if not prices:
            return 0
        maxprofit = 0
        minprice = prices[0]
        for i in range(1, len(prices)):
            maxprofit = max(maxprofit, prices[i] - minprice)
            minprice = min(minprice, prices[i])
        return maxprofit
