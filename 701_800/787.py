class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """K站中转内最便宜的航班
        1. 限制步长求最短路: bellman ford算法
        dp[k][j]: 从起点经过k步到达点j的最短路径
        dp[k][j] = min(dp[k][j], dp[k-1][i] + cost(i,j))
        -> 空间优化: 用两个一维数组取代矩阵 
        """
        dp = [[float('inf')]*n for _ in range(k+2)]
        dp[0][src] = 0
        ans = float('inf')
        for t in range(1, k+2):
            for s, e, cost in flights:
                dp[t][e] = min(dp[t][e], dp[t-1][s] + cost)
        for i in range(k+2):
            ans = min(ans, dp[i][dst])
        return ans if ans != float('inf') else -1