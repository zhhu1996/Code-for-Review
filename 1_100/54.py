class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 方向矩阵 + flag判断
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        flag = [[0] * n for i in range(m)]
        res = []
        i, j, di = 0, 0, 0
        for k in range(m * n):
            res.append(matrix[i][j])
            flag[i][j] = 1
            tmpr, tmpc = i + dr[di], j + dc[di]
            if 0 <= tmpr < m and 0 <= tmpc < n and not flag[tmpr][tmpc]:
                i, j = tmpr, tmpc
            else:
                di = (di + 1) % 4
                i, j = i + dr[di], j + dc[di]

        return res