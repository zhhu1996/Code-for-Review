class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """最大人工岛
        1. dfs
        先通过dfs得到每个岛屿的面积, 然后遍历每个海洋, 计算联通后的最大面积
        """
        m, n = len(grid), len(grid[0])
        lands = {}
        ans = 0

        def is_valid(row, col):
            return row >= 0 and row < m and col >= 0 and col < n

        def dfs(row, col, index):
            if not is_valid(row, col):
                return 0
            if grid[row][col] != 1:
                return 0
            grid[row][col] = index
            return 1 + dfs(row-1, col, index) + dfs(row+1, col, index) + \
                       dfs(row, col-1, index) + dfs(row, col+1, index)

        def dfs_water(row, col):
            i_set = set()
            ans = 1
            ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d in ds:
                r, c = row + d[0], col + d[1]
                if not is_valid(r, c):
                    continue
                if grid[r][c] not in i_set and grid[r][c] in lands:
                    ans += lands[grid[r][c]]
                    i_set.add(grid[r][c])
            return ans
        
        index = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    lands[index] = dfs(i, j, index)
                    ans = max(ans, lands[index])
                    index += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans, dfs_water(i, j))
        return ans