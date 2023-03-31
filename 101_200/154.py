class Solution:
    def findMin(self, nums: List[int]) -> int:
        """寻找旋转排序数组中的最小值II
        1. 二分
        恢复二段性 + 二分查找
        """
        n = len(nums)
        l, r = 0, n-1
        while r > l and nums[l] == nums[-1]:
            l += 1
        while l <= r:
            mid = (l + r) // 2
            # f(l-1) > nums[-1], f(r+1) < nums[-1]
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]