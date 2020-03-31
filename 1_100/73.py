class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. 重建一个矩阵，然后根据原矩阵的0值修改，空间复杂度O(mn)

        # 2. 新建一个row数组和col数组，遍历原矩阵将对应的row数组元素和col数组元素置1，最后再修改原数组，空间复杂度O(m+n)

        # 3. 利用第一行和第一列作为标志位，空间复杂度O(1)
        rowFlag, colFlag = False, False
        rows, cols = len(matrix), len(matrix[0])
        for i in range(cols):
            if matrix[0][i] == 0:
                rowFlag = True
                break
        for j in range(rows):
            if matrix[j][0] == 0:
                colFlag = True
                break
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if rowFlag:
            for j in range(cols):
                matrix[0][j] = 0
        if colFlag:
            for i in range(rows):
                matrix[i][0] = 0
