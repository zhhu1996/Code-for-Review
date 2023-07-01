class Solution:
    def maxRepOpt1(self, text: str) -> int:
        """单字符重复子串的最大长度
        1. 变长滑动窗口, 时间复杂度O(n)
        i - 起点
        j - [i, j-1]均相同
        k - [j+1, k-1]均等于text[i]
        """
        cnt = Counter(text)
        i, n = 0, len(text)
        ans = 1
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            l = j - i
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            r = k - (j+1)
            ans = max(ans, min(l+r+1, cnt[text[i]]))
            i = j
        return ans