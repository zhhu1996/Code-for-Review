class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """两个字符串的最小ASCII删除和
        1. dp
        双串dp, 位置i,j可不取, O(1)个子问题
        dp[i][j]表示s1的前i个字符与s2的前j个字符的最小删除和
        => 也可以转化成LCS问题
        """
        m, n = len(s1), len(s2)
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        # init
        dp[0][0] = 0
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        # dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]), dp[i-1][j-1]+ord(s1[i-1])+ord(s2[j-1]))
        return dp[m][n]