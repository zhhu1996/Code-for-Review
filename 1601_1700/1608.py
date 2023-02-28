class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        def gt_target(nums, target):
            cnt = 0
            for num in nums:
                if num >= target:
                    cnt += 1
            return cnt

        l, r = 0, len(nums)
        while l <= r:
            # f[l-1] >= x
            # f[r+1] <x
            mid = (l + r) // 2
            if gt_target(nums, mid) >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return l-1 if gt_target(nums, l-1) == l-1 else -1