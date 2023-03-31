class TimeMap:
    """基于时间的键值存储
    1. 二分, 时间复杂度O(nlogn)
    key为str, value为list, timestamp是递增的list, 可使用二分
    """
    def __init__(self):
        self.kvs = {}
        self.kts = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvs:
            self.kvs[key] = [value]
            self.kts[key] = [timestamp]
        else:
            self.kvs[key].append(value)
            self.kts[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvs:
            return ""
        l, r = 0, len(self.kvs[key])-1
        target = timestamp
        while l <= r:
            mid = (l + r) // 2
            if self.kts[key][mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        # f(l-1) <= target, f(l) > target
        return "" if l == 0 else self.kvs[key][l-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)