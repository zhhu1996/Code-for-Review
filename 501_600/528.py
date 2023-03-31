class Solution:
    """按权重随机选择
    1. 前缀和 + 二分
    随机生成一个概率值, 然后根据前缀和二分查找确定下标
    """
    def __init__(self, w: List[int]):
        self.n = len(w)
        self.presum = [0]*(self.n+1)
        for i in range(1, self.n+1):
            self.presum[i] = self.presum[i-1] + w[i-1]
        for i in range(1, self.n+1):
            self.presum[i] /= self.presum[-1]

    def pickIndex(self) -> int:
        import random
        target = random.random()
        l, r = 0, self.n-1
        while l <= r:
            mid = (l + r) // 2
            if self.presum[mid+1] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l  


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()