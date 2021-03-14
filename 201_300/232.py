class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.head = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1 and self.s2:
            while self.s2:
                d = self.s2.pop(-1)
                self.s1.append(d)
        self.s1.append(x)
        if len(self.s1) == 1:
            self.head = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.s1:
            d = self.s1.pop(-1)
            self.s2.append(d)
        d = self.s2.pop(-1)
        if self.s2:
            self.head = self.s2[-1]
        else:
            self.head = None
        return d

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.head

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) + len(self.s2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()