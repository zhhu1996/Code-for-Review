class Solution:
    def numSquares(self, n: int) -> int:
        """完全平方数
        1. 完全背包 + 二分, 时间复杂度O(nlogn)
        dp[v]: 和为v的完全平方数的最少数量
        """
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        sq_nums = []
        k = 1
        while k*k <= 10**4:
            sq_nums.append(k*k)
            k += 1
        for i in range(1, n+1):
            target = i
            l, r = 0, len(sq_nums)-1
            while l <= r:
                mid = (l + r) // 2
                if sq_nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            for k in range(l):
                dp[i] = min(dp[i-sq_nums[k]]+1, dp[i])

        return dp[n]