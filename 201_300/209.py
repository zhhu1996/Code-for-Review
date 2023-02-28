class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """长度最小的子数组
        1. 变长滑动窗口
        """
        l, r, n = 0, 0, len(nums)
        cur, res = 0, float('inf')
        while r < n:
            cur += nums[r]
            while cur >= target:
                res = min(res, r-l+1)
                cur = cur - nums[l]
                l += 1
            r += 1
        return res if res <= n else 0