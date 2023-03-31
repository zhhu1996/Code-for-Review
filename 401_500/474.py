class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """1和0
        1. dp
        0/1背包
        dp[i][j][k]: 前i个元素使用j个0和k个1能产生最大子集的长度
        => 空间优化
        dp[j][k]: 使用j个0和k个1能产生最大子集的长度
        """
        # # 1. 朴素
        # l = len(strs)
        # dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l+1)]
        # for i in range(1, l+1):
        #     w = strs[i-1]
        #     cur_m, cur_n = 0, 0
        #     for c in w:
        #         if c == '0':
        #             cur_m += 1
        #         else:
        #             cur_n += 1
        #     for j in range(m+1):
        #         for k in range(n+1):
        #             if j < cur_m or k < cur_n:
        #                 dp[i][j][k] = dp[i-1][j][k]
        #             else:
        #                 dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-cur_m][k-cur_n] + 1)
        # return dp[l][m][n]


        # 1. 空间优化
        l = len(strs)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, l+1):
            w = strs[i-1]
            cur_m, cur_n = 0, 0
            for c in w:
                if c == '0':
                    cur_m += 1
                else:
                    cur_n += 1
            for j in range(m,-1,-1):
                for k in range(n,-1,-1):
                    if j < cur_m or k < cur_n:
                        dp[j][k] = dp[j][k]
                    else:
                        dp[j][k] = max(dp[j][k], dp[j-cur_m][k-cur_n] + 1)
        return dp[m][n]