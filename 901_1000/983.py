class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """最低票价
        1. dp
        单串dp, 位置i必取, O(1)个子问题
        """
        dp = [float('inf')]*366
        dp[0] = 0
        targets = set(days)
        for i in range(1, 366):
            if i in targets:
                dp[i] = min(dp[i], \
                            dp[max(i-1, 0)]+costs[0],  \
                            dp[max(i-7, 0)]+costs[1],  \
                            dp[max(i-30, 0)]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]