import heapq

class minNode:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __lt__(self, other):
        if self.score == other.score:
            return self.name > other.name
        return self.score < other.score

class maxNode:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __lt__(self, other):
        if self.score == other.score:
            return self.name < other.name
        return self.score > other.score  

class SORTracker:
    """序列顺序查询
    => 数据流中查询第k大的元素
    1. 列表 + 二分查找

    2. 最大堆 + 最小堆
    假设目前有k次查询, 最小堆中即存放前k大的元素
    """

    def __init__(self):
        self.min_heap = [] # 存放前k大元素, 堆顶即为第k大元素
        self.max_heap = []

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.min_heap, minNode(name, score))
        cur = heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap, maxNode(cur.name, cur.score))

    def get(self) -> str:
        cur = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, minNode(cur.name, cur.score))
        return self.min_heap[0].name

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()