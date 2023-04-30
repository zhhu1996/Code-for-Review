class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """递增的三元子序列
        1. LIS, 时间复杂度O(nlogn)
        求LIS, 大于等于3即存在

        2. 贪心
        """
        n = len(nums)
        if n < 3: return False

        small, mid = float('inf'), float('inf')
        for t in range(n):
            if nums[t] <= small:
                small = nums[t]
            elif nums[t] <= mid:
                mid = nums[t]
            else:
                return True
        return False