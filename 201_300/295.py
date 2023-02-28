class MedianFinder:
    """数据流的中位数
    将长度为n的数据流分为两部分, 取n/2个元素分别放入最大堆和最小堆中
    i. (min_len + max_len) % 2 == 0
    => 最大堆长度+1, 最小堆长度不变
    ii.(min_len + max_len) % 2 != 0
    => 最大堆长度不变, 最小堆长度+1
    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        min_len, max_len = len(self.min_heap), len(self.max_heap)
        if (min_len + max_len) % 2 == 0:
            if self.min_heap and num > self.min_heap[0]:
                target = heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, (-target, target))
            else:
                heapq.heappush(self.max_heap, (-num, num))
        else:
            if self.max_heap and num < self.max_heap[0][1]:
                target = heapq.heappop(self.max_heap)[1]
                heapq.heappush(self.max_heap, (-num, num))
                heapq.heappush(self.min_heap, target)
            else:
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        min_len, max_len = len(self.min_heap), len(self.max_heap)
        if min_len < max_len:
            return self.max_heap[0][1]
        elif min_len == max_len:
            return (self.max_heap[0][1]+self.min_heap[0])/2
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()