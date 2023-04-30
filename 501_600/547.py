class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """省份数量
        1. dfs
        求最大联通子图数
        """
        n = len(isConnected)
        visit = [False]*n

        def dfs(row):
            visit[row] = True
            for col in range(n):
                if isConnected[row][col] > 0 and not visit[col]:
                    dfs(col)

        ans = 0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                ans += 1
        return ans