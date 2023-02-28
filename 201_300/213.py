class Solution:
    def rob(self, nums: List[int]) -> int:
        """打家劫舍II
        单串, 位置i可不取, O(1)个子问题
        i. 偷窃第一间房子, nums[:-1]的最大收益
        ii. 不偷窃第一间房子, nums[1:]的最大收益
        求两者的最大值
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        dp1 = [0] * (n-1)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        dp2 = [0] * n
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])
        for i in range(3, n):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
        return max(dp1[n-2], dp2[n-1])