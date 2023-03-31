class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """有序数组中的单一元素
        1. 二分
        构造函数, 满足二分性
        """
        n = len(nums)
        l, r = 0, n-1

        def check(x):
            if x-1 >= 0 and nums[x] == nums[x-1]:
                return True if (x+1) % 2 == 0 else False
            if x+1 < len(nums) and nums[x] == nums[x+1]:
                return True if (x+2) % 2 == 0 else False

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]