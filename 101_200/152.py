class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        max_dp[i]表示以i结尾的最大乘积子数组, min_dp[i]表示以i结尾的最小乘积子数组
        if nums[i] >= 0
        =>  max_dp[i] = max(max_dp[i-1]*nums[i], nums[i])
        =>  min_dp[i] = min(min_dp[i-1]*nums[i], nums[i])
        if nums[i] < 0
        =>  max_dp[i] = max(min_dp[i-1]*nums[i], nums[i])
        =>  min_dp[i] = min(max_dp[i-1]*nums[i], nums[i])
        """
        if not nums:
            return 0
        n = len(nums)
        max_dp = [x for x in nums]
        min_dp = [x for x in nums]
        for i in range(1, n):
            if nums[i] >= 0:
                max_dp[i] = max(max_dp[i-1]*nums[i], nums[i])
                min_dp[i] = min(min_dp[i-1]*nums[i], nums[i])
            else:
                max_dp[i] = max(min_dp[i-1]*nums[i], nums[i])
                min_dp[i] = min(max_dp[i-1]*nums[i], nums[i])
        return max(max_dp)

        
        # # dpMax[i]表示以第i个数结尾的最大乘积
        # # dpMin[i]表示以第i个数结尾的最小乘积
        # # 需要根据nums[i]的正负分情况讨论：
        # # i. nums[i] > 0
        # # 需要前一个乘积尽可能的大
        # # ii. nums[i] < 0
        # # 需要前一个乘积尽可能的小

        # # dpMax[i] = max(dpMax[i-1]*nums[i], dpMin[i-1]*nums[i], nums[i])
        # # dpMin[i] = min(dpMax[i-1]*nums[i], dpMin[i-1]*nums[i], nums[i])
        
        # if not nums:
        #     return 0

        # n = len(nums)
        # dpMax, dpMin = [nums[0]] * n, [nums[0]] * n
        # for i in range(1, n):
        #     dpMax[i] = max(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i], nums[i])
        #     dpMin[i] = min(dpMax[i - 1] * nums[i], dpMin[i - 1] * nums[i], nums[i])
        # return max(dpMax)

