class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """回溯法"""

        def judgeK(row, col, k):
            sum = 0
            while row > 0:
                sum += row % 10
                row = row // 10
            while col > 0:
                sum += col % 10
                col = col // 10
            if sum > k:
                return False
            else:
                return True

        def movingCountCore(m, n, row, col, k, visited):
            """直接返回count"""
            count = 0
            if 0 <= row < m and 0 <= col < n and not visited[row][col] and judgeK(row, col, k):
                visited[row][col] = True
                count = 1 + movingCountCore(m, n, row-1, col, k, visited) \
                        + movingCountCore(m, n, row+1, col, k, visited)   \
                        + movingCountCore(m, n, row, col-1, k, visited)   \
                        + movingCountCore(m, n, row, col+1, k, visited)
            return count

        def movingCountCoreV2(m, n, row, col, k, visited):
            """最后统计count"""
            if 0 <= row < m and 0 <= col < n and not visited[row][col] and judgeK(row, col, k):
                visited[row][col] = True
                movingCountCoreV2(m, n, row - 1, col, k, visited)
                movingCountCoreV2(m, n, row + 1, col, k, visited)
                movingCountCoreV2(m, n, row, col - 1, k, visited)
                movingCountCoreV2(m, n, row, col + 1, k, visited)

        visited = [[False] * n for i in range(m)]
        return movingCountCore(m, n, 0, 0, k, visited)
        # movingCountCoreV2(m, n, 0, 0, k, visited)
        # count = 0
        # for i in range(m):
        #     for j in range(n):
        #         if visited[i][j]:
        #             count += 1
        # return count