class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """K 个不同整数的子数组
        1. 变长滑动窗口
        K个不同整数的子数组个数 = (<=k个不同整数的子数组个数) - (<=k-1个不同整数的子数组个数)
        """
        def bounded_target(target):
            from collections import defaultdict
            l, r, res, n = 0, 0, 0, len(nums)
            w_map = defaultdict(int)
            matches = 0
            while r < n:
                w_map[nums[r]] += 1
                if w_map[nums[r]] == 1:
                    matches += 1
                while matches > target:
                    w_map[nums[l]] -= 1
                    if w_map[nums[l]] == 0:
                        matches -= 1
                    l += 1
                res += r-l+1
                r += 1
            return res

        return bounded_target(k) - bounded_target(k-1)