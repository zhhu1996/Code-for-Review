class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """安排工作以达到最大收益
        1. 贪心 + 二分
        """
        n = len(difficulty)
        arr = [(difficulty[i], profit[i]) for i in range(n)]
        arr.sort()
        dp = [0]*n
        dp[0] = arr[0][1]
        for i in range(1, n):
            dp[i] = max(dp[i-1], arr[i][1])
        res = 0
        for w in worker:
            target = w
            # 搜索<=target的最后一个位置
            l, r = 0, n-1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][0] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            if l > 0:
                res += dp[l-1]
        return res