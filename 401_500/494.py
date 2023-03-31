class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """目标和
        1. 回溯, 时间复杂度O(2^n)
        每个位置只有+/-的选项

        2. dp
        0/1背包
        dp[i][v]: 前i个元素和为v的组合数目

        3. 另一种dp思路
        设pos为取+的和, neg为取-的和, 即有 (sum-neg)-neg=target
        => neg = (sum-target) / 2
        dp[i][v]: 前i个元素和为v的组合数目
        => 空间优化
        """
        # 2. 朴素dp
        # n = len(nums)
        # tsum = sum(nums)
        # if abs(target) > tsum:
        #     return 0
        # t = 2*tsum + 1
        # dp = [[0]*t for _ in range(n+1)]
        # dp[0][tsum] = 1
        # for i in range(1, n+1):
        #     for v in range(t):
        #         plus = v-nums[i-1] if v-nums[i-1] >= 0 else 0
        #         minus = v+nums[i-1] if v+nums[i-1] <= t-1 else t-1
        #         dp[i][v] = dp[i-1][plus] + dp[i-1][minus]
        # return dp[n][target+tsum]

        
        # 3. 另一dp思路
        n = len(nums)
        tsum = sum(nums)
        if (tsum-target) % 2 != 0 or tsum < target:
            return 0
        neg = (tsum-target) // 2
        dp = [[0]*(neg+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for v in range(neg+1):
                dp[i][v] = dp[i-1][v]
                if v - nums[i-1] >= 0:
                    dp[i][v] += dp[i-1][v-nums[i-1]]
        return dp[n][neg]


        # 3. 空间优化
        n = len(nums)
        tsum = sum(nums)
        if (tsum-target) % 2 != 0 or tsum < target:
            return 0
        neg = (tsum-target) // 2
        dp = [0]*(neg+1)
        dp[0] = 1
        for i in range(1, n+1):
            for v in range(neg, -1, -1):
                if v - nums[i-1] >= 0:
                    dp[v] += dp[v-nums[i-1]]
        return dp[neg]