class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """寻找峰值
        1. 二分, 时间复杂度O(logn)
        i.  单峰值
        构造函数, 存在点p, 当x<=p时 f(x)-f(x-1)>0; 当x>p时 f(x)-f(x-1)<0
        ii. 多峰值
        存在点pi, 当pj<x<=pi时 f(x)-f(x-1)>0; 当pi<x<pk时 f(x)-f(x-1)<0
        """
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if mid == 0 or nums[mid] - nums[mid-1] > 0:
                l = mid + 1
            else:
                r = mid - 1
        return l-1