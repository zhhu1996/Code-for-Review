class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """删掉一个元素以后全为 1 的最长子数组
        1. 变长滑动窗口
        """
        l, r, n = 0, 0, len(nums)
        zeros, res = 0, 0
        while r < n:
            if nums[r] == 0:
                if zeros == 0:
                    zeros += 1
                else:
                    while nums[l] > 0:
                        l += 1
                    l += 1
            res = max(res, r-l)
            r += 1
        return res