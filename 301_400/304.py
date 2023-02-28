class NumMatrix:
    """二维区域和检索 - 矩阵不可变
    1. 利用1维前缀和思想, 查询二维区域和需要O(n^2)

    2. 先求(0,0)到(i,j)的区域和, 再求(row1,col1)到(row2,col2)
    i. (0,0) -> (i,j)
    dp[i][j]表示 (0,0) -> (i,j) 的区域和, dp可以建成(m+1)*(n+1)大小
    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
    ii.(row1,col1) -> (row2,col2)
    S = dp[row2][col2] + dp[row1-1][col1-1] - dp[row1-1][col2] - dp[row2][col1-1]
    """
    # # 1.
    # def __init__(self, matrix: List[List[int]]):
    #     m, n = len(matrix), len(matrix[0])
    #     self.csum = [[0 for i in range(n+1)] for j in range(m)]
    #     for i in range(m):
    #         for j in range(1,1+n):
    #             self.csum[i][j] = matrix[i][j-1] + self.csum[i][j-1]

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     res = 0
    #     for row in range(row1, row2+1):
    #         res += self.csum[row][col2+1] - self.csum[row][col1]
    #     return res

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        # dp[i][j]
        self.dp = [[0 for i in range(n)] for j in range(m)]
        self.dp[0][0] = matrix[0][0]
        for i in range(1,n):
            self.dp[0][i] = matrix[0][i] + self.dp[0][i-1]
        for i in range(1, m):
            self.dp[i][0] = matrix[i][0] + self.dp[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        if row1 == 0 and col1 == 0:
            res = self.dp[row2][col2]
        elif row1 == 0:
            res = self.dp[row2][col2] - self.dp[row2][col1-1]
        elif col1 == 0:
            res = self.dp[row2][col2] - self.dp[row1-1][col2]
        else:
            res = self.dp[row2][col2] + self.dp[row1-1][col1-1] - self.dp[row1-1][col2] - self.dp[row2][col1-1]
        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)