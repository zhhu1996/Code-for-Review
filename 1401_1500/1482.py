class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """制作m束花所需的最少天数
        1. 二分查找
        实现is_valid函数时, 可以不生成花朵的实际情况
        """
        n = len(bloomDay)
        if n < m*k:
            return -1

        def is_valid(x):
            flower = 0
            res = 0
            for day in bloomDay:
                if day <= x:
                    flower += 1
                    if flower == k:
                        res += 1
                        flower = 0
                else:
                    flower = 0
            return res >= m

        l, r = 1, max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l