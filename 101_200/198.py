class Solution:
    def rob(self, nums: List[int]) -> int:
        """打家劫舍
        单串, 位置i可不取, O(1)个子问题
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return max(dp)
