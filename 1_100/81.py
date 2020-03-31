class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # mid 在左边有序部分
            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]: # 边界点处理
                    r = mid - 1
                else:
                    l = mid + 1
            # mid 在右边有序部分
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # 不确定在左边有序部分还是右边有序部分
            else:
                r -= 1

        return False