class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """在排序数组中查找数字
        1. 直接遍历，时间复杂度O(n)

        2. 二分查找第一个target和最后一个target出现的位置，时间复杂度O(logn)
        """

        def getFirstTarget(nums, length, start, end, target):
            if not nums:
                return -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    if mid > 0 and nums[mid] == nums[mid - 1]:
                        end = mid - 1
                    else:
                        return mid

        def getLastTarget(nums, length, start, end, target):
            if not nums:
                return -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    if mid < length - 1 and nums[mid] == nums[mid + 1]:
                        start = mid + 1
                    else:
                        return mid

        if target not in nums:
            return 0
        first = getFirstTarget(nums, len(nums), 0, len(nums)-1, target)
        last = getLastTarget(nums, len(nums), 0, len(nums)-1, target)
        return last - first + 1
