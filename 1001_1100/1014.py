class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """最佳观光组合
        dp[i]: i作为观光点(j)的最大收益
        i. i-1, i同作为右端点j
            dp[i] = dp[i-1] + (nums[i]-nums[i-1]-1)
        ii. i-1,i组合
            dp[i] = nums[i]+nums[j-1]-1
        dp[i] = max(dp[i-1] + (nums[i]-nums[i-1]-1), nums[i]+nums[j-1]-1)
        """
        n = len(values)
        if n < 2: return 0
        dp = [0]*n
        dp[0], dp[1] = 0, values[0]+values[1]-1
        for i in range(2, n):
            cand1 = dp[i-1] + values[i]-values[i-1]-1
            cand2 = values[i]+values[i-1]-1
            dp[i] = max(cand1, cand2)
        return max(dp)