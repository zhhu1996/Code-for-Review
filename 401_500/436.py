class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """寻找右区间
        1. 排序 + 二分
        """
        n = len(intervals)
        arr = [(intervals[i][0], i) for i in range(n)]
        arr.sort()
        res = [-1]*n
        for i in range(n):
            target = intervals[i][1]
            l, r = 0, n-1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            if l < n:
                res[i] = arr[l][1]
        return res