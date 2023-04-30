class SnapshotArray:
    """快照数组
    1. 设计 + 二分
    用哈希表存储所有有变化的位置, val对应(snap_id, element)数组, 搜索<target的最大snap_id
    """

    def __init__(self, length: int):
        self.snap_id = -1
        self.mat = {}

    def set(self, index: int, val: int) -> None:
        if index not in self.mat:
            self.mat[index] = [[self.snap_id], [val]]
        else:
            if self.snap_id == self.mat[index][0][-1]:
                self.mat[index][1][-1] = val
            else:
                self.mat[index][0].append(self.snap_id)
                self.mat[index][1].append(val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.mat:
            return 0
        keys = self.mat[index][0]
        vals = self.mat[index][1]
        n = len(keys)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if keys[mid] < snap_id:
                l = mid + 1
            else:
                r = mid - 1
        # f(l-1) < snap_id
        if l == 0:
            return 0
        return vals[l-1]

        
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)