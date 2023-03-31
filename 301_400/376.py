class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """摆动序列
        1. 带维度单串dp, 位置i必取, O(n)个子问题, 时间复杂度O(n^2)
        dp[i][0]: 以nums[i]结尾, 最后一个差为负数的LS长度
        dp[i][1]: 以nums[i]结尾, 最后一个差为正数的LS长度

        2. 带维度单串dp, 位置i可不取, O(1)个子问题, 时间复杂度O(n)
        dp[i][0]: nums[0..i]上最后一个差为负数的LS长度
        dp[i][1]: nums[0..i]上最后一个差为正数的LS长度
        """
        # # 1.
        # n = len(nums)
        # dp = [[1]*2 for _ in range(n)]
        # max_l = 1
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i][1] = max(dp[i][1], dp[j][0]+1)
        #         elif nums[i] < nums[j]:
        #             dp[i][0] = max(dp[i][0], dp[j][1]+1)
        #     max_l = max(max_l, dp[i][0], dp[i][1])
        # return max_l

        # 2.
        n = len(nums)
        dp = [[1]*2 for _ in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i][0] = dp[i-1][0]
                # 证明: 设j为nums[0..i-1]最后一个下降元素, 分nums[j] >= nums[i-1], nums[j] < nums[i-1]讨论
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]+1)
            elif nums[i] < nums[i-1]:
                # 证明: 设j为nums[0..i-1]最后一个上升元素, 分nums[j] >= nums[i-1], nums[j] < nums[i-1]讨论
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+1) 
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        return max(dp[n-1])