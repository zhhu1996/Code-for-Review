class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """被围绕的区域
        1. dfs
        先从边界的O开始遍历, 找到所有的开区间, 剩下的O则全部替换成X
        """
        m, n = len(board), len(board[0])
        visit = [[False]*n for _ in range(m)]

        def is_valid(row, col):
            return row >= 0 and row < m and col >= 0 and col < n

        def dfs(row, col):
            if not is_valid(row, col):
                return
            if visit[row][col] or board[row][col] == 'X':
                return
            visit[row][col] = True
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for i in range(m):
            for j in range(n):
                is_bound = (i == 0 or i == m-1 or j == 0 or j == n-1)
                if is_bound and board[i][j] == 'O' and not visit[i][j]:
                    dfs(i, j)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and not visit[i][j]:
                    board[i][j] = 'X'