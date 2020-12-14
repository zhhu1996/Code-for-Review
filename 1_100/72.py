class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """编辑距离"""

        m, n = len(word1), len(word2)
        if m * n == 0:
            return m + n

        op = [[0]*(n+1) for i in range(m+1)]
        for i in range(n+1):
            op[0][i] = i
        for j in range(m+1):
            op[j][0] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    op[i][j] = op[i-1][j-1]
                else:
                    op[i][j] =  1 + min(op[i-1][j-1], op[i-1][j], op[i][j-1])
        return op[m][n]