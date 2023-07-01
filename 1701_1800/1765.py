class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """地图中的最高点
        1. 多源BFS, 时间复杂度O(n^2)
        任意相邻格的高度差至多为1 & 水源高度必须为0 => 以水源为起点BFS, 得到陆地的高度 
        => 多水源(多源BFS问题), 陆地高度等于最小值
        可以通过虚拟节点转化成单源BFS问题

        2. dp
        矩阵, 位置i,j必取, O(1)个子问题
        dp[i][j]: 点(i,j)距离水源的最近距离 
        """
        # 1.
        m, n = len(isWater), len(isWater[0])
        ans = [[-1]*n for _ in range(m)]
        drs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    q.append((i, j))
        h = 1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for i in range(len(drs)):
                    nx, ny = x+drs[i][0], y+drs[i][1]
                    if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] == -1:
                        ans[nx][ny] = h
                        q.append((nx, ny))
            h += 1
        return ans


        # # 2.
        # m, n = len(isWater), len(isWater[0])
        # dp = [[float('inf')]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if isWater[i][j] == 1:
        #             dp[i][j] = 0
        # for i in range(m):
        #     for j in range(n):
        #         if i-1 >= 0:
        #             dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
        #         if j-1 >= 0:
        #             dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if i+1 < m:
        #             dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
        #         if j+1 < n:
        #             dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
        # return dp    