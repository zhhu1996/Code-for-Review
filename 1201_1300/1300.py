class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # 第一个大于等于 target的值
        arr.sort()
        left, right = 0, arr[-1]
        while left < right:
            mid = (left + right) // 2
            tarr = [ x if x <= mid else mid for x in arr]
            if sum(tarr) < target:
                left = mid + 1
            else:
                right = mid
        l1, l2 = left-1, left
        ts1 = sum([x if x<=l1 else l1 for x in arr])
        ts2 = sum([x if x<=l2 else l2 for x in arr])
        if abs(ts1-target) <= abs(ts2-target):
            return l1
        else:
            return l2