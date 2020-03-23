class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 方向矩阵 + flag判断
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        res = [[0]*n for i in range(n)]
        i, j, di = 0, 0, 0
        for k in range(1, n*n+1):
            res[i][j] = k
            tmpr, tmpc = i + dr[di], j + dc[di]
            if 0 <= tmpr < n and 0 <= tmpc < n and res[tmpr][tmpc]==0:
                i, j = tmpr, tmpc
            else:
                di = (di + 1) % 4
                i, j = i + dr[di], j + dc[di]

        return res