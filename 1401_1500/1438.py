from collections import defaultdict, deque
from queue import Queue
from heapq import *


class WindowQueue:
    def __init__(self):
        self.maxQueue = deque()  # 第一个元素是最大值，之后是降序排列
        self.minQueue = deque()  # 第一个元素是最小值，之后是升序排列

    def push(self, x):
        while len(self.maxQueue) > 0 and x > self.maxQueue[-1]:
            self.maxQueue.pop()
        self.maxQueue.append(x)
        while len(self.minQueue) > 0 and x < self.minQueue[-1]:
            self.minQueue.pop()
        self.minQueue.append(x)

    def pop(self, x):
        if len(self.maxQueue) > 0 and x == self.maxQueue[0]:
            self.maxQueue.popleft()
        if len(self.minQueue) > 0 and x == self.minQueue[0]:
            self.minQueue.popleft()

    def diff(self):
        return self.maxQueue[0] - self.minQueue[0]


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """绝对差不超过限制的最长连续子数组
        1. 滑动窗口 + 双端队列
        最大值队列第一个元素是最大值，之后降序排列；
        最小值队列第一个元素是最小值，之后升序排列

        2. 滑动窗口 + 堆
        堆中记录最大值与最小值
        """
        if not nums or limit < 0:
            return 0
        i, j, n = 0, 0, len(nums)
        maxLen = 0
        window = WindowQueue()
        while j < n:
            window.push(nums[j])
            while window.diff() > limit:
                window.pop(nums[i])
                i += 1
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen
