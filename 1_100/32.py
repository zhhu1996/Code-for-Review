class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """最长有效括号
        1. dp
        dp[i]表示以位置i结尾的最长有效(格式正确且连续)括号长度, 状态转移方程如下:
        i.  s[i] = '(', dp[i] = 0
        ii. s[i] = ')'
            a) s[i-1] = '('
                dp[i] = dp[i-2] + 2
            b) s[i-1] = ')' && s[i-dp[i-1]-1] == '('
                dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        """
        if len(s) < 2:
            return 0
        n = len(s)
        dp = [0]*n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif s[i-1] == ')' and i-dp[i-1] >= 1 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0)
        return max(dp)