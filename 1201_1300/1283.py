class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """使结果不超过阈值的最小除数
        1. 二分
        """
        if len(nums) > threshold:
            return -1

        def is_valid(x):
            res = 0
            for num in nums:
                res += (num-1)//x + 1
            return res <= threshold

        n = len(nums)
        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        # f(l-1) = False
        return l