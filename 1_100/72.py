class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """编辑距离
        dp[i][j]表示word1[..i]转换成word2[..j]的最少操作数
        i.  word1[i] = word2[j]
        dp[i][j] = dp[i-1][j-1]
        ii. word1[i] != word2[j]
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
        """
        m, n = len(word1), len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # init
        for i in range(n+1):
            dp[0][i] = i
        for j in range(m+1):
            dp[j][0] = j
        # dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[m][n]