class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """分割等和子集
        1. 背包问题，
        dp[i][j]表示[0，i]的区间内挑选子集是否能得到和为j
        状态转移方程为
        dp[i][j] = dp[i-1][j]
                   | dp[i-1][j-nums[i] if j>nums[i]
                   | True j == nums[i]

        2. 回溯
        只要找到一个组合使得组合之和=target即可
        """
        # # 方法1
        # n = len(nums)
        # total = sum(nums)
        # if total & 1 == 1:
        #     return False
        # target = total // 2 + 1
        # dp = [[False]*target for i in range(n)]
        # if nums[0] <= target:
        #     dp[0][nums[0]] = True
        # for i in range(n):
        #     for j in range(target):
        #         if j == nums[i]:
        #             dp[i][j] = True
        #             continue
        #         dp[i][j] = dp[i-1][j]
        #         if j > nums[i]:
        #             dp[i][j] = dp[i][j] or dp[i-1][j-nums[i]]
        # return dp[n-1][target-1]

        # 方法2, 超时，待优化
        self.result = False
        def getCandidate(array, index, nowSum, target):
            if nowSum > target:
                return
            if nowSum == target:
                self.result = True
                return
            for j in range(index, len(array)):
                getCandidate(array, j+1, nowSum+array[j], target)


        n = len(nums)
        total = sum(nums)
        if total & 1 == 1:
            return False
        target = total // 2
        nums.sort()
        getCandidate(nums, 0, 0, target)
        return self.result

