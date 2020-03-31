class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划题：f[n] = f[n-1] + f[n-2]
        f = [0, 1, 2]
        for i in range(3, n + 1):
            f.append(f[i - 1] + f[i - 2])

        return f[n]