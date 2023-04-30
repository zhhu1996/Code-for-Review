class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """在排序数组中查找元素的第一个和最后一个位置
        1. 二分
        >=target的第一个位置; >=(target+1)的第一个位置
        """
        def binary_search(nums, target):
            # [l, r]
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        first = binary_search(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        second = binary_search(nums, target+1) -1
        return [first, second]