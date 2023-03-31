class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        """超过1次操作后的最大子数组和
        1. dp
        带维度dp, 位置i必取, O(1)个子问题
        dp[i][0]: 以nums[i]结尾, 使用0次trick的最大子数组和
        dp[i][1]: 以nums[i]结尾, 使用1次trick的最大子数组和
        """
        n = len(nums)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0], dp[0][1] = nums[0], nums[0]*nums[0]
        res = max(dp[0])
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0]+nums[i], nums[i])
            dp[i][1] = max(dp[i-1][1]+nums[i], dp[i-1][0]+nums[i]*nums[i], nums[i]*nums[i])
            res = max(res, dp[i][0], dp[i][1])
        return res