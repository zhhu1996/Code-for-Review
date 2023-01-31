class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        """最大平均值和的分组
        1. 前缀和+dp, 时间复杂度O(n^3)
        带维度的单串问题, 维度为k表示个数, dp[i][j]表示以i结尾的数组划分为j个子数组的最大平均值之和
        i.  前缀和
        cumsum[i]表示nums[:i]的和, 快速求解连续子数组的和
        ii. dp
        dp[i][j] = max(dp[m][j-1] + avg(nums[m+1..])), 0<=m<i
        """
        if not nums or k <= 0:
            return 0
        # 前缀和
        n = len(nums)
        cumsum = [0] * n
        cumsum[0] = nums[0]
        for i in range(1, n):
            cumsum[i] = cumsum[i-1] + nums[i]
        # dp
        dp = [[0 for i in range(k+1)] for j in range(n)]
        for i in range(n):
            dp[i][1] = cumsum[i] / (i+1)
            for j in range(2, k+1):
                for m in range(i):
                    dp[i][j] = max(dp[i][j], dp[m][j-1]+(cumsum[i]-cumsum[m])/(i-m))
        return dp[n-1][k]