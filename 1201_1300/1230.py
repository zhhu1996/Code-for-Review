class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """抛掷硬币
        1. dp, 带维度单串问题
        dp[i][k]表示以硬币i结尾的实验中, 正面朝上次数等于k次的概率
        dp[i][k] = prob[i]*dp[i-1][k-1] + (1-prob[i])*dp[i-1][k]
        """
        if not prob:
            return 0
        n = len(prob)
        dp = [[0 for i in range(n+1)] for j in range(n)]
        dp[0][0] = 1-prob[0]
        dp[0][1] = prob[0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]*(1-prob[i])
            for k in range(1, i+2):
                dp[i][k] = prob[i]*dp[i-1][k-1] + (1-prob[i])*dp[i-1][k]
        return dp[n-1][target]