class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 在Q33基础上增加关于相等的判断
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]: # mid在后半段数组
                # [mid, right]是有序的
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right]: # mid在前半段数组
                # [left, mid]是有序的
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[right] == target:
                    return True
                right -= 1

        return nums[left] == target