from heapq import *

class MedianFinder:
    """数据流的中位数
    将数据流分为两部分，左边区间内用最大堆存储最大的元素，右边区间用最小堆存储最小的元素，
    中位数即是两个数的平均值
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = [] # i
        self.maxHeap = [] # (-i, i)

    def addNum(self, num: int) -> None:
        minLen, maxLen = len(self.minHeap), len(self.maxHeap)
        if (minLen + maxLen) % 2 == 0: # 最小堆元素个数不变，最大堆元素个数+1
            if self.minHeap and num > self.minHeap[0]:
                result = heappop(self.minHeap)
                heappush(self.minHeap, num)
                heappush(self.maxHeap, (-result, result))
            else:
                heappush(self.maxHeap, (-num, num))
        else: # 最大堆元素个数不变，最小堆元素个数+1
            if self.maxHeap and num < self.maxHeap[0][1]:
                result = heappop(self.maxHeap)
                heappush(self.minHeap, result[1])
                heappush(self.maxHeap, (-num, num))
            else:
                heappush(self.minHeap, num)

    def findMedian(self) -> float:
        if not self.minHeap and not self.maxHeap:
            return None
        minLen, maxLen = len(self.minHeap), len(self.maxHeap)
        if minLen > maxLen:
            return self.minHeap[0]
        elif minLen == maxLen:
            return (self.minHeap[0] + self.maxHeap[0][1]) / 2
        else:
            return self.maxHeap[0][1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()