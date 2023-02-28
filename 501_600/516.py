class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """最长回文子序列
        1. 区间dp
        dp[i][j]定义为s[i..j]上的最长回文子序列长度
        i. s[i] = s[j]
        dp[i][j] = dp[i+1][j-1] + 2
        ii.s[i] != s[j]
        dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        2. 将s反转成rs, 即可转换成线性dp, 也就是求s与rs的最长公共子序列
        """
        ## 1.区间dp
        """
        \   \\  \\\
            \   \\
                \  
        """
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for lth in range(1, n+1):
            for l in range(0, n-lth+1):
                r = l + lth - 1
                if lth == 1:
                    dp[l][r] = 1
                    continue
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l][r-1], dp[l+1][r])
        return dp[0][n-1]

        ## 2.
        # rs = list(reversed(s))
        # n = len(s)
        # dp = [[0]*(n+1) for i in range(n+1)]
        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         if s[i-1] == rs[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # return dp[n][n]
