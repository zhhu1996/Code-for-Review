class Solution:
    def tribonacci(self, n: int) -> int:
        """第 N 个泰波那契数"""
        t = [0, 1, 1]
        if n <= 2:
            return t[n]
        for i in range(3, n + 1):
            t.append(t[-3] + t[-2] + t[-1])
        return t[n]
