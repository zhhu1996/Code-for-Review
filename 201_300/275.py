class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """H指数II
        1. 二分查找
        最小值最大化, 构造函数f(x), 存在点p, 当x<=p时 f(x)=True, x>p时 f(x)=False
        => 利用数组的有序性, 可将f(x)的时间复杂度降低到O(1)
        """
        # 1.
        def is_valid(x):
            h = 0
            for c in citations:
                if c >= x:
                    h += 1
            return h >= x

        def is_valid_qk(x):
            return citations[x] >= len(citations)-x

        # l, r = 0, len(citations)
        # while l <= r:
        #     mid = (l + r) // 2
        #     if is_valid(mid):
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return l-1

        # 1. f(x)优化
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if is_valid_qk(mid):
                r = mid - 1
            else:
                l = mid + 1
        return n-l