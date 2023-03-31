class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """轰炸敌人
        1. dp
        矩阵, 位置i,j必取, O(1)个子问题
        dp[i][j][0]: 第j列nums[0..i]的敌人数(向上)
        dp[i][j][1]: 第j列nums[i..m]的敌人数(向下)
        dp[i][j][2]: 第i行nums[0..j]的敌人数(向左)
        dp[i][j][3]: 第i行nums[j..n]的敌人数(向右)
        """
        m, n = len(grid), len(grid[0])
        dp = [[[0,0,0,0] for _ in range(n+2)] for _ in range(m+2)]
        res = 0
        # 上/左
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == 'W':
                    dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3] = 0,0,0,0
                elif grid[i-1][j-1] == 'E':
                    dp[i][j][0] = dp[i-1][j][0] + 1
                    dp[i][j][2] = dp[i][j-1][2] + 1
                else:
                    dp[i][j][0] = dp[i-1][j][0]
                    dp[i][j][2] = dp[i][j-1][2]
        # 下/右
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if grid[i-1][j-1] == 'W':
                    dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3] = 0,0,0,0
                elif grid[i-1][j-1] == 'E':
                    dp[i][j][1] = dp[i+1][j][1] + 1
                    dp[i][j][3] = dp[i][j+1][3] + 1
                else:
                    dp[i][j][1] = dp[i+1][j][1]
                    dp[i][j][3] = dp[i][j+1][3]
                    res = max(res, sum(dp[i][j]))
        return res