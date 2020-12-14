class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """可获得的最大点数
        1. 递归回溯，时间复杂度O(2^n)
        每次拿开头或者末尾的值，直到拿k个元素，保留所有的和，选择最大的

        2. 题目中求解两边k个值的最大值 => 求包含n-k个元素的连续子数组和的最小值
        即用滑动窗口求连续子数组和的最小值
        """
        # 方法1
        # self.maxScore = 0
        # def getCandidate(array, start, end, index, nowSum, K):
        #     if index == K:
        #         self.maxScore = max(nowSum, self.maxScore)
        #         return
        #     if start <= len(array)-1:
        #         getCandidate(array, start+1, end, index+1, nowSum+array[start], K)
        #     if end >= 1:
        #         getCandidate(array, start, end-1, index+1, nowSum+array[end], K)
        # getCandidate(cardPoints, 0, len(cardPoints)-1, 0, 0, k)
        # return self.maxScore

        # 方法2
        if not cardPoints or k <= 0:
            return 0
        n = len(cardPoints)
        i, j = 0, 0
        nowSum = 0
        totalSum = sum(cardPoints)
        minSum = float("inf")
        if n == k:
            return totalSum
        while j < n:
            nowSum += cardPoints[j]
            if j - i + 1 >= n - k:
                minSum = min(minSum, nowSum)
                nowSum -= cardPoints[i]
                i += 1
            j += 1
        return totalSum - minSum




