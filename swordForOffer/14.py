class Solution:
    def cuttingRope(self, n: int) -> int:
        """贪心
        当n>=5的时候：优先切3
            2*(n-2) > n
            3*(n-3) > n
            3*(n-3) > 2*(n-2)
        特殊情况：n=4,3,2,1
        注意m>1的条件
        """

        f = [0, 0, 1, 2, 4]
        if n < 5:
            return f[n]

        maxLen = 1
        while n >= 5:
            n -= 3
            maxLen *= 3
        maxLen *= n
        return maxLen % 1000000007
