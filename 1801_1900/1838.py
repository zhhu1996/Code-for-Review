class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """最高频元素的频数
        1. 二分+滑动窗口+前缀和, 时间复杂度O(nlogn)
        """
        nums.sort()
        n = len(nums)
        presum = [0]*(n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        def check(x):
            for i in range(x, len(nums)+1):
                cur = x * nums[i-1] - (presum[i] - presum[i-x])
                if cur <= k:
                    return True
            return False

        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l-1