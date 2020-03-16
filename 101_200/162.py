class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # # 1. 暴力，时间复杂度O(n)
        # for i in range(0, len(nums)-1): # [0, len-2]
        #     if nums[i] > nums[i+1]:
        #         return i
        # return len(nums)-1

        # 2. 二分查找
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
