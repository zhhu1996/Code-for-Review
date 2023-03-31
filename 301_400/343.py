class Solution:
    def integerBreak(self, n: int) -> int:
        """整数拆分
        1. 完全背包
        dp[i][v]: 长度为i且和为n的最大乘积
            dp[i][v] = max(dp[i-1][v-ci]*ci)
        => 优化到1维
        dp[v]: 和为n的最大乘积
            dp[v] = max(dp[v-ci]*ci)

        2. 单串dp
        dp[i]表示将i拆分为至少2个正整数的最大乘积
        dp[i] = max(j*(i-j), j*dp[i-j]), 1<=j<i
        """
        # # 1. 二维
        # dp = [[0]*(n+1) for _ in range(n+1)]
        # dp[0][0] = 1
        # res = 0
        # for i in range(1, n+1):
        #     for v in range(n+1):
        #         if v < i:
        #             dp[i][v] = 0
        #         elif v == i:
        #             dp[i][v] = 1
        #         else:
        #             for x in range(1, v+1):
        #                 dp[i][v] = max(dp[i][v], dp[i-1][v-x]*x)
        #     if i > 1:
        #         res = max(res, dp[i][n])
        # # for x in dp:print(x)
        # return res

        # 1. 一维
        if n <= 2:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for v in range(1, n+1):
                if i < n:
                    if i >= v:
                        dp[i] = max(dp[i], dp[i-v]*v)
                else: # 去除1个正整数的状态
                    if i > v:
                        dp[i] = max(dp[i], dp[i-v]*v)
        # print(dp)
        return dp[n]

        # # 2.
        # dp = [0 for i in range(1+n)]
        # for i in range(2, n+1):
        #     for j in range(1, i):
        #         dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        # return dp[n]