class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        """转变数组后最接近目标值的数组和
        1. 二分, 时间复杂度O(nlogn)
        寻找和首次>=target的位置, 返回两边界l-1和l最接近target的
        """
        left, right = 0, max(arr)
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