class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """将 x 减到 0 的最小操作数
        1. 变长滑动窗口
        => 寻找和为sum(nums)-x的最长子数组
        """
        n, total = len(nums), sum(nums)
        if total - x < 0:
            return -1
        l, r = 0, 0
        cursum = 0
        res = -1
        while r < n:
            cursum += nums[r]
            while cursum > total - x:
                cursum = cursum - nums[l]
                l += 1
            if cursum == total - x:
                res = max(res, r-l+1)
            r += 1
        return -1 if res < 0 else n-res  
