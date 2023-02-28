class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """滑动窗口最大值
        1. 利用最大堆维护滑动窗口, 时间复杂度O(nlogk)

        2. 利用双端队列维护单调递增性, 时间复杂度O(n)
        """
        # # 1.
        # q, n = [], len(nums)
        # for i in range(k):
        #     q.append((-nums[i], i))
        # heapq.heapify(q)
        # res = [-q[0][0]]
        # for i in range(k, n):
        #     while q and q[0][1] <= i-k:
        #         heapq.heappop(q)
        #     heapq.heappush(q, (-nums[i], i))
        #     res.append(-q[0][0])
        # return res

        # 2.
        from collections import deque
        q, n = deque(), len(nums)
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]
        for i in range(k, n):
            while q and q[0] <= i-k:
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res