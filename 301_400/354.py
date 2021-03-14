class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """俄罗斯套娃问题
        方法1：
        动态规划：LIS
        dp[i]表示到第i个元素的最长递增子序列的长度
        dp[i] = max(dp[j]+1, dp[i])
        j<=i and envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]

        方法2：
        对于数组
        (x1,y1) (x2,y2) (x3,y3) ... (x_n,y_n)
        假设按照两维度均升序进行排序，有以下两种情况
        a. 维度1严格递增
        x1 < x2 < x3 < ... < x_n
        直接对第2个维度进行LIS求解

        b. 维度2非严格递增
        x1 <= x2 <= x3 <= ... <= x_n
        运用方法1求解
        或者
        对第一维元素升序排列，第二维元素降序排列
        这样可以保证第一维度相等的元素，第二维度对应的序列不可能成为IS
        之后对第二维度调用LIS即可
        """
        # # 方法1
        # if not envelopes:
        #     return 0
        # n = len(envelopes)
        # dp = [1 for i in range(n)]
        # envelopes.sort(key=lambda x:x[0])
        # print(envelopes)
        # for i in range(n):
        #     for j in range(i):
        #         if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
        #             dp[i] = max(dp[i],dp[j]+1)
        # return max(dp)

        # 方法2
        if not envelopes:
            return 0
        n = len(envelopes)
        dp = [1 for i in range(n)]
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        for i in range(n):
            for j in range(i):
                if envelopes[i][1]>envelopes[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)