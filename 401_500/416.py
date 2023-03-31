class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """分割等和子集
        1. dp
        0/1背包, dp[i][v]表示前i个元素的和是否能组成v
        dp[i][v] = dp[i-1][v] or dp[i-1][v-nums[i-1]]
        => 空间优化
        dp[v]表示能否组成v
        """
        # # 1. 二维
        # n = len(nums)
        # total = sum(nums)
        # if total % 2 != 0:
        #     return False
        # total = total // 2
        # dp = [[False]*(total+1) for _ in range(n+1)]
        # dp[0][0] = True
        # for i in range(1, n+1):
        #     for v in range(1, total+1):
        #         dp[i][v] = dp[i-1][v]
        #         if v >= nums[i-1]:
        #             dp[i][v] = dp[i][v] or dp[i-1][v-nums[i-1]]
        # return dp[n][total]
                

        # 1. 空间优化
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        total = total // 2
        dp = [False]*(total+1)
        dp[0] = True
        for i in range(1, n+1):
            for v in range(total, 0, -1):
                if v >= nums[i-1]:
                    dp[v] = dp[v] or dp[v-nums[i-1]]
        return dp[total]
