class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """最长的斐波那契子数列的长度
        dp[i][j]表示以a[i], a[j]结尾的fib数列的最大长度
        寻找k < i使得 a[k] + a[i] = a[j]
        => dp[i][j] = max(dp[k][i] + 1)
        1. 暴力, 时间复杂度O(n^3)
        2. 用map存储arr, key为数组的值, value为索引, 时间复杂度O(n^2), 空间复杂度O(n)
        """
        # # 1. 
        # if len(arr) <= 2:
        #     return 0
        # n = len(arr)
        # res = -float('inf')
        # dp = [[0 for i in range(n)] for j in range(n)]
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         for k in range(i):
        #             if arr[k] + arr[i] == arr[j]:
        #                 dp[i][j] = max(dp[i][j], dp[k][i]+1)
        #         res = max(res, dp[i][j])
        # if res > 0:
        #     res += 2
        # return res

        # 2.
        if len(arr) <= 2:
            return 0
        n = len(arr)
        res = -float('inf')
        idict = {arr[i]: i for i in range(n)}
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[j] - arr[i] in idict and idict[arr[j] - arr[i]] < i:
                    k = idict[arr[j] - arr[i]]
                    dp[i][j] = max(dp[i][j], dp[k][i]+1)
                res = max(res, dp[i][j])
        if res > 0:
            res += 2
        return res