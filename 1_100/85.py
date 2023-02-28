class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """最大矩形
        1. 暴力+dp, 时间复杂度O(n^3)
        遍历每个节点, 求以该节点为右下角的最大矩形(枚举所有高度的矩形)
        width[i][j]表示matrix[i][..j]的最大矩形长度
        i.  matrix[i][j] = 0
        width[i][j] = 0
        ii. matrix[i][j] = 1
        width[i][j] = width[i][j-1] + 1

        2. 暴力+dp优化
        dp[i][j][k]表示以节点(i, j)为顶点的矩形在方向k上的最大连接长度, 
            k=0表示向左方向上的最大连接长度, k=1表示向上方向上的最大连接长度
        i.  matrix[i][j] = 0
        dp[i][j][0] = dp[i][j][1] = 0
        ii. matrix[i][j] = 1
        dp[i][j][0] = dp[i][j-1][0] + 1
        dp[i][j][1] = dp[i-1][j][1] + 1
        """
        # # 1.
        # m, n = len(matrix), len(matrix[0])
        # width = [[0 for i in range(n)] for j in range(m)]
        # max_area = 0
        # for row in range(m):
        #     for col in range(n):
        #         # 更新width
        #         if matrix[row][col] == '1':
        #             if col == 0:
        #                 width[row][col] = 1
        #             else:
        #                 width[row][col] = width[row][col-1] + 1
        #         else:
        #             width[row][col] = 0
        #         min_w = width[row][col]
        #         for k in range(row, -1, -1):
        #             height = row - k + 1
        #             min_w = min(width[k][col], min_w)
        #             max_area = max(height*min_w, max_area)
        # return max_area

        # 2.
        m, n = len(matrix), len(matrix[0])
        dp = [[[0 for i in range(2)] for i in range(n)] for j in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 and j == 0:
                        dp[i][j][0] = 1
                        dp[i][j][1] = 1
                    elif i == 0:
                        dp[i][j][0] = dp[i][j-1][0] + 1
                        dp[i][j][1] = 1
                    elif j == 0:
                        dp[i][j][0] = 1
                        dp[i][j][1] = dp[i-1][j][1] + 1
                    else:
                        dp[i][j][0] = dp[i][j-1][0] + 1
                        dp[i][j][1] = dp[i-1][j][1] + 1
                else:
                    dp[i][j][0] = 0
                    dp[i][j][1] = 0
                min_w = dp[i][j][0]
                for k in range(i, -1, -1):
                    height = i - k + 1
                    if height > dp[i][j][1]:
                        break
                    min_w = min(dp[k][j][0], min_w)
                    max_area = max(height*min_w, max_area)
        return max_area