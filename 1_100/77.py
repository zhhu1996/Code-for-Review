class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # 1. itertools.combinations
        # from itertools import combinations
        # return list(combinations(list(range(1,n+1)), k))

        # 2. 回溯
        self.res = []

        def gen_combinations(n, cur, index, k):
            """
                n: 候选列表[1,n]
                cur: 已生成的列表
                index: 当前遍历到的索引
                k: 最大长度
            """
            if len(cur) == k:
                self.res.append(cur.copy())
                return
            for i in range(index, n+1):
                cur.append(i)
                gen_combinations(n, cur, i+1, k)
                cur.pop()

        gen_combinations(n, [], 1, k)
        return self.res