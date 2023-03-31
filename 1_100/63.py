class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. 回溯，超时

        # 2. dp, 矩阵, 位置i/j必取, O(1)个子问题
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*cols for i in range(rows)]
        for i in range(rows):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for j in range(cols):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[rows-1][cols-1]

