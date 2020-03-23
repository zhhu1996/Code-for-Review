# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # 1. 先对列表按照第一个坐标进行排序，然后根据是否相交进行合并
        if not intervals:
            return []

        # 根据第一个坐标升序排列
        intervals.sort(key=lambda x: x[0])
        res = []
        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(1, len(intervals)):
            if e < intervals[i][0]:  # 不相交: a[1] < b[0]
                res.append([s, e])
                s = intervals[i][0]
                e = intervals[i][1]
            else:  # 相交: a[1] >= b[0]，将e更新为较大的坐标
                e = max(e, intervals[i][1])
        # 添加区间
        res.append([s, e])

        return res