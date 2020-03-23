class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = []
        main = {i: 1 for i in range(-n + 1, n)}  # 主对角线, i-j
        neg = {i: 1 for i in range(2 * n - 1)}  # 负对角线, i+j

        def dfs(row, tmp):
            if row == n:
                self.res.append(tmp.copy())
            for i in range(n):
                if i not in tmp and main[row - i] and neg[row + i]:
                    tmp.append(i)
                    main[row - i] = 0
                    neg[row + i] = 0
                    dfs(row + 1, tmp)
                    tmp.pop()
                    main[row - i] = 1
                    neg[row + i] = 1

        dfs(0, [])

        return len(self.res)