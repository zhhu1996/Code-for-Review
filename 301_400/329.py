class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """矩阵中的最长递增路径
        1. 递归 + 记忆化
        """
        m, n = len(matrix), len(matrix[0])
        self.dp = [[1]*n for _ in range(m)]
        res = 1

        def dfs(row, col):
            if self.dp[row][col] > 1:
                return self.dp[row][col]
            if row-1 >= 0 and matrix[row-1][col] > matrix[row][col]:
                self.dp[row][col] = max(dfs(row-1, col)+1, self.dp[row][col])
            if row+1 < m and matrix[row+1][col] > matrix[row][col]:
                self.dp[row][col] = max(dfs(row+1, col)+1, self.dp[row][col])
            if col-1 >= 0 and matrix[row][col-1] > matrix[row][col]:
                self.dp[row][col] = max(dfs(row, col-1)+1, self.dp[row][col])
            if col+1 < n and matrix[row][col+1] > matrix[row][col]:
                self.dp[row][col] = max(dfs(row, col+1)+1, self.dp[row][col])
            return self.dp[row][col]

        for i in range(m):
            for j in range(n):
                res = max(dfs(i, j), res)
        return res