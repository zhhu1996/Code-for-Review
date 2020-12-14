class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """定长子串中元音的最大数目
        1. 滑动窗口
        """
        if not s or k <= 0:
            return 0
        i, j = 0, 0
        n = len(s)
        localCnt, maxCnt = 0, 0
        targets = "aoeiu"
        while j < n:
            if s[j] in targets:
                localCnt += 1
                maxCnt = max(localCnt, maxCnt)
            if j - i + 1 == k:
                if s[i] in targets:
                    localCnt -= 1
                i += 1
            j += 1
        return maxCnt
