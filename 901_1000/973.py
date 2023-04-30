class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """最接近原点的k个点
        1. 排序(快排/堆排序)
        """
        d = []
        for p in points:
            cur = p[0]*p[0] + p[1]*p[1]
            d.append((cur, p))
        d.sort()
        return [d[i][1] for i in range(k)]