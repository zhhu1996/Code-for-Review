class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """粉刷房子
        1. dp
        带维度单串, 位置i/k可不取, O(1)个子问题
        dp[i][k]: 前i个房子, 最后一个刷k颜色的最小成本
        """
        n = len(costs)
        dp = [[0]*3 for _ in range(n)]
        dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        return min(dp[n-1])