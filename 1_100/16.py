class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 双指针法, 时间复杂度为O(n^2)
        nums.sort()
        delta = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if abs(delta) > abs(nums[i] + nums[L] + nums[R] - target):
                    delta = nums[i] + nums[L] + nums[R] - target
                if nums[i] + nums[L] + nums[R] > target:
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < target:
                    L += 1
                else:
                    return target

        return target + delta