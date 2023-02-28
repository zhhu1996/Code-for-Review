class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """通配符匹配
        1. dp
        dp[i][j]表示p[..i]和s[..j]是否匹配, 位置i,j必须取
        i.  p[i] = s[j] or p[i] = '?'
        dp[i][j] = dp[i-1][j-1]
        ii. p[i] = '*'
        dp[i][j] = dp[i-1][j] || dp[i-1][j-1] || dp[i][j-1]
                  (匹配0次)       (匹配1次)        (匹配>1次)
        iii. else
        dp[i][j] = False
        """
        m, n = len(s), len(p)
        dp = [[False for i in range(m+1)] for j in range(n+1)]
        # init
        dp[0][0] = True     # p = ''
        for i in range(n):  # s = ''
            if p[i] == '*':
                dp[i+1][0] = True
            else:
                break
        # dp
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-1] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[n][m]