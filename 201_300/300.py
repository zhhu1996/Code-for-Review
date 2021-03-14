class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i]表示以i结尾的最长子序列的长度
        dp[i] = max(dp[j]+1), j < i and a[i]>a[j]
        """
        if not nums:
            return 0
        dp = [1]
        for i in range(1, len(nums)):
            result = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    result = max(dp[j]+1, result)
            dp.append(result)
        return max(dp)