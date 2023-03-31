class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """最长字符串链(LIS题型)
        1. dp, 时间复杂度O(n*nk)
        单串, 位置i必取, O(n)个子问题
        dp[i]表示以words[i]结尾的最长字符串链的长度
        => 优化, 时间复杂度O(n^2)
        dp[w]表示以w结尾的最长字符串链的长度
        """
        # # 1. 朴素dp
        # def is_valid(s1, s2):
        #     m, n = len(s1), len(s2)
        #     if m + 1 != n:
        #         return False
        #     i, j = 0, 0
        #     while i < m and j < n:
        #         if s1[i] == s2[j]:
        #             i += 1
        #         j += 1
        #     return i == m

        # # 1. 朴素dp
        # words.sort(key=lambda x: len(x))
        # n = len(words)
        # dp = [1]*n
        # for i in range(1, n):
        #     for j in range(i):
        #         if is_valid(words[j], words[i]):
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

        # 1. 优化
        words.sort(key=lambda x: len(x))
        dp = collections.defaultdict(int)
        res = 1
        for i in range(len(words)):
            w = words[i]
            for j in range(len(w)):
                pre = w[:j] + w[j+1:]
                dp[w] = max(dp[w], dp[pre]+1)
            res = max(res, dp[w])
        return res