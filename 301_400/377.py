class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """组合总和IV
        1. 回溯法，当target很大时，超时

        2. 动态规划，dp[i]表示和为i的组合总数
        dp[i] = sum(dp[i-j]), i >= j and j属于nums
        """
        # self.result = []
        #
        # def getCandidate(array, target, nowSum, path):
        #     if nowSum > target:
        #         return
        #     if nowSum == target:
        #         print(path)
        #         self.result.append(path.copy())
        #         return
        #     for j in range(len(array)):
        #         path.append(array[j])
        #         getCandidate(array, target, nowSum+array[j], path)
        #         path.pop()
        #
        # getCandidate(nums, target, 0, [])
        #
        # return len(self.result)

        size = len(nums)
        if size == 0 or target <= 0:
            return 0

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(size):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]