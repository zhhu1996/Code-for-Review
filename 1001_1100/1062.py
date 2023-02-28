class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        """最长重复子串
        1. 暴力 + 集合
        子串长度范围为[1, Len-1], 从Len-1开始查找是否有重复子串
        2. dp
        单串, 位置i可不取, O(1)个子问题
        dp[i]: nums[0..i]的最长重复子串的长度
        dp[i+1] = dp[i]+1, if s[i-dp[i]+1:i+2] in s[:i]
        """
        ## 1.
        # n = len(s)
        # exist = set()
        # for lth in range(n-1, 0, -1):
        #     for l in range(n-lth+1):
        #         r = l + lth - 1
        #         if s[l:r+1] in exist:
        #             return lth
        #         else:
        #             exist.add(s[l:r+1])
        # return 0

        # 2.
        n = len(s)
        dp = [0]*n
        for i in range(1, n):
            dp[i] = dp[i-1]
            if i-dp[i-1] >= 0:
                target = s[i-dp[i-1]: i+1]
                if target in s[:i]:
                    dp[i] += 1
        return dp[n-1]