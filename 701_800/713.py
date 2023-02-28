class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """乘积小于k的子数组
        1. 变长滑动窗口
        """
        if k in [0, 1]:
            return 0
        l, r, n = 0, 0, len(nums)
        res = 0
        w_prod = 1
        while r < n:
            w_prod *= nums[r]
            while w_prod >= k:
                w_prod = w_prod // nums[l]
                l += 1
            res += r-l+1
            r += 1
        return res