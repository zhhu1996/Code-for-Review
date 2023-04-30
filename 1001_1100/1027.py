class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """最长等差数列
        1. dp
        dp[i][k]: 以nums[i]结尾的差为k的最长序列长度
        """
        n = len(nums)
        dp = defaultdict(dict)
        dp[0][0] = 1
        ans = 1
        for i in range(1, n):
            for j in range(i):
                d = nums[i]-nums[j]
                if d not in dp[i]:
                    dp[i][d] = 2
                if d in dp[j]:
                    dp[i][d] = max(dp[i][d], dp[j][d]+1)
                ans = max(ans, dp[i][d])
        return ans