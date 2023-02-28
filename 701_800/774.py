class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        """最小化去加油站的最大距离
        1. 二分查找最小的最大间距
        最大间距的范围为[0, 10**8], 随着最大间距的减小, 新增加油站的数量一定会变多, 存在单调递减性
        """
        def is_possible(stations, d, k):
            cnt = 0
            for i in range(1, len(stations)):
                cnt += int((stations[i]-stations[i-1])/d)
            return cnt <= k

        left, right = 0, 10**8
        while right - left > 10**-6:
            mid = (left + right) / 2
            if is_possible(stations, mid, k):
                right = mid
            else:
                left = mid+10**-6
        return left