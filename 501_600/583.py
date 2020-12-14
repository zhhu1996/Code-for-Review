class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """两个字符串的删除操作
        1. 求出两个字符串的最长公共子序列，删除操作数为len1 + len2 - 2*len(LCS)
        如何求两个字符串的最长公共子序列？动态规划
        dp[i][j]表示word1[0:i]与word2[0:i]的最长公共子序列长度
        那么状态转移为:
        if word1[i] == word2[j]: dp[i][j] = dp[i-1][j-1]
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        2. 直接用dp计算删除次数
        dp[i][j]表示使得word1[0:i]与word2[0:j]相同所需要的最少次数
        那么状态转移为
        if word1[i] == word2[j]: dp[i][j] = dp[i-1][j-1]
        else: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        注意与方法1的初始化是不同的
        """
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n1 + n2 - 2* dp[n1][n2]