class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # 1. 滑动窗口
        n = len(grumpy)
        res1, res2, window = 0, 0, 0
        for i in range(n):
            if not grumpy[i]:
                res1 += customers[i]
            else:
                window += customers[i]
            if i >= X and grumpy[i-X] == 1:
                window -= customers[i-X]
            res2 = max(res2, window)
        return res1 + res2

