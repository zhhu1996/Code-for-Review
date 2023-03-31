class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """最大连续1的个数II
        1. dp, 时间复杂度O(n)
        单串dp, 位置i必取, O(n)个子问题(记录上一个出现的0可优化为O(1)个子问题)

        2. 滑动窗口
        变长滑动窗口, 控制窗口内0的个数<=1
        """
        # 1. 
        n = len(nums)
        dp = [1]*n
        last_o = (0 if nums[0]==0 else -1)
        for i in range(1, n):
            if nums[i] == 1:
                dp[i] = dp[i-1] + 1 
            else:
                dp[i] = i-last_o
                last_o = i
        return max(dp)

        # # 2.
        # zeros = 0
        # i, j = 0, 0
        # res = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         if zeros == 0:
        #             zeros += 1
        #         else:
        #             while nums[j] != 0:
        #                 j += 1
        #             j += 1
        #     res = max(res, i-j+1)
        #     i += 1
        # return res