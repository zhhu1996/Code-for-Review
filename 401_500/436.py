class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 排序+二分查找
        if len(intervals) <= 1:
            return [-1]
        pos = {}
        for x in enumerate(intervals):
            pos[tuple(x[1])] = x[0]
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [-1]*len(intervals)
        for i in range(len(intervals)):
            # 在剩余数组中寻找第一个大于等于target的元素
            target = intervals[i][1]
            index = pos[tuple(intervals[i])]
            left, right = 0, len(intervals)-1
            while left < right:
                mid = (left+right)//2
                if intervals[mid][0] < target:
                    left = mid+1
                else:
                    right = mid
            if intervals[left][0] < target:
                res[index] = -1
            else:
                res[index] = (pos[tuple(intervals[left])])
        return res