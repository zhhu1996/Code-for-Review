class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """验证回文字符串III
        1. dp
        最长回文子序列 >= n-k 即满足条件
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        ans = 0
        for lth in range(1, n+1):
            for l in range(n-lth+1):
                r = l + lth - 1
                if l == r:
                    dp[l][r] = 1
                    continue
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l+1][r-1]
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
                ans = max(ans, dp[l][r])
        return ans >= n-k