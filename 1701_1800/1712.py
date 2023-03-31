class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """将数组分成三个子数组的方案数
        1. 二分 + 前缀和, 时间复杂度O(nlogn)
        枚举left子数组的最后一个位置, 二分搜索mid子数组的最后一个位置, 统计组合数
        """
        n = len(nums)
        presum = [0]*(n+1)
        res = 0
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]
        for i in range(n-2): # left数组的最后一个位置
            target = presum[i+1]
            l, r = i+1, n-2  # mid数组的最后一个位置
            while l <= r:
                mid = (l + r) // 2
                if presum[mid+1]-target >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            p1 = l
            l, r = i+1, n-2  # mid数组的最后一个位置
            while l <= r:
                mid = (l + r) // 2
                if presum[n]-presum[mid+1] >= presum[mid+1]-target:
                    l = mid + 1
                else:
                    r = mid - 1
            p2 = l-1
            res += max(p2-p1+1, 0)
        return res % (10**9+7)