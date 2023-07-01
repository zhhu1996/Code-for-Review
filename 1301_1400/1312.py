class Solution:
    def minInsertions(self, s: str) -> int:
        """让字符串成为回文串的最少插入次数
        1. dp
        区间dp, O(1)个子问题
        """
        n = len(s)
        dp = [[float('inf')]*n for _ in range(n)]
        for lth in range(1, n+1):
            for l in range(n-lth+1):
                r = l+lth-1
                if r == l:
                    dp[l][r] = 0
                elif r == l + 1:
                    dp[l][r] = 0 if s[l] == s[r] else 1
                else:
                    if s[l] == s[r]:
                        dp[l][r] = dp[l+1][r-1]
                    else:
                        dp[l][r] = min(dp[l][r-1], dp[l+1][r])+1
        return dp[0][n-1]