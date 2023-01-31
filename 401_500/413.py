class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """等差数列划分
        1. 暴力, 时间复杂度O(n^2)
        求每个位置i结尾的等差数组个数, 汇总即可  

        2. dp, 时间复杂度O(n)
        dp[i]表示以位置i结尾的等差数组个数
        i.  nums[i] - nums[i-1] = nums[i-1] - nums[i-2]
            dp[i] = dp[i-1] + 1  
        ii. dp[i] = 0     
        """
        # if len(nums) <= 2:
        #     return 0
        # res = 0
        # for i in range(2, len(nums)):
        #     diff = nums[i] - nums[i-1]
        #     j = i - 2
        #     cur = 0
        #     while j >= 0:
        #         if nums[j+1] - nums[j] == diff:
        #             j -= 1
        #             cur += 1
        #         else:
        #             break
        #     res += cur
        # return res

        if len(nums) <= 2:
            return 0
        n = len(nums)
        dp = [0]*n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)