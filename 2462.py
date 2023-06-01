class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """雇佣K位工人的总代价
        1. 双指针+最小堆, 时间复杂度klog(n)
        用1个最小堆或2个最小堆存储每一轮的候选集
        """
        import heapq
        arr = []
        n = len(costs)
        heapq.heapify(arr)
        p, q = candidates-1, n-candidates
        for i in range(p+1):
            heapq.heappush(arr, (costs[i], i))
        for j in range(n-1, max(p, q-1), -1):
            heapq.heappush(arr, (costs[j], j))
        ans = 0
        for _ in range(k):
            w, pos = heapq.heappop(arr)
            ans += w
            if pos <= p and p+1 < q:
                p += 1
                heapq.heappush(arr, (costs[p], p))
            elif pos >= q and p+1 < q:
                q -= 1
                heapq.heappush(arr, (costs[q], q))
        return ans