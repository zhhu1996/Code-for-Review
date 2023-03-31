class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """叶值的最小代价生成树
        1. dp
        区间, 位置i必取, O(n)个子问题
        dp[i][j]表示arr[i..j]的最小代价生成树
        dp[i][j] = min(dp[i][k] + dp[k+1][j] + lmax*rmax), lmax=max(arr[i..k]), rmax=max(arr[k..j])
        """
        n = len(arr)
        dp = [[float('inf')]*(n) for _ in range(n)]
        for lth in range(1, n+1):
            for l in range(n-lth+1):
                r = l + lth - 1
                if l == r:
                    dp[l][r] = arr[l]
                    continue
                # dp
                for k in range(l, r):
                    # 预处理lmax, rmax可以加速
                    lmax = max(arr[l: k+1])
                    rmax = max(arr[k+1: r+1])
                    cand = lmax * rmax
                    if k-l > 0:
                        cand += dp[l][k]
                    if r-k > 1:
                        cand += dp[k+1][r]
                    dp[l][r] = min(dp[l][r], cand)
        return dp[0][n-1]