class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """区间子数组个数
        1. 滑动窗口
        利用滑动窗口法求最大元素<=x的子数组个数
        """
        def bounded_target(target):
            # nums[l:r]存储的元素均小于等于target
            l, r, n = 0, 0, len(nums)
            res = 0
            while r < n:
                if nums[r] > target:
                    l = r + 1
                else:
                    res += r-l+1
                r += 1
            return res

        return bounded_target(right) - bounded_target(left-1)