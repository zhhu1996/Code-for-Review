class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """最大加号标志
        1. 暴力, 时间复杂度O(n^3), 超时

        2. dp
        双串, 位置i必取, O(1)个子问题
        """
        zeros = set()
        for xi, yi in mines:
            zeros.add((xi, yi))
        left = [[0]*n for _ in range(n)]
        right = [[0]*n for _ in range(n)]
        up = [[0]*n for _ in range(n)]
        down = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (i, j) in zeros:
                    left[i][j] = 0
                    up[i][j] = 0
                else:
                    left[i][j] = (1 + left[i][j-1] if j > 0 else 1)
                    up[i][j] = (1 + up[i-1][j] if i > 0 else 1)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) in zeros:
                    right[i][j] = 0
                    down[i][j] = 0
                else:
                    right[i][j] = (1 + right[i][j+1] if j+1 < n else 1)
                    down[i][j] = (1 + down[i+1][j] if i+1 < n else 1)
        # dp
        ans = 0
        for i in range(n):
            for j in range(n):
                cur = min(left[i][j], right[i][j], up[i][j], down[i][j])
                ans = max(ans, cur)
        return ans