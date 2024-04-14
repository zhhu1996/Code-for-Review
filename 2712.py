class Solution:
    def minimumCost(self, s: str) -> int:
        """使所有字符相等的最小成本
        1. 贪心
        为使所有字符相等, 需要消除所有的相邻不等对, 消除顺序不影响结果
        """
        ans, n = 0, len(s)
        for i in range(n-1):
            if s[i] != s[i+1]:
                ans += min(i+1, n-i-1)
        return ans