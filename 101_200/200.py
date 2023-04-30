class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """岛屿数量
        1. dfs
        求最大联通子图数
        """
        m, n = len(grid), len(grid[0])
        ans = 0
        
        def is_valid(row, col):
            return row >= 0 and row < m and col >= 0 and col < n 

        def dfs(row, col):
            if not is_valid(row, col): return
            if grid[row][col] != '1': return
            grid[row][col] = '2'
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans