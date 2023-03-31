class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """最长数对链(LIS)
        1. dp
        单串, 位置i必取, O(n)个子问题, 时间复杂度O(n^2)
        => 二分法加速, 时间复杂度O(nlogn)
        dp[i]表示长度为(i+1)的IS的末尾最小值
        """
        # # 1. 朴素dp
        # pairs.sort(key=lambda x: x[0])
        # n = len(pairs)
        # dp = [1]*n
        # for i in range(1, n):
        #     for j in range(i):
        #         if pairs[i][0] > pairs[j][1]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

        
        # 1. 二分 + 贪心
        pairs.sort(key=lambda x: x[0])
        print(pairs)
        dp = [pairs[0][1]]
        for i in range(1, len(pairs)):
            target = pairs[i]
            # 寻找第一个大于target[0]的位置进行替换
            l, r = 0, len(dp)-1
            while l <= r:
                mid = (l + r) // 2
                if dp[mid] <= target[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            if target[0] == dp[l-1]:
                continue
            if l == len(dp):
                dp.append(target[1])
            else:
                dp[l] = min(target[1], dp[l])
        return len(dp)