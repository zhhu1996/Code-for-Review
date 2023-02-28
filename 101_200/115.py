class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """不同的子序列
        1. 暴力法
        根据s生成所有长度为len(t)的子序列，进行比较
        
        2. dp思路1, 时间复杂度O(n^3), 超时
        dp[i][j]表示s[..i]的子序列中t[..j]出现的个数
        dp[i][j] = sum(dp[k-1][j-1]), s[k]=t[j]

        3. dp思路2, 时间复杂度O(n^2)
        dp[i][j]表示s[..i]的子序列中t[..j]出现的个数, 位置i可不取, 位置j必须取
        i.  s[i] = t[j]
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        ii. s[i] != t[j]
        dp[i][j] = dp[i-1][j]
        """
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

        # 3.
        m, n = len(s), len(t)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # init
        dp[0][0] = 1      # s = ''
        for i in range(1, m+1): # t = ''
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][n]