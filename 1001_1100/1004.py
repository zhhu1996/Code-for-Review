from collections import defaultdict

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """最大连续1的人数III
        1. 滑动窗口
        historyMaxCount表示窗口内出现字符1的个数
        k = 1
        historyMaxCount + k >= j - i + 1的时候满足扩张条件；
        否则窗口进行收缩
        """
        if not A:
            return 0
        table = defaultdict(int)
        historyMaxCount = 0
        maxLen = 0
        n = len(A)
        i, j = 0, 0
        while j < n:
            table[A[j]] += 1
            historyMaxCount = max(historyMaxCount, table[1])
            if historyMaxCount + K < j - i + 1:
                if table[A[i]] == historyMaxCount:
                    historyMaxCount -= 1
                table[A[i]] -= 1
                i += 1
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen