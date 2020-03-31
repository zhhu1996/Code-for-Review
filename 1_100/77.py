class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1. 回溯法
        # https://leetcode-cn.com/problems/combinations/solution/hui-su-si-xiang-tuan-mie-pai-lie-zu-he-zi-ji-wen-2/
        self.result = []
        self.recur(n, [], k, 1)
        return self.result

    def recur(self, n, nlist, k, index):
        # n代表原列表的长度，nlist代表新生成的列表，k表示组合数的个数，index表示当前索引，length表示长度
        # 每次从[index, n]中挑选一个数进行递归，直到生成列表的长度等于k就返回
        if len(nlist) == k:
            self.result.append(nlist.copy())
            return

        for i in range(index, n + 1):
            if i not in nlist:
                nlist.append(i)
                self.recur(n, nlist, k, i + 1)
                nlist.pop()