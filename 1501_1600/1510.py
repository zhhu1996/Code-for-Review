class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """石子游戏 IV
        1. dp
        单串dp, 位置i必取, O(n)个子问题, 时间复杂度O(n*sqrt(n))
        """
        dp = [False]*(n+1)
        dp[0], dp[1] = False, True
        for i in range(2, n+1):
            j = 1
            while j*j <= i:
                if not dp[i-j*j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]