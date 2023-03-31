class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            # f(l-1)>nums[-1], f(r+1)<=nums[-1]
            if nums[mid] <= nums[-1]:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l] if l < len(nums) else nums[-1]