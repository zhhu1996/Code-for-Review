class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. 新建一个矩阵，按照以下规则进行更新
        # (i, j) -> (j, n-i-1)

        # # 2. 原地改变数组，要求我们进一步找规律
        # # (i, j) -> (j, i) -> (j, n-1-i)
        # # 即先转置再关于y轴对称
        # rows, cols = len(matrix), len(matrix[0])
        # for i in range(rows):
        #     for j in range(i, cols):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = temp
        # for i in range(rows):
        #     matrix[i][:] = matrix[i][::-1]

        # 3. 回溯法, 规律: 原数组m[i][j] -> 新数组m[j][n-1-i]
        n = len(matrix)
        visit = [[False for i in range(n)] for j in range(n)]
        
        def dfs(row, col, value, visit, matrix, isfirst):
            """
                row: 当前遍历行
                col: 当前遍历列
                value: 上一个位置被覆盖的值
                visit: 是否访问过
                matrix: 原数组
                isfirst: 是否是第一个被交换的位置
            """
            if visit[row][col]:
                return
            n = len(matrix)
            if not isfirst:
                visit[row][col] = True
            tmp = matrix[row][col]
            matrix[row][col] = value
            dfs(col, n-1-row, tmp, visit, matrix, False)
        
        for i in range(n):
            for j in range(n):
                if not visit[i][j]:
                    dfs(i, j, 0, visit, matrix, True)