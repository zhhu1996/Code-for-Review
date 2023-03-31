class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        """矩阵中最长的连续1线段
        1. dp
        带维度矩阵, 位置i,j必取, O(1)个子问题
        dp[i][j][k]: 以mat[i][j]为终点的k方向最长连续1长度
        """
        m, n = len(mat), len(mat[0])
        dp = [[[0,0,0,0] for _ in range(n+2)] for _ in range(m+2)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if mat[i-1][j-1] == 0:
                    continue
                dp[i][j][0] = dp[i][j-1][0] + 1
                dp[i][j][1] = dp[i-1][j][1] + 1
                dp[i][j][2] = dp[i-1][j-1][2] + 1
                dp[i][j][3] = dp[i-1][j+1][3] + 1
                res = max(res, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return res