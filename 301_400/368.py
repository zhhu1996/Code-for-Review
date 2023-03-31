class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """最大整除子集
        1. dp
        单串, 位置i必取, O(n)个子问题, 时间复杂度O(n^2)
        dpset[i]表示nums[0..i]的最大整除子集
        """
        n = len(nums)
        nums.sort()
        dpset = {}
        max_l = 0
        res = None
        for i in range(n):
            dpset[i] = set([nums[i]])
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dpset[i]) < len(dpset[j]) + 1:
                    dpset[i] = dpset[j] | set([nums[i]])
            if max_l < len(dpset[i]):
                max_l = len(dpset[i])
                res = dpset[i]
        return list(res)