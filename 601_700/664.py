class Solution:
    def strangePrinter(self, s: str) -> int:
        """奇怪的打印机
        1. 区间dp
        i. 只打印i位置
        dp[i][j] = 1 + dp[i+1][j]
        ii. 打印[i..k]位置, s[i]=s[k]
        dp[i][j] = dp[i][k-1] + dp[i+1][j]
        """
        n = len(s)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for lth in range(1, n+1):
            for i in range(0, n-lth+1):
                j = i + lth - 1
                dp[i][j] = dp[i+1][j] + 1
                for k in range(i+1, j+1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k-1]+dp[k+1][j])
        return dp[0][n-1]