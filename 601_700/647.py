class Solution:
    def countSubstrings(self, s: str) -> int:
        """回文子串
        1. 区间dp
        i.  s[i] = s[j]
        d[i][j] = dp[i+1][j-1]
        ii. s[i] != s[j]
        dp[i][j] = 0
        """
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        res = 0
        for lth in range(1, n+1):
            for l in range(0, n-lth+1):
                r = l + lth - 1
                if lth <= 2:
                    dp[l][r] = True if s[l] == s[r] else False
                else:
                    if s[l] == s[r]:
                        dp[l][r] = dp[l+1][r-1]
                    else:
                        dp[l][r] = False
                if dp[l][r]:
                    res += 1
        return res