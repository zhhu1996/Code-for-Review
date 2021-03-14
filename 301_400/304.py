class NumMatrix:
    """
    方法1: 以dp[i][j][p][q]表示起点到终点的区域和，具体区间和用前缀计算，时间复杂度为O(n^4)

    方法2: 每一行计算前缀和，以dp[i][j]表示matrix[i][:j]的和
    那么(row1,col1)->(row2,col2)的区域和就等于sum(dp[i][col2]-dp[i][col1-1])
    时间复杂度O(n^2)
    """

    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix
    #     self.initAns(matrix)
    #     self.cal2dAns()
    #     # print(self.ans)
    #     # print(self.ans)
    #
    # def initAns(self, matrix):
    #     if not matrix:
    #         return []
    #     m,n = len(matrix),len(matrix[0])
    #     self.ans = []
    #     for i in range(m):
    #         tempj = []
    #         for j in range(n):
    #             tempp = []
    #             for p in range(m):
    #                 tempq = [0 for q in range(n)]
    #                 tempp.append(tempq)
    #             tempj.append(tempp)
    #         self.ans.append(tempj)
    #
    # def cal2dAns(self):
    #     if not self.matrix:
    #         return
    #     m,n = len(self.matrix), len(self.matrix[0])
    #     for i in range(m):
    #         rowSum = [0 for _ in range(n)]
    #         for j in range(i,m):
    #             for k in range(n):
    #                 rowSum[k] += self.matrix[j][k]
    #             cumSum = self.cal1dAns(rowSum)
    #             for p in range(n):
    #                 for q in range(p,n):
    #                     if p >= 1:
    #                         self.ans[i][p][j][q] = cumSum[q] - cumSum[p-1]
    #                     else:
    #                         self.ans[i][p][j][q] = cumSum[q]
    #
    # def cal1dAns(self, array):
    #     if not array:
    #         return []
    #     cur = 0
    #     n = len(array)
    #     cumSum = []
    #     for i in range(n):
    #         cur += array[i]
    #         cumSum.append(cur)
    #     return cumSum
    #
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     return self.ans[row1][col1][row2][col2]

    def __init__(self, matrix: List[List[int]]):
        if matrix:
            self.m, self.n = len(matrix), len(matrix[0])
        else:
            self.m, self.n = 0, 0
        self.matrix = matrix
        self.cumSum = []
        self.getRowSum()

    def getRowSum(self):
        for i in range(self.m):
            cur = 0
            tmp = []
            for j in range(self.n):
                cur += self.matrix[i][j]
                tmp.append(cur)
            self.cumSum.append(tmp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        for i in range(row1, row2 + 1):
            if col1 >= 1:
                result += self.cumSum[i][col2] - self.cumSum[i][col1 - 1]
            else:
                result += self.cumSum[i][col2]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)