from collections import defaultdict

class TopVotedCandidate:
    """在线选举
    1. 二分, 时间复杂度为O(nlogn)
    在k中查询k的索引, 根据索引从v获取对应值
    """

    def __init__(self, persons: List[int], times: List[int]): # 计算v, O(n)
        counters = defaultdict(int)
        counters[persons[0]] += 1
        self.cand = [persons[0]]
        fst_max = (counters[persons[0]], persons[0])
        sec_max = None
        n = len(persons)
        for i in range(1, n):
            pi = persons[i]
            counters[pi] += 1
            if counters[pi] >= fst_max[0]:
                sec_max = (fst_max[0], fst_max[1])
                fst_max = (counters[pi], pi)
            elif counters[pi] >= sec_max[0]:
                sec_max = (counters[pi], pi)
            self.cand.append(fst_max[1])
        self.times = times

    def q(self, t: int) -> int: # 根据q查询, O(logn)
        # k: times, v: cand
        n = len(self.cand)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if self.times[mid] < t:
                l = mid + 1
            else:
                r = mid - 1
        # f(l-1) < t, f(l) >= t
        if l == n:
            return self.cand[-1]
        return self.cand[l] if self.times[l] == t else self.cand[l-1]
        
        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)