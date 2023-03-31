class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """袋子里最少数目的球
        1. 二分查找, 时间复杂度O(nlogC), C=max(nums)
        最小开销的搜索空间为[1, max(nums)], 存在点p, 当x<p时不可以分配; 当x>=p时可以分配
        """

        def is_valid(x):
            k = maxOperations
            for i in range(len(nums)):
                if nums[i] <= x:
                    continue
                if nums[i] % x == 0:
                    k -= (nums[i] // x - 1)
                else:
                    k -= nums[i]//x
                if k < 0:
                    return False
            return True

        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        # f(l-1) = False
        return l