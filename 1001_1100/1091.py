class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """二进制矩阵中的最短路径
        1. bfs
        """
        from queue import Queue

        n = len(grid)
        if grid[0][0] != 0: 
            return -1
        q = Queue(-1)

        def is_valid(row, col):
            return row >= 0 and row < n and col >= 0 and col < n

        q.put((0,0))
        grid[0][0] = -1 # visited
        ans = 0
        while not q.empty():
            size = q.qsize()
            ans += 1
            for i in range(size):
                x, y = q.get()
                if x == n-1 and y == n-1:
                    return ans
                ds = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
                for d in ds:
                    nx, ny = x + d[0], y + d[1]
                    if is_valid(nx, ny) and grid[nx][ny] == 0:
                        q.put((nx, ny))
                        grid[nx][ny] = -1
        return -1