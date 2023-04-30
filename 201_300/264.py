class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """丑数II
        1. 生成法, 时间复杂度O(nlogn)
        哈希表/集合+最小堆

        2. dp + 二分查找, 时间复杂度O(nlogn)
        单串, 位置i必须取, O(n)个子问题

        3. dp + 三指针法, 时间复杂度O(n)
        3个严格递增的数组, 分别表示2/3/5的倍数, 进行merge
        pi表示有资格与i相乘的丑数位置
        """
        # # 1.
        # import heapq
        # exs = set()
        # arr = [1]
        # alpha = [2,3,5]
        # heapq.heapify(arr)
        # exs.add(1)
        # cnt = 0
        # while True:
        #     cur = heapq.heappop(arr)
        #     cnt += 1
        #     if cnt == n:
        #         return cur
        #     for i in range(3):
        #         beta = cur * alpha[i]
        #         if beta not in exs:
        #             exs.add(beta)
        #             heapq.heappush(arr, beta)

        # # 2. 
        # dp = [0]*n
        # dp[0] = 1
        # for i in range(1, n):
        #     div = [2,3,5]
        #     min_v = float('inf')
        #     for j in range(3):
        #         target = dp[i-1] // div[j]
        #         l, r = 0, i-1
        #         while l <= r:
        #             mid = (l + r) // 2
        #             # f(l-1)<=target, f(r+1)>target
        #             if dp[mid] <= target:
        #                 l = mid + 1
        #             else:
        #                 r = mid - 1
        #         if l < i:
        #             min_v = min(min_v, div[j]*dp[l])
        #     dp[i] = min_v
        # return dp[n-1]

        # 3.
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[n]