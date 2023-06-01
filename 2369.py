class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        """检查数组是否存在有效划分
        1. dp
        单串, 位置i必取, O(1)个子问题
        """
        n = len(nums)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(2, n+1):
            if i == 2:
                dp[i] = (True if nums[i-1] == nums[i-2] else False)
            else:
                if dp[i-2] and nums[i-1] == nums[i-2]:
                    dp[i] = True
                if dp[i-3] and nums[i-1] == nums[i-2] and nums[i-1] == nums[i-3]:
                    dp[i] = True
                if dp[i-3] and nums[i-1] == nums[i-2]+1 and nums[i-1] == nums[i-3]+2:
                    dp[i] = True
        return dp[n]