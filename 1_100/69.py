class Solution:
    def mySqrt(self, x):
        # 1. 二分查找
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
