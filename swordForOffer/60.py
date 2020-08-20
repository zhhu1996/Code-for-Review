class Solution:
    def twoSum(self, n: int) -> List[float]:
        """n个骰子的点数
        1. 回溯法，时间复杂度：指数级

        2. 动态规划, 时间复杂度：平方级
        设k个骰子，和为s出现的次数为f[k][s]
        则f[k][s] = f[k-1][s-1] + f[k-1][s-2] + f[k-1][s-3] + f[k-1][s-4] + f[k-1][s-5] + f[k-1][s-6]
        """
        # 方法1
        # self.probability = [0 for i in range(6*n+1)]
        #
        # def getProbability(n, nowSum):
        #     if n < 1:
        #         self.probability[nowSum] += 1
        #         return
        #     for i in range(1, 7):
        #         getProbability(n-1, nowSum+i)
        #
        # getProbability(n, 0)
        # base = 6 ** n
        # for i in range(len(self.probability)):
        #     self.probability[i] /= base
        # return self.probability[n:]

        # 方法2
        self.probability = [[0] * (6 * n + 1) for i in range(n + 1)]
        for i in range(1, 7):
            self.probability[1][i] = 1

        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for k in range(j - 1, j - 7, -1):
                    if k >= 0:
                        self.probability[i][j] += self.probability[i - 1][k]
        base = 6 ** n
        for i in range(len(self.probability[0])):
            self.probability[n][i] /= base

        return self.probability[n][n:]
