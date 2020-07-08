class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """求礼物的最大价值
        1. 回溯法, 太慢

        2. 动态规划, dp[i] = max(dp[i], dp[i-1]) + grid[row][i]
        """
        if not grid:
            return 0
        dp = [0 for i in range(len(grid[0]))]
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if j > 0:
                    dp[j] = max(dp[j], dp[j-1]) + grid[i][j]
                else:
                    dp[j] = dp[j] + grid[i][j]
        return dp[-1]