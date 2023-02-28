class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """戳气球
        1. 区间dp
        dp[i][j]表示[i..j]能获得的最大硬币数量, 位置i、j不取
        假设区间[i..j]上最后一个被戳破的气球是k, 那么存在
        dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        """
        nums.insert(0, 1)
        nums.insert(len(nums), 1)
        n = len(nums)

        dp = [[0 for i in range(n)] for j in range(n)]
        for lth in range(3, n+1):
            for i in range(0, n-lth+1):
                j = i + lth - 1
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        return dp[0][n-1]