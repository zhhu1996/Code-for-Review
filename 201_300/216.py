class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []

        def getCandidate(n, k, index, nowSum, path):
            if len(path) == k:
                if nowSum == n:
                    self.result.append(path.copy())
                return
            for j in range(index, 10):
                path.append(j)
                getCandidate(n, k, j + 1, nowSum + j, path)
                path.pop()

        getCandidate(n, k, 1, 0, [])
        return self.result
