class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # # 1. 暴力
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         begin = i
        #         end = i
        #         for j in range(i+1, len(nums)):
        #             if nums[j] == target:
        #                 end = j
        #         return [begin, end]
        # return [-1, -1]

        # # 2. 二分查找，先查找target的值，然后再左右延伸得到区间

        # 两次二分查找
        # 对左边界的查找
        l, r = 0, len(nums)
        li, ri = -1, -1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if l != len(nums) and nums[l] == target:
            li = l
        # 对右边界的查找
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                l = mid + 1
        if l != 0 and nums[l - 1] == target:
            ri = l - 1
        return li, ri