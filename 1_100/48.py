class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. 新建一个矩阵，按照以下规则进行更新
        # (i, j) -> (j, n-i-1)

        # 2. 原地改变数组，要求我们进一步找规律
        # (i, j) -> (j, i) -> (j, n-1-i)
        # 即先转置再关于y轴对称
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(i, cols):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(rows):
            matrix[i][:] = matrix[i][::-1]