from collections import defaultdict


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """最大连续1的个数II
        1. 滑动窗口
        historyMaxCount表示窗口内出现字符1的个数
        k = 1
        historyMaxCount + k >= j - i + 1的时候满足扩张条件；
        否则窗口进行收缩
        """
        if not nums:
            return 0
        table = defaultdict(int)
        historyMaxCount = 0
        maxLen = 0
        n = len(nums)
        i, j = 0, 0
        while j < n:
            table[nums[j]] += 1
            historyMaxCount = max(historyMaxCount, table[1])
            if historyMaxCount + 1 < j - i + 1:
                if table[nums[i]] == historyMaxCount:
                    historyMaxCount -= 1
                table[nums[i]] -= 1
                i += 1
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen

