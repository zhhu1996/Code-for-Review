class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """粉刷房子II
        1. dp, 时间复杂度O(nkk)
        带维度单串, 位置i/k可不取, O(1)个子问题
        => 优化成O(nk)
        对于dp[i], 计算最小值与次小值, 加速dp[i+1]的计算
        """
        # # 1. O(nkk)
        # n, k = len(costs), len(costs[0])
        # dp = [[float('inf')]*k for _ in range(n)]
        # for i in range(k):
        #     dp[0][i] = costs[0][i]
        # for i in range(1, n):
        #     for j in range(k):
        #         # dp[i][j]
        #         for z in range(k):
        #             if z == j: continue
        #             dp[i][j] = min(dp[i][j], dp[i-1][z])
        #         dp[i][j] += costs[i][j]
        # return min(dp[n-1])

        # 2. O(nk)
        n, k = len(costs), len(costs[0])
        dp = [[float('inf')]*k for _ in range(n)]
        fst_min, sed_min = float('inf'), float('inf')
        # init
        for i in range(k):
            dp[0][i] = costs[0][i]
            if dp[0][i] < fst_min:
                sed_min = fst_min
                fst_min = dp[0][i]
            else:
                sed_min = min(sed_min, dp[0][i])
        # dp
        for i in range(1, n):
            nfst_min, nsed_min = float('inf'), float('inf')
            print(fst_min, sed_min)
            for j in range(k):
                # dp[i][j]
                dp[i][j] = (sed_min if dp[i-1][j] == fst_min else fst_min)
                dp[i][j] += costs[i][j]
                if dp[i][j] < nfst_min:
                    nsed_min = nfst_min
                    nfst_min = dp[i][j]
                else:
                    nsed_min = min(nsed_min, dp[i][j])
            fst_min = nfst_min
            sed_min = nsed_min

        return min(dp[n-1])