class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """爱吃香蕉的珂珂
        1. 二分查找
        速度的搜索空间为[1, max(piles)], 存在阈值k, 当x<k时, h小时内吃不完香蕉; 当x>=k时, h小时内可吃完香蕉
        """
        n = len(piles)
        l, r = 1, max(piles)

        def is_finish(x):
            needs = 0
            for i in range(len(piles)):
                needs += (piles[i]-1) // x + 1
            return needs <= h

        while l <= r:
            mid = (l + r) // 2
            if is_finish(mid):
                r = mid - 1
            else:
                l = mid + 1
        # f(l-1) = False
        return l