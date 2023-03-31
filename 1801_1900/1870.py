class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """准时到达的列车最小时速
        1. 二分查找, 时间复杂度O(nlogn)
        """
        def is_valid(x):
            need = 0
            for i in range(len(dist)):
                d = dist[i]
                if i < len(dist)-1:
                    need += (d-1)//x+1
                else:
                    need += d/x
            return need <= hour

        l, r = 1, 10**7
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        # f(l-1) = False
        return l if l-1 != 10**7 else -1   