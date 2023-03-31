class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """零钱兑换
        1. 单串dp, 位置i可不取, O(n)个子问题
        dp[i]: 总金额为i的最少硬币数

        2. 完全背包问题
        dp[i][v]: 前i个硬币达到面额k的最少数量
        dp[i][v] = min(dp[i-1][v], dp[i][v-ci]+1)
        => 优化到1维
        dp[v]: 面额k的最少数量
        """
        # # 1.
        # dp = [float('inf')]*(amount+1)
        # dp[0] = 0
        # for i in range(1, amount+1):
        #     for j in range(len(coins)):
        #         if i-coins[j] >= 0:
        #             dp[i] = min(dp[i], dp[i-coins[j]]+1)
        # return dp[amount] if dp[amount] < float('inf') else -1

        # # 2. 二维
        # n = len(coins)
        # dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
        # dp[0][0] = 0
        # for i in range(1, n+1):
        #     ci = coins[i-1]
        #     for v in range(amount+1):
        #         if v < ci:
        #             dp[i][v] = dp[i-1][v]
        #         else:
        #             dp[i][v] = min(dp[i-1][v], dp[i][v-ci]+1)
        # return dp[n][amount] if dp[n][amount] != float('inf') else -1

        # 2. 一维
        n = len(coins)
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, n+1):
            ci = coins[i-1]
            for v in range(ci, amount+1):
                dp[v] = min(dp[v], dp[v-ci]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
