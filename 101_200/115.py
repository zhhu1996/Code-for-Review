class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """不同的子序列
        方法1: 暴力法
        根据s生成所有长度为len(t)的子序列，进行比较"""
        # if not s or not t:
        #     return 0

        # candidates = []
        # visited = [False for i in range(len(s))]
        # self.cnt = 0

        # def get_permutation(s, n, index, cur):
        #     if len(cur) == n:
        #         candidates.append(cur.copy())
        #         return
        #     if index >= len(s):
        #         return
        #     for i in range(index, len(s)):
        #         if not visited[i]:
        #             cur.append(s[i])
        #             visited[i] = True
        #             get_permutation(s, n, i + 1, cur)
        #             cur.pop()
        #             visited[i] = False

        # def get_permutation_online(s, t, n, index, lc):
        #     if lc == n:
        #         self.cnt += 1
        #         return
        #     if index >= len(s):
        #         return
        #     for i in range(index, len(s)):
        #         if not visited[i] and t[lc] == s[i]:
        #             visited[i] = True
        #             get_permutation_online(s, t, n, i + 1, lc + 1)
        #             visited[i] = False

        # # get_permutation(s, len(t), 0, [])
        # # cnt = 0
        # # for s in candidates:
        # #     if ''.join(s) == t:
        # #         cnt += 1
        # # return cnt

        # get_permutation_online(s, t, len(t), 0, 0)
        # return self.cnt

        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]