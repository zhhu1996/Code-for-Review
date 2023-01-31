class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i]表示nums[:i]可取得的最大收益
        位置i有条件选取, 状态转移方程为
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]