class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """矩阵区域和
        1. 二维前缀和
        先求(0,0)->(i,j)的前缀和,再求(i-k,j-k)->(i+k,j+k)的前缀和
        """
        m, n = len(mat), len(mat[0])
        dp = [[0 for i in range(1+n)] for j in range(1+m)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + mat[i-1][j-1]
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                # (i-k,j-k)->(i+k,j+k)的区域和
                row1 = i-k if i-k >= 0 else 0
                col1 = j-k if j-k >= 0 else 0
                row2 = i+k if i+k <= m-1 else m-1
                col2 = j+k if j+k <= n-1 else n-1
                res[i][j] = dp[row2+1][col2+1] - dp[row2+1][col1] - dp[row1][col2+1] + dp[row1][col1] 
        return res