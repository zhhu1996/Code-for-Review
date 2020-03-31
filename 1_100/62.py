class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. 回溯, 时间复杂度O(m*n)，因为进行了m*n次递归，性能很差，超时
        # self.res = 0
        #
        # def run(x, y, targetX, targetY):
        #     if x == targetX and y == targetY:
        #         self.res += 1
        #         return
        #
        #     if x < targetX:
        #         run(x+1, y, targetX, targetY)
        #     if y < targetY:
        #         run(x, y+1, targetX, targetY)
        #
        # run(0, 0, m-1, n-1)
        # return self.res

        # 2. 动态规划，dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[0]*n for i in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


