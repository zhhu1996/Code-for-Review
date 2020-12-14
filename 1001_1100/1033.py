class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """移动石子直到连续
        最大值 = c-b-1 + b-a-1
        最小值 = 0 if second-first==1 and third-second==1
                1 if second-first in [1,2] or third=second in [1,2]
                2 else
        """
        first = min(a, b, c)
        third = max(a, b, c)
        if a != first and a != third:
            second = a
        if b != first and b != third:
            second = b
        if c != first and c != third:
            second = c
        maxCnt = third - second - 1 + second - first - 1
        if second - first == 1 and third - second == 1:
            minCnt = 0
        elif second - first in [1, 2] or third - second in [1, 2]:
            minCnt = 1
        else:
            minCnt = 2
        return [minCnt, maxCnt]
