class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        """中心对称数II
        1. 生成所有的n位整数，然后判断是否是中心对称，超时了

        2. 根据table生成所有的key

        """
        self.candidates = []

        def isStrobo(num, start, end, table):
            if start > end:
                return True
            if num[start] not in table or num[end] not in table or table[num[start]] != num[end]:
                return False
            return isStrobo(num, start + 1, end - 1, table)

        def getCandidates(n, index, path, table):
            if index == n:
                self.candidates.append("".join(path))
                return
            for j in sorted(table.keys()):
                if index == 0 and j == "0" and n > 1:
                    continue
                path.append(j)
                getCandidates(n, index + 1, path, table)
                path.pop()

        def getResult(left, right, now, table):
            if left > right:
                self.candidates.append("".join(now))
                return
            keys = table.keys()
            for k in keys:
                if k == "0" and left < right and left == 0:
                    continue
                if left > right:
                    continue
                if left == right and table[k] != k:
                    continue
                now[left] = k
                now[right] = table[k]
                getResult(left + 1, right - 1, now, table)


        result = []
        table = {"1": "1", "6": "9", "8": "8", "9": "6", "0": "0"}
        nums = ["0"] * n
        getResult(0, n - 1, nums, table)
        return self.candidates
