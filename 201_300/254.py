class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        """因子的组合
        1. 回溯法
        对于当前需要找因子组合的数n来说，遍历2,3...,根号n+1的所有元素，符合条件就进行回溯，注意本身别忘了
        """
        # 方法1
        self.result = []

        def dfs(n, now, path):
            if n == 1:
                if path:
                    self.result.append(path.copy())
                return
            for i in range(now, int(pow(n,0.5))+1):
                if n % i == 0:
                    path.append(i)
                    dfs(n//i, i, path)
                    path.pop()
            if path:
                path.append(n)
                dfs(1, n, path)
                path.pop()

        dfs(n, 2, [])
        return self.result
