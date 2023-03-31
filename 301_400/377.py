class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """组合总和IV
        1. 完全背包
        dp[i][v]: 长度为i且和为v的排列个数
        dp[i][v] = sum(dp[i-1][v-ci])
        => 优化到1维
        dp[v]: 和为v的排列个数
        """
        # # 二维
        # n = target
        # dp = [[0]*(1+target) for _ in range(n+1)]
        # dp[0][0] = 1
        # res = 0
        # for i in range(1, n+1):
        #     for v in range(1+target):
        #         for num in nums:
        #             if v >= num:
        #                 dp[i][v] += dp[i-1][v-num]
        #     res += dp[i][target]
        #     # print(dp[i])
        # return res

        # 1维
        n = target
        dp = [0]*(1+target)
        dp[0] = 1
        for v in range(1+target):
            for num in nums:
                if v >= num:
                    dp[v] += dp[v-num]
        return dp[-1]