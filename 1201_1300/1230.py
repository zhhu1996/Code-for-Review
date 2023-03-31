class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """抛掷硬币
        1. dp
        带维度单串, 位置i可不取, O(1)个子问题
        dp[i][j]: 前i次实验有j枚硬币向上的概率
        dp[i][j] = dp[i-1][j-1]*prob[i-1] + dp[i-1][j]*(1-prob[i-1])
        """
        n = len(prob)
        if target > n:
            return 0
        dp = [[0]*(1+n) for _ in range(1+n)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(i+1):
                if j == 0:
                    dp[i][0] = dp[i-1][0] * (1-prob[i-1])
                else:
                    dp[i][j] = dp[i-1][j-1]*prob[i-1] + dp[i-1][j]*(1-prob[i-1])
        return dp[n][target]