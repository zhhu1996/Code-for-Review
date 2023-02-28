class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """和为k的最短子数组
        1. 暴力 + 前缀和, 时间复杂度O(n^2)

        2. 滑动窗口(单调队列) + 前缀和
        """
        # # 1.
        # n = len(nums)
        # cumsum = [0]*(n+1)
        # for i in range(1, n+1):
        #     cumsum[i] = cumsum[i-1] + nums[i-1]
        # for lth in range(1, n+1):
        #     for l in range(0, n-lth+1):
        #         r = l + lth - 1
        #         if cumsum[r+1]-cumsum[l] >= k:
        #             return lth
        # return -1

        # 2.
        from collections import deque
        n = len(nums)
        cumsum = [0]*(n+1)
        res = float('inf')
        for i in range(1, n+1):
            cumsum[i] = cumsum[i-1] + nums[i-1] 
        q = deque()
        for i in range(len(cumsum)):
            while q and cumsum[i] - cumsum[q[0]] >= k: # s[i] > s[j]
                res = min(res, i-q.popleft())
            while q and cumsum[i] <= cumsum[q[-1]]:    # s[i] < s[j]
                q.pop()
            q.append(i)
        return res if res <= n else -1