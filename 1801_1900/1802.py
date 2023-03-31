class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """有界数组中指定下标处的最大值
        元素之间的约束: nums[i] - 1 <= nums[i+1] <= nums[i] + 1
        1. 贪心 + 二分, 时间复杂度O(log(maxSum))
        构造函数, nums[index]的搜索空间为[1, maxSum], 存在点p, 当x<p时 f(x)<=maxSum; 当x>=p时 f(x)>maxSum
        check函数的时间复杂度必须优化到O(1)才不超时
        """
        def calc(x, length):
            # 计算x-length,...,x-1的和
            res = 0
            if x - length >= 1:
                small = x - length
                res += (small + x - 1) * length // 2
            else:
                ones = length - (x-1)
                res += x * (x-1) // 2
                res += ones
            return res 

        def check(x): # O(n) -> O(1)
            res = x + calc(x, index) +  calc(x, n-index-1)
            return res <= maxSum
            
        l, r = 1, maxSum
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        # f(l-1) <= maxSum
        return l-1