class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """最小窗口子序列
        1. dp
        双串, i可不取, O(1)个子问题
        dp[i][j]: s1的前i个字符包含s2的前j个字符的最近起点, -1则表示不包含

        2. 滑动窗口
        i. 扩大窗口, 使得s2与s1完全匹配
        ii. 缩小窗口, 找到满足要求的最小窗口
        """
        # # 1.
        # m, n = len(s1), len(s2)
        # dp = [[-1]*(n+1) for i in range(m+1)]
        # min_w, min_s = float('inf'), ''
        # # init
        # for i in range(m+1):
        #     dp[i][0] = i
        # # dp
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if s1[i-1] == s2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        #     if dp[i][n] >= 0 and i-dp[i][n] < min_w:
        #         min_w = i - dp[i][n]
        #         min_s = s1[dp[i][n]: i]
        # return min_s

        # 2.
        m, n, min_w, min_s = len(s1), len(s2), float('inf'), ''
        i, j = 0, 0
        while i < m:
            if s1[i] == s2[j]:
                j += 1
            if j == n: # s[..i]已经包含s2, 右边界已确定
                right = i
                j -= 1
                while j >= 0: # 寻找左边界
                    if s2[j] == s1[i]:
                        j -= 1
                    i -= 1
                i += 1
                left = i
                if right - left + 1 < min_w: # 更新最小窗口
                    min_s = s1[left: right+1]
                    min_w = right - left + 1
                j = 0
            i += 1
        return min_s