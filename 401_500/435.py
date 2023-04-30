class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """无重叠区间
        1. dp (LIS问题的变形), 时间复杂度O(n^2)
        单串, 位置i必取, O(n)个子问题

        2. 排序 + 贪心, 时间复杂度O(n)
        按照左端点排序, 实时维护无重叠区间的最大右端点值
        """
        # # 1.
        # intervals.sort(key=lambda x: x[0])
        # n = len(intervals)
        # dp = [1] * n
        # ans = 1
        # for i in range(1, n):
        #     for j in range(i):
        #         if intervals[i][0] >= intervals[j][1]:
        #             dp[i] = max(dp[i], dp[j]+1)
        #     ans = max(ans, dp[i])
        # return n - ans

        
        # 2.
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        if n < 1: return 0
        ans = 0
        end = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < end:
                ans += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        return ans