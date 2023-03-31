class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """乘积为正数的最长子数组长度
        1. dp
        带维度单串, 位置i必取, O(1)个子问题
        dp[i][0]: 以nums[i]结尾的乘积为负数的最长子数组长度
        dp[i][1]: 以nums[i]结尾的乘积为正数的最长子数组长度
        """
        n = len(nums)
        dp = [[0,0] for _ in range(n)]
        if nums[0] > 0:
            dp[0][0], dp[0][1] = 0, 1
        elif nums[0] == 0:
            dp[0][0], dp[0][1] = 0, 0
        else:
            dp[0][0], dp[0][1] = 1, 0
        res = dp[0][1]
        for i in range(1, n):
            if nums[i] > 0:
                dp[i][0] = (1+dp[i-1][0] if dp[i-1][0]>0 else 0)
                dp[i][1] = 1+dp[i-1][1]
            elif nums[i] == 0:
                dp[i][0], dp[i][1] = 0, 0
            else:
                dp[i][0] = 1+dp[i-1][1]
                dp[i][1] = (1+dp[i-1][0] if dp[i-1][0]>0 else 0)
            res = max(res, dp[i][1])
        return res