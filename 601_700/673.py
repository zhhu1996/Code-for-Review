class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """最长递增子序列的个数
        1. dp
        带维度单串, 位置i必取, O(n)个子问题
        dp[i][0]: 以nums[i]结尾LIS长度
        dp[i][1]: 以nums[i]结尾LIS个数
        """
        n = len(nums)
        dp = [[1,1] for _ in range(n)]
        maxl = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
            if dp[i][0] > maxl:
                maxl = dp[i][0]
        res = 0
        for i in range(n):
            if dp[i][0] == maxl:
                res += dp[i][1]
        return res