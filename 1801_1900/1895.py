class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """最大的幻方
        1. 前缀和模拟, 时间复杂度O(m*n*min(m,n)*min(m,n))
        """
        m, n = len(grid), len(grid[0])
        ans = 1

        # presum
        row_sum = [[0]*(n+1) for _ in range(m+1)]
        col_sum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                row_sum[i][j] = row_sum[i][j-1] + grid[i-1][j-1]
                col_sum[i][j] = col_sum[i-1][j] + grid[i-1][j-1]

        def is_valid(row, col, k):
            diag, no_diag = 0, 0
            for i in range(row, row+k): # rows
                diag += grid[i][col+i-row]
                no_diag += grid[i][col+k-1-(i-row)]
                cur = row_sum[i+1][col+k] - row_sum[i+1][col]
                if i == row:
                    base = cur
                elif cur != base:
                    return False
            for j in range(col, col+k):  # cols
                cur = col_sum[row+k][j+1] - col_sum[row][j+1]
                if cur != base:
                    return False
            if diag != base or no_diag != base:
                return False        
            return True

        for i in range(m):
            for j in range(n):
                for k in range(2, min(m-i, n-j)+1):
                    if is_valid(i, j, k):
                        ans = max(ans, k)
        return ans