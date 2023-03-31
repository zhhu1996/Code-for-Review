class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """判断子序列
        1. 双串dp, 位置i,j可不取, O(1)个子问题, 时间复杂度O(m*n)

        2. 双指针, 时间复杂度O(m+n)
        """
        m, n = len(s), len(t)
        dp = [[False]*(n+1) for _ in range(m+1)]
        # init
        for i in range(n+1):
            dp[0][i] = True
        # dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m][n]