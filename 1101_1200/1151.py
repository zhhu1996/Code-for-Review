class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """最少交换次数来组合所有的 1
        1. 滑动窗口
        窗口扩大的条件：j-i+1 < count(1)
        窗口缩小：i++
        最少交换次数=count(1)-窗口内1的个数
        """
        if not data:
            return 0
        n = len(data)
        i, j, swapCount = 0, 0, n
        localCount = 0
        totalCount = sum(data)
        while j < n:
            if j - i + 1 > totalCount:
                if data[i] == 1:
                    localCount -= 1
                i += 1
            if data[j] == 1:
                localCount += 1
            swapCount = min(swapCount, totalCount - localCount)
            j += 1
        return swapCount
