from collections import deque

class MaxQueue:
    """求队列的最大值"""

    def __init__(self):
        self.maxValue = deque()
        self.data = deque()

    def max_value(self) -> int:
        if not self.maxValue:
            return -1
        return self.maxValue[0]

    def push_back(self, value: int) -> None:
        self.data.append(value)
        while self.maxValue and self.maxValue[-1] < value:
            self.maxValue.pop()
        self.maxValue.append(value)

    def pop_front(self) -> int:
        if not self.data:
            return -1
        if self.maxValue and self.data[0] == self.maxValue[0]:
            self.maxValue.popleft()
        return self.data.popleft()

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()