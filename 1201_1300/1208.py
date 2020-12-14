class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """尽可能使字符串相等
        1. 滑动窗口法
        在满足cost条件下尽可能扩大窗口，否则右移i指针
        """
        if not s or not t or maxCost < 0:
            return 0
        i, j, n = 0, 0, len(s)
        localCost, maxLen = 0, 0
        while j < n:
            localCost += abs(ord(s[j]) - ord(t[j]))
            while localCost > maxCost:
                localCost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen
