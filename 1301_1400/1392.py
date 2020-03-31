class Solution:
    def longestPrefix(self, s: str) -> str:
        # 1. 超内存
        # strSet = set()
        # n = len(s)
        # maxStr, maxLen = '', 0
        # for i in range(n - 1):
        #     strSet.add(s[:i + 1])
        # for j in range(n - 1, 0, -1):
        #     if s[j:] in strSet:
        #         maxStr = s[j:]
        #         maxLen = len(maxStr)
        # return maxStr

        # 2. 通过
        n = len(s)
        maxStr = ''
        for i in range(n-1):
            if s[:i+1] == s[n-1-i:]:
                maxStr = s[:i+1]
        return maxStr

