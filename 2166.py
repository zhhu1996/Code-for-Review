class Bitset:
    """设计位集
    1. 双集合法

    2. 懒标记法
    懒惰标记，就是动作发出时，记录下动作，而并不真正的执行，等到真正应用时再执行
    """

    def __init__(self, size: int):
        self.ones = 0
        self.zeros = size
        self.one_set = set()
        self.zero_set = set(list(range(size)))

    def fix(self, idx: int) -> None:
        if idx not in self.one_set:
            self.one_set.add(idx)
            self.ones += 1
            self.zero_set.remove(idx)
            self.zeros -= 1

    def unfix(self, idx: int) -> None:
        if idx not in self.zero_set:
            self.zero_set.add(idx)
            self.zeros += 1
            self.one_set.remove(idx)
            self.ones -= 1

    def flip(self) -> None:
        self.one_set, self.zero_set = self.zero_set, self.one_set
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        return self.zeros == 0

    def one(self) -> bool:
        return self.ones >= 1

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        ans = ['0']*(self.ones + self.zeros)
        for c in self.one_set:
            ans[c] = '1'
        return ''.join(ans)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()