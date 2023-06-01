class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """球会落何处
        1. 模拟, 时间复杂度O(mn)
        只要不遇边界, 不形成V型, 球就可以向下滑动
        """
        def ball_move(col, m, n):
            row = 0
            while row < m:
                if grid[row][col] == 1:
                    if col == n-1 or grid[row][col+1] == -1:
                        return -1
                    else:
                        row += 1
                        col += 1
                else: # -1
                    if col == 0 or grid[row][col-1] == 1:
                        return -1
                    else:
                        row += 1
                        col -= 1
            return col

        rows, cols = len(grid), len(grid[0])
        return [ball_move(col, rows, cols) for col in range(cols)]