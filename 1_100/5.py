class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1. 暴力解，超时了

        # # 2. dp，f[i][j]表示从i到j的子串是否是回文子串
        # # 当j - i <= 1 时，如果s[i] == s[j], 那么f[i][j] = 1，否则赋值0
        # # 当j - i >= 1 时，如果s[i] == s[j]并且f[i+1][j-1] = 1，那么f[i][j] = 1
        # # 注意外层循环是j，内层循环是i，每次给[i, j]的序列赋值，这样递推能保证逐个计算；时间复杂度O(n^2)，空间复杂度O(n^2)
        # k = len(s)
        # dp = [[0] * k for i in range(k)]
        # maxStr = ''
        # for i in range(k):
        #     dp[i][i] = 1
        # for j in range(k):
        #     for i in range(j + 1):
        #         if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1] == 1):
        #             dp[i][j] = 1
        #             if j - i + 1 > len(maxStr):
        #                 maxStr = s[i: j + 1]
        #
        # return maxStr

        # 3. 中心扩展法, 有2n-1个扩展中心，所以时间复杂度为O(n^2)，空间复杂度O(1)
        def calcSubStringLength(l, r, s):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return r - l - 1

        start, end = 0, 0
        for i in range(0, len(s)):
            lenA = calcSubStringLength(i, i, s)
            lenB = calcSubStringLength(i, i+1, s)
            maxLen = max(lenA, lenB)
            if maxLen > end - start + 1:
                start = i - (maxLen - 1) // 2
                end = i + maxLen // 2

        return s[start: end+1]