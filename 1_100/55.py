class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # 1. 回溯，每到一个节点递归遍历所有的状态，时间复杂度O(2^n)，超时
        # self.res = -1
        #
        # def jump(nums, index):
        #     if index >= len(nums) - 1:
        #         self.res = index
        #         return
        #     if nums[index] == 0:
        #         return
        #     for j in range(1, nums[index] + 1):
        #         jump(nums, index + j)
        #
        # jump(nums, 0)
        # return self.res >= len(nums) - 1

        # # 2. dp，对于某个索引i，对于[0, i-1]的值，如果nums[j] + j >= i则表示能够到达索引i，最好时间复杂度O(n)，最差时间复杂度O(n^2)
        # n = len(nums)
        # dp = [False]*n
        # dp[0] = True
        # for i in range(1, n):
        #     # 从最后一个开始查找
        #     for j in range(i-1, -1, -1):
        #         if dp[j] and nums[j] + j >= i:
        #             dp[i] = True
        #             break
        # return dp[-1]

        # 3. 贪心，时间复杂度O(n)
        lastPos = len(nums) - 1
        for j in range(len(nums) - 1, -1, -1):
            if j + nums[j] >= lastPos:
                lastPos = j
        return lastPos == 0
