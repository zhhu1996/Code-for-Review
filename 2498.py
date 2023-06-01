class Solution:
    def maxJump(self, stones: List[int]) -> int:
        """青蛙过河II
        1. 贪心, 时间复杂度O(n)
        假设4个点a,b,c,d
        不使用间隔: a->d->c->b->a
        间隔跳: a->c->d->b->a
        max(c-a, d-b) < (d-a)

        2.二分查找, 时间复杂度O(nlogn)
        """
        # 1.
        res = stones[1] - stones[0]
        for i in range(2, len(stones)):
            res = max(res, stones[i] - stones[i-2])
        return res


        # 2.
        n = len(stones)
        zset = set(stones)

        def check(x):
            visit = set()
            i, j = 1, 0
            while i < n:
                if abs(stones[i]-stones[j]) <= x:
                    i += 1
                elif i != j+1:
                    j = i-1
                    visit.add(j)
                else:
                    return False

            i, j = n-2, n-1
            while i >= 0:
                if i in visit:
                    i -= 1
                    continue
                if abs(stones[i]-stones[j]) > x:
                    return False
                j = i
                i -= 1
            return True
            
        l, r = 0, stones[-1]
        while l <= r:
            mid = (l + r) // 2
            if not check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l