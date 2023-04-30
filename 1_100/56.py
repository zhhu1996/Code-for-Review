class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """合并区间
        1. 排序 + 合并
        """
        intervals.sort(key=lambda x: x[0])
        ans = []
        for i in range(len(intervals)):
            if not ans or ans[-1][-1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][-1] = max(ans[-1][-1], intervals[i][1])
        return ans