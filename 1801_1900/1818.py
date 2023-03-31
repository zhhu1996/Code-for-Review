class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        """绝对差值和
        1. 排序 + 二分, 时间复杂度O(nlogn)
        """
        n = len(nums1)
        diff = 0
        for i in range(n):
            diff += abs(nums1[i]-nums2[i])
        res = diff
        arr = list(sorted(nums1))
        for i in range(n): # 替换nums1[i]
            l, r = 0, n-1
            target = nums2[i]
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            # arr[l] >= target
            cand = diff - abs(nums1[i]-target)
            if l == n:
                cand += abs(arr[l-1]-target)
            elif l == 0:
                cand += abs(arr[l]-target)
            elif arr[l] == target:
                cand += 0
            else: # >
                cand = min(cand + abs(arr[l]-target), cand + abs(arr[l-1]-target))
            res = min(res, cand)
        return res % (10**9+7)