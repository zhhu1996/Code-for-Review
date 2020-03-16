class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. 暴力

        #         # 2. 二分查找，先遍历找到分割点，然后在各自的序列中做二分查找
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # 二分查找分界点
        def find_rotate_index(nums):
            if nums[0] < nums[-1]:
                return 0
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1

        rotate_index = find_rotate_index(nums)
        if nums[rotate_index] == target:  # 加速
            return rotate_index
        if rotate_index == 0:  # 情况1，直接对全部序列进行二分
            l, r = 0, len(nums) - 1
        elif target >= nums[0]:  # 情况2，对左侧序列进行二分
            l, r = 0, rotate_index - 1
        else:  # 情况3，对右侧序列进行二分
            l, r = rotate_index, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1
